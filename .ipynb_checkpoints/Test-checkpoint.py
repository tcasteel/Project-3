import requests
import pandas as pd
from flask import Flask, render_template
from pathlib import Path

app = Flask(__name__, template_folder=(Path(__file__).parent / 'Templates').resolve())

geo_url = 'https://api.census.gov/data/2022/acs/acsse?get=NAME,K200701_001E&for=place:*&key=9eae9971d44f700fff84404097248e88ccfc813c'
geo_response = requests.get(geo_url)
geo_json_response = geo_response.json()

geo_data = pd.DataFrame(geo_json_response[1:], columns=geo_json_response[0])
geo_data = geo_data.rename(columns={'K200701_001E': 'Geographical Mobility total'})
geo_data = geo_data.dropna()
geo_data['Geographical Mobility total'] = geo_data['Geographical Mobility total'].astype(int)
geo_data = geo_data.sort_values('Geographical Mobility total', ascending=False)

transportationurl = 'https://api.census.gov/data/2022/acs/acsse?get=NAME,K202403_007E&for=place:*&key=9eae9971d44f700fff84404097248e88ccfc813c'
transportationresponse = requests.get(transportationurl)
transportationjson_response = transportationresponse.json()

transportation_data = pd.DataFrame(transportationjson_response[1:], columns=transportationjson_response[0])
transportation_data = transportation_data.rename(columns={'K202403_007E': 'Total Employed in Transportation'})
transportation_data = transportation_data.dropna()
transportation_data = transportation_data.loc[
    (transportation_data['Total Employed in Transportation']) != '0']

transportation_data['Total Employed in Transportation'] = transportation_data[
    'Total Employed in Transportation'].astype(int)
transportation_data = transportation_data.sort_values('Total Employed in Transportation', ascending=False)

@app.route('/')
def index():
    tables = [geo_data, transportation_data]
    return render_template('Test.html', tables=tables)

    # print("Geo Data:", geo_data)
    # print("Transportation Data:", transportation_data)
    # return render_template('Test.html', geo_data=geo_data, transportation_data=transportation_data)

if __name__ == '__main__':
    app.run(debug=True, port=5002)



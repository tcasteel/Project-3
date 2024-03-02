const express = require('express');
const axios = require('axios');
const path = require('path');
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

const express = require('express');
const axios = require('axios');

const app = express();
const port = 5002;

app.get('/', async (req, res) => {
  try {
    const geoUrl = 'https://api.census.gov/data/2022/acs/acsse?get=NAME,K200701_001E&for=place:*&key=9eae9971d44f700fff84404097248e88ccfc813c';
    const geoResponse = await axios.get(geoUrl);
    const geoJsonResponse = geoResponse.data;

    let geoData = geoJsonResponse.slice(1).map(item => ({
      NAME: item[0],
      'Geographical Mobility total': parseInt(item[1]),
      place: item[2],
    }));

    geoData = geoData.filter(item => !isNaN(item['Geographical Mobility total']));

    geoData = geoData.sort((a, b) => b['Geographical Mobility total'] - a['Geographical Mobility total']);

    const transportationUrl = 'https://api.census.gov/data/2022/acs/acsse?get=NAME,K202403_007E&for=place:*&key=9eae9971d44f700fff84404097248e88ccfc813c';
    const transportationResponse = await axios.get(transportationUrl);
    const transportationJsonResponse = transportationResponse.data;

    let transportationData = transportationJsonResponse.slice(1).map(item => ({
      NAME: item[0],
      'Total Employed in Transportation': parseInt(item[1]),
      place: item[2],
    }));

    transportationData = transportationData.filter(item => item['Total Employed in Transportation'] !== 0);

    transportationData = transportationData.sort((a, b) => b['Total Employed in Transportation'] - a['Total Employed in Transportation']);

    res.render('base.html', { geoData, transportationData });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).send('Internal Server Error');
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

CREATE TABLE city_growth(
citystate varchar PRIMARY KEY NOT NULL,
pop_2017 int,
pct_growth_2018 decimal(6,2),
pct_growth_2019 decimal(6,2),
pct_growth_2020 decimal(6,2),
pct_growth_2021 decimal(6,2),
pct_growth_2022 decimal(6,2)
);

SELECT * from city_growth
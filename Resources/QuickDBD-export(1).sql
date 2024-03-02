-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

CREATE TABLE "tx_zip_pop" (
    "Zip" int   NOT NULL,
    "City" varchar   NOT NULL,
    "County" varchar   NOT NULL,
    "Latitude" numeric   NOT NULL,
    "Longitude" numeric   NOT NULL,
    "Pop_2017" int   NOT NULL,
    "Pop_2018" int   NOT NULL,
    "Pop_2019" int   NOT NULL,
    "Pop_2020" int   NOT NULL,
    "Pop_2021" int   NOT NULL,
    "Pop_2022" int   NOT NULL,
    CONSTRAINT "pk_tx_zip_pop" PRIMARY KEY (
        "Zip"
     )
);

CREATE TABLE "tx_zip_growth" (
    "Zip" int   NOT NULL,
    "City" varchar   NOT NULL,
    "County" varchar   NOT NULL,
    "Latitude" numeric   NOT NULL,
    "Longitude" numeric   NOT NULL,
    "Growth_2018" numeric   NOT NULL,
    "Growth_2019" numeric   NOT NULL,
    "Growth_2020" numeric   NOT NULL,
    "Growth_2021" numeric   NOT NULL,
    "Growth_2022" numeric   NOT NULL,
    CONSTRAINT "pk_tx_zip_growth" PRIMARY KEY (
        "Zip"
     )
);

ALTER TABLE "tx_zip_pop" ADD CONSTRAINT "fk_tx_zip_pop_Zip_City_County_Latitude_Longitude" FOREIGN KEY("Zip", "City", "County", "Latitude", "Longitude")
REFERENCES "tx_zip_growth" ("Zip", "City", "County", "Latitude", "Longitude");

SELECT * FROM "tx_zip_pop";

SELECT * FROM "tx_zip_growth";
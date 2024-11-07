CREATE DATABASE testfligoo;

-- Cambia a la base de datos testfligoo
\c testfligoo;

CREATE TABLE testdata(
 flight_date            DATE,
 flight_status          VARCHAR NOT NULL,
 departure_airport      VARCHAR,
 departure_timezone     VARCHAR,
 arrival_airport        VARCHAR,
 arrival_terminal       INT,
 arrival_timezone       VARCHAR,
 airline_name           VARCHAR,
 flight_number          INT

)
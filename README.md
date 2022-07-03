# Productivity App

## Local Setup / Installation
Postgres DB set up named "productivity" with username
padmin with password ppassword.

Add section in config.ini to match the following:

`[postgresql]  
host=localhost  
database=productivity  
user=padmin  
password=ppassword`

## Running locally
`ng serve` Opens to 4200

## Modifying the Schema
If the schema for any table is edited or added, the script to create the table should be added to ./sql/table with "create_tablename.sql" as the format, and then the name of the table added to the TABLES array constant in the dbservice class.

## Todo
- Setup DB repo stuff to create tables if they do not exist
- Set up SW with PWA so that it works offline and can sync up
- Set up separate users
- Logging
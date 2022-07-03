# Productivity App

## Local Setup / Installation
1. Install PostgreSQL latest stable version with pgAdmin 4.
2. Set the default password for the default user <i>(`postgres`)</i> to `root`.
3. Install Python 3.10 and pip3.
4. Using pip3, install the following packages: `psycopg2`, and `flask`.
5. After cloning the repo, cd into `app` and run `npm install`.

## Running locally
1. `cd` to `/app`
2. Open another terminal in this directory.
3. Run in one terminal: `ng serve` Runs the client app on localhost:4200.
4. Run in the other terminal: `npm run flask` Runs the Python Flask API on localhost:5000.

## Modifying the Schema
If the schema for any table is edited or added, the script to create the table should be added to `/database/sql/`table with "create_tablename.sql" as the format, and then the name of the table added to the TABLES array constant in the dbservice class.

<i>TODO:</i>
For migrations to add data to a table create the SQL script in `/database/sql/table/add_tablename.sql`.

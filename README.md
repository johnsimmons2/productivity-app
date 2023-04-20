# Productivity App

A work in progress productivity app to track habits and chores and whatever other neat features I feel like adding.

Built with PostgreSQL databases, DJango (Python) backend, Angular front-end.

- Backend is in `./api`
- Frontend is in `./app`

## Local Setup / Installation
0. Make sure you have node.js, npm, and @angular/cli with its dependencies.
1. Install PostgreSQL latest stable version with pgAdmin 4.
2. Set the default password for the default user <i>`(postgres)`</i> to `root`.
3. Install Python 3.10 and pip3.
4. Using pip3, install the following packages: `psycopg2`, and `flask`.
5. After cloning the repo, cd into `app` and run `npm install`.

## Running locally
Front end
1. `cd` to `/app`
2. Open another terminal in this directory.
3. Run in one terminal: `ng serve` Runs the client app on localhost:4200.

API
1. `cd` to `/app`
2. Run in terminal: `npm run flask` Runs the Python Flask API on localhost:5000.

Full Stack
1. `cd` to `/app`
2. Open 3 terminals
3. Run the following in order: `npm run watch:app`, `npm run watch:sw`, `npm run server`.

## Modifying the Schema
If the schema for any table is edited or added, the script to create the table should be added to `/database/sql/`table with "create_tablename.sql" as the format, and then the name of the table added to the TABLES array constant in the dbservice class.

<i>TODO:</i>
For migrations to add data to a table create the SQL script in `/database/sql/table/add_tablename.sql`.

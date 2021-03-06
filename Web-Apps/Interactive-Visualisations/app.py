import psycopg2

import csv

import json
import collections
import flask
import pandas as pd

#################################################
# Flask Setup
#################################################
app = flask.Flask(__name__)

#################################################
# Database Setup
#################################################
def get_db_connection():
    conn = psycopg2.connect(user='postgres',
                            password='meg221196',
                            host='localhost',
                            port='5432',
                            database='integrated_covid_view_db')
    return conn

#################################################
# Flask Routes
#################################################
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM full_covid_table;')
    rows = cur.fetchall()

    covid_data_dict = []
    for row in rows:
        d = collections.OrderedDict()
        d['country_id'] = row[0]
        d['country_name'] = row[1]
        d['continent_name'] = row[2]
        d['population'] = row[3]
        d['date'] = row[4]
        d['confirmed'] = row[5]
        d['deaths'] = row[6]
        d['recovered'] = row[7]
        d['active'] = row[8]
        d['case_fatality'] = row[9]
        d['new_cases'] = row[10]
        d['new_deaths'] = row[11]
        d['new_recovered'] = row[12]
        d['vaccinated_per_hundred'] = row[13]
        d['fully_vaccinated_per_hundred'] = row[14]
        d['boosted_per_hundred'] = row[15]
        d['not_fully_vaccinated_per_hundred'] = row[16]
        d['hospital_occupancy'] = row[17]
        covid_data_dict.append(d)

    covid_data = json.dumps(covid_data_dict)

    cur.close()
    conn.close()
    response = flask.jsonify(covid_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)
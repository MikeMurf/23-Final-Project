import psycopg2

import csv

import pickle
import json
import collections
import flask
import pandas as pd

#################################################
# Flask Setup
#################################################
app = flask.Flask(__name__)

#################################################
# Model Import
# Use pickle to load in the pre-trained model
#################################################
with open(f'model/bike_model_xgboost.pkl', 'rb') as f:
    model = pickle.load(f)

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

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('new_forecast.html'))
    if flask.request.method == 'POST':
        conf_cases = flask.request.form['conf_cases']
        conf_deaths = flask.request.form['conf_deaths']
        conf_recovered = flask.request.form['conf_recovered']
        conf_active = flask.request.form['conf_active']
        input_variables = pd.DataFrame([[conf_cases, conf_deaths, conf_recovered, conf_active]],
                                       columns=['confirmed_cases', 'confirmed_deaths',
                                       'confirmed_recovered', 'confirmed_active'],
                                       dtype=float)
        prediction = model.predict(input_variables)[0]
        return flask.render_template('new_forecast.html',
                                     original_input={'Confirmed Cases':conf_cases,
                                                     'Confirmed Deaths':conf_deaths,
                                                     'Confirmed Recovered':conf_recovered,
                                                     'Confirmed Active':conf_active},
                                     result=prediction,
                                     )

if __name__ == '__main__':
    app.run(debug=True)

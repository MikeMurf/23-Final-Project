import pickle
import flask
import pandas as pd

#################################################
# Flask Setup
#################################################
app = flask.Flask(__name__, template_folder='templates')

#################################################
# Model Import
# Use pickle to load in the pre-trained model
#################################################
filename = "../../Machine-Learning/hospitalisations_model.pkl"
model = pickle.load(open(filename, "rb"))

#################################################
# Flask Routes
#################################################
@app.route('/', methods=['GET','POST'])
def index():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))
    if flask.request.method == 'POST':
        conf_cases = flask.request.form['conf_cases']
        conf_deaths = flask.request.form['conf_deaths']
        conf_recovered = flask.request.form['conf_recovered']
        conf_active = flask.request.form['conf_active']
        input_variables = pd.DataFrame([[conf_cases, conf_deaths, conf_recovered, conf_active]],
                                        columns=['confirmed', 'deaths',
                                        'recovered', 'active'],
                                        dtype=float)
        prediction = model.predict(input_variables).item()
        return flask.render_template('index.html',
                                    original_input={'Confirmed Cases':conf_cases,
                                                    'Confirmed Deaths':conf_deaths,
                                                    'Confirmed Recovered':conf_recovered,
                                                    'Confirmed Active':conf_active},
                                    result=round(prediction)
                                    )

if __name__ == '__main__':
    app.run(debug=True)
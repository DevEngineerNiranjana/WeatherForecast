import logging
import flask
from flask import render_template
from common.get_config_data import ParseConfig
from schema.ManageDatapoints.features_blueprint import weather_blueprint

logging.basicConfig(format='%(levelname)s-%(asctime)s-%(message)s', level=logging.DEBUG)
logging.info('Logger initiated.')

parser_obj = ParseConfig('config.ini')
results = parser_obj.get_server_details()
host = results["host"]
port = int(results["port"])

app = flask.Flask(__name__, static_folder='static/')
app.debug = True
logging.info("Flask is initialized..")


@app.route('/')
def index():
    low_temp = 25
    high_temp = 40
    return render_template('index.html', lt=low_temp, ht=high_temp)


@app.route('/manage')
def manage():
    status = ""
    return render_template('manage.html', st=status)


@app.route('/details')
def details():
    status = ""
    return render_template('details.html', st=status)


# @app.route('/mapbox_js')
# def mapbox_js():
#     return render_template(
#         'mapbox_js.html',
#         ACCESS_KEY=MAPBOX_ACCESS_KEY
#     )


app.register_blueprint(weather_blueprint)

if __name__ == "__main__":
    app.run(host, port)
    print("Terminating..")

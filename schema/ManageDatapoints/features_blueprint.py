from flask import Blueprint, request, render_template
from common.utilities import return_response, format_data
from schema.ManageDatapoints.functions.manage_datapoints import DataPoints

weather_blueprint = Blueprint("weather_forecast", __name__)


@weather_blueprint.route('/data-points/<string:location>', methods=['GET', 'PUT', 'DELETE'])
def data_point(location):
    obj = DataPoints()
    if request.method == 'GET':
        resp, data = obj.get_data_point(location)
        if resp:
            return return_response("success", data), 200
        return return_response("Failed to add data point"), 404

    elif request.method == 'PUT':
        json_data = request.json
        resp = obj.update_data_point(location, json_data)
        if resp:
            return return_response("success", resp), 200
        return return_response("Failed to update data point"), 404

    elif request.method == 'DELETE':
        resp = obj.delete_data_point(location)
        if resp:
            return return_response("success", resp), 200
        return return_response("Failed to delete data point"), 404
    else:
        return return_response("Invalid request"), 404


@weather_blueprint.route('/rerun-forecast/<string:latitude>/<string:longitude>', methods=['POST'])
def forecast(latitude, longitude):
    obj = DataPoints()
    if request.method == 'POST':
        resp = obj.rerun_forecast(latitude, longitude)
        if resp:
            return return_response("success"), 200
        return return_response("Failed to rerun forecast"), 404


@weather_blueprint.route('/data-points', methods=['GET', 'POST'])
def data_points():
    obj = DataPoints()
    if request.method == 'POST':
        data = request.form.to_dict()
        resp = obj.add_data_point(data)
        if resp:
            return render_template('index.html', st=resp)
        return render_template('index.html', st=resp)
    elif request.method == 'GET':
        resp, data = obj.get_all_data_point()
        if resp:
            return render_template('details.html', results=data)
        return render_template('index.html', st=resp)
    else:
        return render_template('index.html', st="failed")


@weather_blueprint.route('/fetch-points', methods=['GET'])
def fetch_points():
    formatted_data = []
    if request.method == 'GET':
        obj = DataPoints()
        resp, data = obj.get_all_data_point()
        formatted_data = format_data(data)
        return formatted_data
    else:
        return formatted_data

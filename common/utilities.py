import json


def return_response(msg, data=""):
    response = {
        "msg": msg,
        "data": data
    }
    return json.dumps(response)


def format_data(data):
    response_data = []
    for d in data:
        min_t = float(d["min_temp"])
        max_t = float(d["max_temp"])
        desc = ""
        for row in d["forecast"]["forecast_day"]:
            date_value = row["date"]
            dd = "<p>" + str(date_value)
            f_temp = row["day"]["avgtemp_c"]
            if f_temp < min_t:
                dd += ": Low temperature :" + str(f_temp) + "</p>"
            elif f_temp > max_t:
                dd += ": High temperature :" + str(f_temp) + "</p>"
            else:
                dd += ": Normal temperature :" + str(f_temp) + "</p>"
            desc += dd
        data_dict = {
            'type': 'Feature',
            'properties': {
                'description': desc,
                'icon': 'location'
            },
            'geometry': {
                'type': 'Point',
                'coordinates': [float(d["longitude"]), float(d["latitude"])]
            }
        }
        response_data.append(data_dict)
    response = {"points": response_data}
    return response

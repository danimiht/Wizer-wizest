from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/risk-zones', methods=['GET'])
def get_risk_zones():
    geojson_data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "name": "Район в риск от наводнение",
                    "level": "Червен код",
                    "description": "Повишено внимание за река Дунав в района на Свищов."
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [25.30, 43.60],
                            [25.40, 43.60],
                            [25.40, 43.65],
                            [25.30, 43.65],
                            [25.30, 43.60]
                        ]
                    ]
                }
            }
        ]
    }
    return jsonify(geojson_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
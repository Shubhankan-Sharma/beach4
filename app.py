from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# Sample beach list
beach_list = {
    "beach4": "Cherai Beach",
    # Add more beaches here as needed
}

# Function to generate fresh data
def generate_beach_data(location_name):
    return {
        "location": location_name,
        "data": {
            "timestamp": datetime.now().isoformat(),
            "temperature": random.uniform(20.0, 30.0),
            "currentspeed": random.uniform(0.5, 3.0),
            "ph": round(random.uniform(6.5, 7.5), 2),
            "tidelength": random.uniform(1.0, 2.0),
            "scattering": random.uniform(0.0, 3.0),
            "turbidity": random.uniform(1.0, 7.0)
        }
    }

@app.route('/api/beach/<beach_id>', methods=['GET'])
def get_beach_data(beach_id):
    if beach_id in beach_list:
        beach_name = beach_list[beach_id]
        data = generate_beach_data(beach_name)
        return jsonify(data)
    else:
        return jsonify({"error": "Beach not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

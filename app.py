from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/move_robot', methods=['POST'])
def move_robot():
    data = request.json
    command = data.get('command')
    ros_endpoint = data.get('ros_endpoint')  # Get the dynamic ROS endpoint from the request

    if not command or not ros_endpoint:
        return "Bad request, missing data", 400

    try:
        response = requests.post(ros_endpoint, json=command)
        return response.text, response.status_code
    except requests.exceptions.RequestException as e:
        print("Internal Error")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

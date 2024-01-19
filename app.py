#!/usr/bin/env python
from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/move_robot', methods=['POST'])
def move_robot():
    command = request.json
    # Replace with your ROS server IP and port
    ros_endpoint = "https://i-07cf7ce47bac87c9f.robotigniteacademy.com/5496ab72-2516-4738-a009-317754113163/webpage/"

    try:
        response = requests.post(ros_endpoint, json=command)
        # Return the same status code and text received from ROS server
        return response.text, response.status_code
    except requests.exceptions.RequestException as e:
        # Return a server error message if the ROS server is unreachable
        print("Internal server")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


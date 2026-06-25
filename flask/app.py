from pyexpat import model

from flask import Flask, send_from_directory, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger, swag_from
from openai import OpenAI

import os

app = Flask(__name__, static_folder='static', static_url_path='/static')
swagger = Swagger(app)

@app.route('/analyze')
def index():
    return send_from_directory('static/html', 'log-analyzer.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/api/analyze', methods=['POST'])
def analyze_log():
    """
    Analyze a log file using the OpenAI API.
    ---
    parameters:
      - name: model
        in: query
        type: string
        default: gpt-4.1-mini

      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - logs
          properties:
            logs:
              type: string
              example: "Connection refused"

    responses:
      200:
        description: Successfully analyzed logs
    """

    model = request.args.get('model', 'gpt-4.1-mini')

    data = request.get_json(silent=True) or {}
    logs = data.get("logs", "What is linux?")

    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    response = client.responses.create(
        model=model,
        input=logs
    )

    return jsonify({
        "result": response.output_text
    })
  
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=7777, debug=True)

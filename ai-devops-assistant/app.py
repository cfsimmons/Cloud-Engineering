from flask import Flask, send_from_directory, jsonify, request
from flasgger import Swagger
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
            prompt_type:
              type: string
              enum:
                - "Connection refused"
                - "File not found"
                - "Permission denied"
              default: "Connection refused"

              logs:
                type: string
                description: The log entries to analyze
                example: "ERROR: Connection refused"

    responses:
      200:
        description: Successfully analyzed logs
    """

    # Get model from query parameters, default to 'gpt-4.1-mini'
    # query parameters are the parameters that are passed in the URL after a question mark
    model = request.args.get('model', 'gpt-4.1-mini')

    data = request.get_json(silent=True) or {}
    prompt_type = data.get("prompt_type", "Connection refused")
    #logs = data.get("logs", "What is linux?")

    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    print(f"Model: {model}")
    print(f"Prompt Type: {prompt_type}")

    response = client.responses.create(
        model=model,
        input=prompt_type
    )

    return jsonify({
        "result": response.output_text
    })

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=7777, debug=True)

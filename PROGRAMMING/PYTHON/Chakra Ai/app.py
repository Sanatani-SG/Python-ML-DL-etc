from flask import Flask, jsonify
import subprocess
import time
import os

app = Flask(__name__)

@app.route('/start-chakra', methods=['GET'])
def start_chakra():
    try:
        subprocess.Popen(["python", "ChakraAI.py"])
        return jsonify({"status": "success", "message": "Chakra AI started!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/get-response', methods=['GET'])
def get_response():
    try:
        if os.path.exists('output.txt'):
            with open('output.txt', 'r', encoding='utf-8') as f:
                text = f.read()
            return jsonify({"response": text})
        else:
            return jsonify({"response": "Waiting for your question..."})
    except Exception as e:
        return jsonify({"response": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

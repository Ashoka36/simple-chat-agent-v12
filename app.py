
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello! I am your simple chat agent. Send a POST request to /chat with a 'message' field to talk to me."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    # This is a simple echo for now, but you can integrate an LLM here
    response_message = f"You said: {user_message}. I'm listening!"
    
    return jsonify({"response": response_message})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

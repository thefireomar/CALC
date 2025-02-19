from flask import Flask, render_template, request, jsonify
import logging
from datetime import datetime

app = Flask(__name__)

# Middleware to log all requests
@app.before_request
def log_request_info():
    app.logger.info(f"Request: {request.method} {request.url} - {datetime.now()}")

# Function to log calculation history
def log_history(num1, num2, operation, result):
    with open("history.txt", "a") as file:
        file.write(f"{datetime.now()}: {num1} {operation} {num2} = {result}\n")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    num1 = float(data['num1'])
    num2 = float(data['num2'])
    operation = data['operation']
    
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
    else:
        result = 'Invalid operation'
    
    # Log the calculation to history
    log_history(num1, num2, operation, result)
    
    return jsonify({'result': result})

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
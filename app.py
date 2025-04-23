from flask import Flask, render_template, jsonify
import subprocess
import os

app = Flask(__name__)

# Define the route to serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route to trigger running the test case
@app.route('/run_test', methods=['POST'])
def run_test():
    try:
        # Run the test script using subprocess
        result = subprocess.run(['python', 'test_runner_ui.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # If the test case ran successfully
        if result.returncode == 0:
            return jsonify({"message": f"Test Passed!\n\n{result.stdout}"}), 200
        else:
            return jsonify({"message": f"Test Failed!\n\n{result.stderr}"}), 500
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

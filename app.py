from flask import Flask, jsonify
import subprocess
import os

app = Flask(__name__)


@app.route('/run/<test_case>', methods=['POST'])
def run_test(test_case):
    try:
        result = run_playwright_test(test_case)
        return jsonify({"message": result}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def run_playwright_test(test_case):
    # Path to your pytest test folder and specific test cases
    test_script = f"tests/{test_case}.py"

    # Run the pytest command for the specific test case
    result = subprocess.run(['pytest', test_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode == 0:
        return f"Test {test_case} passed!"
    else:
        return f"Test {test_case} failed: {result.stderr}"


if __name__ == "__main__":
    app.run(debug=True)

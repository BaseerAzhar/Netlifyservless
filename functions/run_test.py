import subprocess
import json


def handler(event, context):
    # Extract test case name from URL path parameter
    test_case = event['pathParameters']['test_case']

    try:
        result = run_playwright_test(test_case)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': result})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }


def run_playwright_test(test_case):
    # Path to your pytest test folder and specific test cases
    test_script = f"tests/{test_case}.py"

    # Run the pytest command for the specific test case
    result = subprocess.run(['pytest', test_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode == 0:
        return f"Test {test_case} passed!"
    else:
        return f"Test {test_case} failed: {result.stderr}"

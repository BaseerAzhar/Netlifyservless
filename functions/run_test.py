import subprocess
import json


def handler(event, context):
    try:
        # Run the test script using subprocess
        result = subprocess.run(['python3', 'test_runner_ui.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True)

        # If the test case ran successfully
        if result.returncode == 0:
            return {
                'statusCode': 200,
                'body': json.dumps({'message': f"Test Passed!\n\n{result.stdout}"})
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': f"Test Failed!\n\n{result.stderr}"})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f"An error occurred: {str(e)}"})
        }

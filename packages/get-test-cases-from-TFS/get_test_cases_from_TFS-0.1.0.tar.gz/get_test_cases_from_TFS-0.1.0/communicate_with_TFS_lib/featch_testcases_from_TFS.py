import base64
import json
import os
import requests


def featch_testcases_from_TFS():
    # Load user data from config file
    main_workspace = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(main_workspace, '../../config.json')
    with open(config_file, 'r') as f:
        config = json.load(f)

    # Personal access token
    personal_access_token = config["personal_access_token"]

    # Base64 encode the personal access token
    token_bytes = f":{personal_access_token}".encode('ascii')
    encoded_token = base64.b64encode(token_bytes).decode('ascii')

    # TFS API endpoint for test cases
    url = f'https://projects.integrant.com/TFS/{config["organization"]}/{config["project"]}/_apis/testplan/plans/{config["test_plan_id"]}/suites/{config["test_suite_id"]}/TestCase?'

    # Authenticate with TFS
    headers = {
        'Authorization': f'Basic {encoded_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    return data
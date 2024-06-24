import os


def create_config_from_user_data(Organization: str ="", Project: str ="", TestPlanId: str ="",
                                        TestSuiteId: str ="", personalToken: str =""):
    
    main_workspace = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(main_workspace, '../../config.json')

    personalToken = personalToken.replace("Bearer ", "")
    if personalToken == "":
        raise ValueError("you have to provide the personal access token to be able to communicate with TFS")
    
    with open(config_file, 'w') as file:
            # Write the TestPlanName as the Feature
            file.write("{\n")
            file.write(f"    \"organization\": \"{Organization}\",")
            file.write(f"\n    \"project\": \"{Project}\",")
            file.write(f"\n    \"test_plan_id\": \"{TestPlanId}\",")
            file.write(f"\n    \"test_suite_id\": \"{TestSuiteId}\",")
            file.write(f"\n    \"personal_access_token\": \"{personalToken}\"\n")
            file.write("}\n")

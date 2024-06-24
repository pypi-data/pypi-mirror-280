import os
import xml.etree.ElementTree as ET


from communicate_with_TFS_lib.featch_testcases_from_TFS import featch_testcases_from_TFS


def fetch_test_cases_and_create_xml(xml_file_path):
    # This function fetches test cases from a TFS test plan and creates an XML file with the test case details.

    data = featch_testcases_from_TFS()

    # Create root element for XML
    root = ET.Element('TestCases')

    # Add testPlan name to XML
    test_plan_name_element = ET.SubElement(root, 'TestPlanName')
    test_plan_name_element.text = data["value"][0]["testPlan"]["name"]

    # Extract Test Case Titles and Steps
    for index, item in enumerate(data.get('value', []), start=1):
        test_case_title = item.get('workItem', {}).get('name')
        test_case_element = ET.SubElement(root, f'TestCase{index}')
        title_element = ET.SubElement(test_case_element, 'Title')
        title_element.text = test_case_title
        for field in item.get('workItem', {}).get('workItemFields', []):
            if 'Microsoft.VSTS.TCM.Steps' in field:
                steps_xml = field['Microsoft.VSTS.TCM.Steps']
                steps_tree = ET.fromstring(steps_xml)
                for step in steps_tree.findall('.//step'):
                    description = step.find('.//parameterizedString').text.strip()
                    expected_result = step.find('.//parameterizedString[2]').text.strip()
                    if description:
                        # Removing <P>,</P>,<DIV>,</DIV> tags from step descriptions
                        description = description.replace('<P>', '').replace('</P>', '').replace('<DIV>', '').replace('</DIV>', '').replace('<BR/>','')
                        expected_result = expected_result.replace('<P>', '').replace('</P>', '').replace('<DIV>', '').replace('</DIV>', '').replace('<BR/>', '')
                        step_element = ET.SubElement(test_case_element, 'Steps')
                        step_text_element = ET.SubElement(step_element, 'Step')
                        step_text_element.text = description
                        expected_result_element = ET.SubElement(step_element, 'ExpectedResult')
                        expected_result_element.text = expected_result
                        
    # Ensure the directory exists
    directory = os.path.dirname(xml_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Create XML tree and write to file
    tree = ET.ElementTree(root)
    tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

    print("XML file has been created successfully.")

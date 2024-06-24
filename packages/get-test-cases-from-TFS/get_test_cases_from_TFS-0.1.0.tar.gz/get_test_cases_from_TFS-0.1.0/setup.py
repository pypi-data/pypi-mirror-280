from setuptools import setup, find_packages

setup(
    name='get_test_cases_from_TFS',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[ 'os', 'base64', 'json', 'requests', 'xml'],
    author='Ayman Mansour, Mohanad Hesham',
    author_email='Ayman.Mansour@integrant.com, Mohanad.hesham@integrant.com',
    description='this Lib is to get the TFS testPlan data, and communicate with TFS API to get the test cases from TFS. Then extract the Testcases as XML file.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

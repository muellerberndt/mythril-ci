"""
Ethereum Solidity CI/CD Processor

Checks the Solidity files in repo using Mythril and fails the build
if there are errors in solidity files
"""

from glob import glob
from json import load
from os import getcwd
from os.path import exists
from subprocess import check_output

import re

# Check if configuration file exists and fetch values from it
if(exists('analysisConfig.json')):
    data = load(open('analysisConfig.json'))
    if 'fail_on_warning' in data and isinstance(data['fail_on_warning'], bool):
        fail_on_warning = data['fail_on_warning']
    else:
        fail_on_warning = False
    if 'fail_on_first_error' in data and isinstance(data['fail_on_first_error'], bool):
        fail_on_first_error = data['fail_on_first_error']
    else:
        fail_on_first_error = False
    if 'is_truffle_project' in data and isinstance(data['is_truffle_project'], bool):
        is_truffle_project = data['is_truffle_project']
    else:
        is_truffle_project = False
else: 
    fail_on_warning = False
    fail_on_first_error = False
    is_truffle_project = False

log = open('test-results.log', 'w')
fail_build = False # Specifies if the build has to be failed

# Handling truffle projects
if(is_truffle_project):
    log.write("Processing Truffle Project\n")
    result = check_output(['myth', '--truffle']).decode("utf-8") 
    log.write(result)
    log.write("\nProcessing of Truffle Project Completed")
    if(re.search('Error', result, re.IGNORECASE)):
      log.write("\nFound Error in Solidity Code. Failing Build")
      exit(1)

# Get all Solidity files in the repository
files = glob(getcwd() + '/**/*.sol', recursive=True)

# Process each file individually and check for errors / warnings as set
for file in files:
    log.write("Processing file " + file + "\n")
    result = check_output(['myth', '-x', file]).decode("utf-8") 
    log.write(result)
    log.write("\nProcessing of file " + file + " Completed\n\n")
    if(re.search('Error', result, re.IGNORECASE) or (fail_on_warning and re.search('Warning', result, re.IGNORECASE))):
        if(fail_on_first_error):
            log.write("\n-----Failing Build Since Fail on first error is enabled----\n")
            log.close()
            exit(1)
        else:
            fail_build = True

# If there are errors or warnings (as per the config), Fail the build
if(fail_build):
    log.write("Failing build since Errors / Warnings (if set) are found in the Code")
    log.close()
    exit(1)

log.write("Build passed since no issues were found")
log.close()

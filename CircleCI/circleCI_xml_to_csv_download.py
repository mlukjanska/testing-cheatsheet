# Parse circleci Unit test result XMLs to CSV
# importing the required modules 
import csv
import xml.etree.ElementTree as ET 
import os
from glob import glob
import ntpath
import requests
import sys


# command execution example: python circleCI_xml_to_csv_download.py <circleci_token> <build_number> <repository_name>
# command execution example: python circleCI_xml_to_csv_download.py 22109bf89aada2f0dd94bf41919a0b9970c363be 4326 test_repository

#circleci config
vcsType = 'github' 
username = 'dataswitcher' #organization or username 
project = sys.argv[3]
build_number = sys.argv[2]
token = sys.argv[1]
isToDownload = 1
#print(str(sys.argv))
if len(sys.argv) == 5:
    isToDownload = int(sys.argv[4])

rootPath = '/Users/mlukjanska/Documents/Dataswitcher/CircleCI/builds/'
newBuildFolder = rootPath + 'build_' + build_number

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def downloadArtifacts(): 

    result = 0

    # circleci url to list the urls to artifacts
    # https://circleci.com/docs/2.0/artifacts/#downloading-all-artifacts-for-a-build-on-circleci
    # https://circleci.com/api/v1.1/project/:vcs-type/:username/:project/$build_number/artifacts?circle-token=$CIRCLE_TOKEN
    url = 'https://circleci.com/api/v1.1/project/' + vcsType + '/' + username + '/' + project + '/' + build_number + '/artifacts?circle-token=' + token
    headers = {'Accept': 'application/json'}
    print(url)

    # creating HTTP response object from given url 
    response = requests.get(url, headers=headers) 

    if response.status_code == 200:
        #create folder where to download the files
        if not os.path.exists(newBuildFolder):
            os.makedirs(newBuildFolder)

        #download the xmls
        if response.json(): 
            for item in response.json():
                urlArtifact = item['url'] + '?circle-token=' + token
                responseArtifact = requests.get(urlArtifact)
                with open(newBuildFolder + '/' + str(item['node_index']) + '_' + path_leaf(item['url']), 'wb') as f: 
                    print('Downloading file: ' + str(item['node_index']) + '_' + path_leaf(item['url']))
                    f.write(responseArtifact.content) 
            result = 1
    else:
        print('Failed to connect to circleCI API, status code: ' + str(response.status_code))

    return result

def parseXMLTestResults(xmlfile): 

    # create element tree object 
    tree = ET.parse(xmlfile) 

    # get root element 
    root = tree.getroot() 

    # create empty list for testcases items 
    testResults = [] 

    # iterate through testsuites
    for testsuite in root:
        # iterate child elements of testsuite --> testcases 
        for testcase in testsuite: 
            # empty testcases dictionary 
            print(xmlfile)
            #print('testcase: ' + str(testcase))
            testcaseitem = {}
            testcaseitem['resultsFilename'] = xmlfile 
            testcaseitem['name'] = testcase.attrib['name'] 
            testcaseitem['class'] = testcase.attrib['class'] 
            testcaseitem['time'] = float(testcase.attrib['time'])
            testcaseitem['assertions'] = int(testcase.attrib['assertions'])
            testcaseitem['file'] = testcase.attrib['file'] 
            testcaseitem['failureType'] = ''
            testcaseitem['failureDetails'] = ''

            #failures are child items of testcase
            #there can be also system-out
            for child in testcase:
                if child.tag == 'failure':
                    testcaseitem['failureType'] = child.attrib['type'] 
                    testcaseitem['failureDetails'] = child.text
                    #print('testcaseitem[failureType]: ' + str(testcaseitem['failureType']))
                if child.tag == 'error':
                    testcaseitem['failureType'] = child.attrib['type'] 
                    testcaseitem['failureDetails'] = child.text
                    #print('testcaseitem[failureType]: ' + str(testcaseitem['failureType']))

            # append testResults dictionary with testcase item
            testResults.append(testcaseitem)

    # return testresults
    return testResults 

def summarizeTestResults(testResultsDetailed): 

    # create empty list for testcases items 
    testResultsSummary = [] 

    # iterate child elements of item 
    for testResult in testResultsDetailed: 
        #print(testResult)
        # empty testResultItem
        testResultItem = {}
        testCaseNotAdded = 1

        testResultItem['resultsFilename'] = testResult['resultsFilename']
        testResultItem['failureType'] = ''
        testResultItem['testCaseCount'] = 1

        if len(testResult['failureType']) > 0:
            testResultItem['failureType'] = testResult['failureType']

        if testResultsSummary:
            #print(testResultsSummary)
            for tc in testResultsSummary:
                if tc and tc['class'] == testResult['class']:
                    tc['time'] += float(testResult['time'])
                    tc['timeMin'] += float(testResult['time'])/60
                    tc['assertions'] += int(testResult['assertions'])
                    tc['testCaseCount'] += 1 
                    #print(tc['class'] + ' ' + str(tc['time']))
                    #print('tc: ' + str(tc))
                    if len(testResult['failureType']) > 0:
                        tc['failureType'] = testResult['failureType']
                    testCaseNotAdded = 0
            if testCaseNotAdded:
                testResultItem['class'] = testResult['class'] 
                testResultItem['file'] = testResult['file'] 
                testResultItem['time'] = float(testResult['time'])
                testResultItem['timeMin'] = float(testResult['time'])/60
                testResultItem['assertions'] = int(testResult['assertions'])
                #print('testResultItem if not added: ' + str(testResultItem))
                testResultsSummary.append(testResultItem)
        else:
            testResultItem['class'] = testResult['class'] 
            testResultItem['file'] = testResult['file'] 
            testResultItem['time'] = float(testResult['time'])
            testResultItem['timeMin'] = float(testResult['time'])/60
            testResultItem['assertions'] = int(testResult['assertions'])
            #print('testResultItem first: ' + str(testResultItem))
            testResultsSummary.append(testResultItem)

    #round the final timings to 2 decimals
    for testResult in testResultsSummary:
        testResult['time'] = round(testResult['time'],2)
        testResult['timeMin'] = round(testResult['timeMin'],2)
    #print(testResultsSummary)
    return testResultsSummary 

def savetoCSV(testResults, filename, fields): 

    # writing to csv file 
    with open(filename, 'w') as csvfile: 

        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 

        # writing headers (field names) 
        writer.writeheader() 

        # writing data rows 
        writer.writerows(testResults) 

    
def main(): 
    isDownloaded = 0
    
    # load rss from web to update existing xml file 
    if isToDownload:
        isDownloaded = downloadArtifacts()
    else:
        isDownloaded = 1
    #print(isDownloaded)
    
    if isDownloaded:
        xmlTestResultFiles = glob(newBuildFolder + '/' + '*.xml')
        #print(xmlTestResultFiles)
        testResults = []
        for xmlTestResultFile in xmlTestResultFiles:
            testResults += parseXMLTestResults(xmlTestResultFile)
        
        print('Saving test results details: _testResults.csv')
        savetoCSV(testResults, newBuildFolder + '/' + '_testResults.csv', ['resultsFilename', 'name', 'class', 'time', 'assertions', 'file', 'failureType', 'failureDetails']) 

        testResultsSummary = summarizeTestResults(testResults)
        print('Saving test results details: _testResultsSummary.csv')
        savetoCSV(testResultsSummary, newBuildFolder + '/' + '_testResultsSummary.csv', ['resultsFilename', 'class', 'time', 'timeMin', 'assertions', 'testCaseCount', 'file', 'failureType']) 
    
    else:
        print('There was error downloading from circleCI')    
    
if __name__ == "__main__": 

    # calling main function 
    main() 

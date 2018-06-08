#coding=utf-8

import os
import commands
import subprocess

import requests

from pyxml2dict import XML2Dict

def command(cmd):
    # result = os.system(cmd)
    # if result == 0:
    #     return True
    # else:
    #     return False
    # status, output = commands.getstatusoutput(cmd)
    # return status, output
    process = subprocess.Popen(cmd)
    process.wait()
    return process.returncode#, process.communicate()

def run_cases(path):
    file = os.path.join(path, "test.xml")
    cmd = "nosetests --where={0} \
    --with-coverage --cover-erase \
    --cover-branches --cover-xml \
    --cover-xml-file={1}".format(path, file)
    return file

def parse_report(name):
    file = open(name)
    xml = file.read()
    file.close()
    data = XML2Dict().fromstring(xml)
    result = {
        "branch": {
            "cover": data['coverage']['@branches-covered'],
            "valid": data['coverage']['@branches-valid'],
            "rate": data['coverage']['@branch-rate'],
        },
        "line": {
            "cover": data['coverage']['@lines-covered'],
            "valid": data['coverage']['@lines-valid'],
            "rate": data['coverage']['@line-rate'],
        }
    }
    return result

def push_report(data):
    url = "http://127.0.0.1:9999/api/v1/insert"
    data.setdefault('collection', 'coverage')
    response = requests.post(url, json=data)
    print response.status_code
    print response.json()

if __name__ == '__main__':
    path = "C:/Users/40556/PycharmProjects/lesson07/unit"
    file = run_cases(path)
    data = parse_report(file)
    push_report(data)
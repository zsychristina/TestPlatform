#coding=utf-8

import time

from selenium import webdriver

commands = [
    {
        'command': 'browser',
        'parameters': {
            'url': 'http://ask.testfan.cn/',
        }
    },
    {
        'command': 'find',
        'parameters': {
            'by': 'css selector',
            'value':  'body > div.wrap > div.jumbotron.text-center > h4 > a.btn.btn-default.ml-5',
        }
    },
    {
        'command': 'action',
        'parameters': {
            'action': 'click',
            'sleep': 3
        }
    },
    {
        'command': 'find',
        'parameters': {
            'by': 'name',
            'value':  'email',
        }
    },
    {
        'command': 'keys',
        'parameters': {
            'value':  '3317434061@qq.com',
        }
    },
    {
        'command': 'find',
        'parameters': {
            'by': 'name',
            'value':  'password',
        }
    },
    {
        'command': 'keys',
        'parameters': {
            'value':  'damao@testfan',
        }
    },
    {
        'command': 'find',
        'parameters': {
            'by': 'xpath',
            'value':  '/html/body/div/div[2]/form/div[3]/button',
        }
    },
    {
        'command': 'action',
        'parameters': {
            'action': 'click',
            'sleep': 3
        }
    },
]

class Function(object):

    def __init__(self, commands):
        self.commands = commands
        self.driver = webdriver.Chrome(executable_path='C:\Python27\chromedriver.exe')

    def browser(self, params):
        url = params.get('url', "http://www.baidu.com")
        self.driver.get(url)

    def find(self, params):
        by = params.get('by')
        selector = params.get('value')
        return self.driver.find_element(by, selector)

    def keys(self, result, params):
        text = params.get('value')
        result.send_keys(text)

    def action(self, result, params):
        cmd = params.get('action')
        if cmd == 'click':
            result.click()

    def run(self):
        result = None
        for command in self.commands:
            cmd = command['command']
            params = command['parameters']
            if result is None:
                result = getattr(self, cmd)(params)
            else:
                result = getattr(self, cmd)(result, params)

if __name__ == '__main__':
    func = Function(commands)
    func.run()
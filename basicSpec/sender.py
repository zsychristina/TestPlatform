#coding=utf-8

import pika

class Sender(object):

    def __init__(self):
        pass

    def send(self,message):
        self.channel.basic
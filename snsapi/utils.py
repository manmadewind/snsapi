# -*- coding: utf-8 -*-

#TODO:
#    This json import piece appears too frequently
#    We'd better make this file the real entrance. 
#    All other files refer to json from utils.py.
try:
    import json
except ImportError:
    import simplejson as json

from snsconf import SNSConf

'''
utilities for snsapi
'''

class JsonObject(dict):
    '''
    general json object that can bind any fields but also act as a dict.
    '''
    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value

class JsonDict(JsonObject):
    """
    The wrapper class for Python dict. 

    It is intended to host Json compatible objects. 
    In the interative CLI, the users are expected 
    to configure SNSAPI during execution. To present
    the current config in a nice way. We should add
    indentation for the dump method.
    """
    def __init__(self, jsonconf = None):
        super(JsonDict, self).__init__()
        if jsonconf:
            self.update(jsonconf)

    def __str__(self):
        return self._dumps_pretty()

    def _dumps(self):
        return json.dumps(self)

    def _dumps_pretty(self):
        return json.dumps(self, indent=2)

    def get(self, attr):
        return dict.get(self, attr, "(nu)")

        
def console_input(string = None):
    '''
    To make oauth2 testable, and more reusable, we use console_input to wrap raw_input.
    See http://stackoverflow.com/questions/2617057/supply-inputs-to-python-unittests.
    '''
    if string is None:
        return raw_input().decode(SNSConf.SNSAPI_CONSOLE_STDIN_ENCODING)
    else:
        return string.decode(SNSConf.SNSAPI_CONSOLE_STDIN_ENCODING)

def console_output(string):
    '''
    The sister function of console_input()!

    Actually it has a much longer story. See Issue#8: 
    the discussion of console encoding~
    '''
    print string.encode(SNSConf.SNSAPI_CONSOLE_STDOUT_ENCODING)


#!/usr/bin/env python
#coding:utf-8
#__author__:Bing
import urllib2,requests
from scan_engine.model.exploit import CTExploit

class Catteam(CTExploit):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.info = {
            "name": "Flash test",
            "author": 'wudizixuan',
            "ref": "http://catteam.com/688",
            "type": self.type.misconfiguration,
            "severity": self.severity.high,
            "privileged": False,
            "create_date": "2016-08-04",
        }

        self.register_option({
            "url": {
                "default": "",
                "required": True,
                "choices": [],
                "convert": self.convert.url_field,
                "desc": "target url"
            }
        })

        self.register_result({
            "status": False,
            "data": {
                "verify_info": {
                    "url": "111",
                }
            },
            "description": "",
            "error": ""
        })
		
        self.repair = {
            "info":"this is reqaired in lastest version!",
		}
		
		
		
    def verify(self):
		print self.option.url
		print "###this is flash scripts##"
		self.result.status = True



#!/usr/bin/env python
#coding:utf-8
#__author__:Bing
import urllib2,requests
from scan_engine.model.exploit import CTExploit
from socket import *

class Catteam(CTExploit):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.info = {
            "name": "Port scan",
            "author": 'Bing',
            "ref": "http://catteam.com/test",
            "type": self.type.info_leak,
            "severity": self.severity.medium,
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
            "data": [],
            "description": "",
            "error": "",
        })
		
        self.post_list = [21,22,23,25,53,80,81,123,161,389,443,445,873,1099,1433,1521,1723,2000,2181,2049,2601,3306,3689,3389,4440,4848,4899,5432,5800,5900,5901,6379,7001,7788,8000,8012,8161,8080,8443,8500,8649,8880,9000,9080,9200,9880,22345,27017,11211,50070]
		
        self.repair = {"info":"close not important port!"}
		

    def verify(self):
		host = self.option.url
		port = self.post_list
		#print host,port
		def test(port):
			try:
				s=socket(AF_INET,SOCK_STREAM)
				s.settimeout(2)
				s.connect((host,int(port)))
				s.close()
				self.result.data.append(int(port))
			except:
				#self.result.data.error(int(port))
				pass
		self.thread(test,self.post_list,10)
		self.result.status = True




#!/usr/bin/env python
#coding:utf-8
#__author__:Bing
import imp,os
import sys,re
	
class Catteam(object):
    result = {
        'vul_info': {},
        'vul_result': {},
		'vul_repair': {},
    }

    def import_poc(self, path):
        poc = imp.load_source('Catteam', path)
        poc = poc.Catteam()
        return poc


    def run(self, target, path):
		try:
			poc = self.import_poc(path)
			poc.option.url = target
			#print poc.option.url+'$$$$'
			poc.verify()
			if poc.result.status == True:
				self.result['vul_info'] = poc.info
				self.result['vul_result'] = poc.result.data
				self.result['vul_repair'] = poc.repair
				#print self.result['vul_info'],self.result['vul_result'],self.result['vul_repair'],'~~~~'
				return self.result
			else:
				return {}
		except Exception,e:
			print e
			return

#!/usr/bin/env python
#coding:utf-8
#author:Bing
import requests as req
from scan_engine.frame.catteam import Catteam

class Poc_Launcher(object):

	def poc_verify(self, target, poc_file):
		save_result_api_addr = 'http://127.0.0.1/test/test.php'#SAVE_RESULT_API
		result = Catteam().run(target, poc_file)
		print target,result,'####'
		if result:
			post = {
				'target': target,
				'poc_file': poc_file.split('/')[-1],
				'result_info': result['vul_info'],
				'result_result': result['vul_result'],
				'result_repair': result['vul_repair'],
				}
			#req.post(url=save_result_api_addr, data=post)
			result = str(result)
			#print post,"^^^^"
		return result


			


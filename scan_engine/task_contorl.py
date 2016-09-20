#!/usr/bin/env python
#coding:utf-8
#author:Bing

import multiprocessing
import math,os
from scan_engine.config import url_seg,get_poc_files,get_basic_files
from scan_engine.tasks import run_task_in_gevent

#this is baisc
class Task_basic_control(object):
    process_num = 5
    def assign_task_in_multiprocessing(self, url_list, poc_file_dict):
        for url_each_process in url_list:
            multiprocessing.Process(target=run_task_in_gevent, args=(url_each_process, poc_file_dict )).start()
            
    def launch(self, target, poc_name, task_name):
        #self.set_task_status(target, task_name, status=True)
        url_list = url_seg(target, self.process_num)
        poc_file_dict = get_basic_files(poc_name)
        self.assign_task_in_multiprocessing(url_list, poc_file_dict)


#this is other poc
class Task_control(object):
    process_num = 5
    def assign_task_in_multiprocessing(self, url_list, poc_file_dict):
        for url_each_process in url_list:
            multiprocessing.Process(target=run_task_in_gevent, args=(url_each_process, poc_file_dict )).start()
            
    def launch(self, target, poc_name, task_name):
        #self.set_task_status(target, task_name, status=True)
        url_list = url_seg(target, self.process_num)
        poc_file_dict = get_poc_files(poc_name)
        self.assign_task_in_multiprocessing(url_list, poc_file_dict)




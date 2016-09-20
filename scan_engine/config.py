#!/usr/bin/env python
#coding:utf-8
#author:Bing
import sys,os,re,math,gevent
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BASIC_DIR = BASE_DIR+'/basic'
POCS_DIR = BASE_DIR+'/pocs'
PLUGINS_DIR = BASE_DIR+'/plugins/'

def fix_target(domain, https=False):
    if not domain:
        return
    elif domain.startswith(('http://', 'https://')):
        return domain
    if not https:
        domain = 'http://' + domain
    else:
        domain = 'https://' + domain
    return domain
    

 
def url_seg(url_list, process_num):
    # [1,2,3,4,5,6,7,8,9] to [[1, 2, 3, 4], [5, 6, 7, 8], [9]]
    n = int(math.ceil(len(url_list) / float(process_num)))
    return [url_list[i:i + n] for i in range(0, len(url_list), n)]

    
#ÎÄ¼þÄ£ºýËÑË÷
def fuzzyfinder(user_input, pocs_path):
        suggestions = []
        files = os.listdir(pocs_path)
        pattern = '.*?'+user_input+'.*?\.py$'    # Converts 'djm' to 'd.*?j.*?m¡®
        regex = re.compile(pattern)         # Compiles a regex.
        for item in files:
            match = regex.search(item)      # Checks if the current item matches the regex.
            if match and item != '__init__.py':
                suggestions.append((len(match.group()), match.start(), pocs_path+'/'+item))
        return [x for _, _, x in sorted(suggestions)]

def get_poc_files(user_search):
    poc = {}
    pocs_path = POCS_DIR
    poc = fuzzyfinder(user_search, pocs_path)
    #poc.setdefault('Catteam', poc_files)
    return poc

def get_basic_files(user_search):
    poc = {}
    pocs_path = BASIC_DIR
    poc = fuzzyfinder(user_search, pocs_path)
    #poc.setdefault('Catteam', poc_files)
    return poc
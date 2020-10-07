#!/bin/python3

import codecs
import re 
import os

def read_source(path):
    work_dir=re.search(r'(.*?)\/',path).group()
    file_content = codecs.open(path, "r", "utf-8").read()
    return file_content,work_dir

def remove_string_contents(str):
    return re.sub(r'([\"\'])(?:(?=(\\?))\2.)*?\1','',str)

def get_custom_imported_files(path):
    file_content,work_dir=read_source(path)
    file_content=remove_string_contents(file_content)
    libs = re.findall(r'.*from (.*?)[ .*|.*\n|.*\r]', file_content) + re.findall(r'.*import (.*?)[ .*|.*\n|.*\r]', file_content)
    ext_files=[]
    for lib in libs:
        filename=lib+".py"
        filepath=work_dir+filename
        if os.path.exists(filepath):
            ext_files.append(filepath)
    return ext_files

def _get_custom_imported_files_recursively(ext_files):
    if len(ext_files)==0:
        return ext_files
    else:
        new_ext_files=[]
        for ext_file in ext_files:
            new_ext_files.extend(_get_custom_imported_files_recursively(get_custom_imported_files(ext_file)))
        return ext_files+new_ext_files

def get_custom_imported_files_recursively(ext_file):
    return [ext_file]+_get_custom_imported_files_recursively(get_custom_imported_files(ext_file))

def replace_last(str,a,b):
    return str[::-1].replace(a,b,1)[::-1]

def replace_first(str,a,b):
    return str.replace(a,b,1)

def pre_compile(content):
    parsed_lines=""
    lines = content.split('\n')
    needed_tabs=0
    for line in lines:
        line=line.strip()
        if re.match(r'^.*}(?=(?:[^\"\']*\"\'[^\"\']*\"\')*[^\"\']*\Z)', line): 
            line=replace_last(line,'}','')
            needed_tabs-=1
        if (needed_tabs>0):
            line="\t"*needed_tabs+line
        if re.match(r'^.*({)\s*$', line):
            line=replace_last(line,'{',':')
            needed_tabs+=1
        parsed_lines+=line+'\n'
    return parsed_lines            

# file_content,work_dir=read_source('examples/basic.py')
# print(get_custom_imported_files_recursively('examples/basic.py'))
print(pre_compile(read_source('examples/basic.py')[0]))


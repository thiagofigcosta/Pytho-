#!/bin/python3

import math
import sys
import basic_external_file as ext

print('This is Pytho{\}')
print('')
print('Running over Python {}.{}.{}'.format(sys.version_info[0],sys.version_info[1],sys.version_info[2]))
print('Several  tabs            here')
print('Is 13 greater than 14?')

if 13 > 14{
    print('Unfortunately not')
}else {
    print('NEVER')
}
print('')
print('10 reasons why you should use Pytho{\}')
for i in range(10){
print ("{} Because I rate : and tab".format(i)) # no ident here
}

ext.print_ext_file()
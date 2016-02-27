#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
length, number = 15, 200

def rand_code():
	r_code = ''
	for i in range(length):
		r_code = r_code + chr(random.randint(65,90))
	return r_code

act_code = set()
cnt = 0
fout = open('activation_code.txt', 'w')
while cnt < number:
	new_code = rand_code()
	if new_code not in act_code:
		act_code.add(new_code)
		cnt = cnt+1
		#print(new_code)
		fout.write(new_code+'\n')
fout.close()
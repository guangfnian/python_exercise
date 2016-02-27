#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open(input('Please drag the file here...\n'), 'r') as fout:
	article = fout.read()
	words = set()
	cnt = dict()
	word = ''
	for cha in article:
		if cha == ' ':
			if word not in words:
				words.add(word)
				cnt[word] = 0
			cnt[word] = cnt[word] + 1
			word = ''
		else:
			word = word + cha
	for key, value in cnt.items():
		print(key, ':', value)
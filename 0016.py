#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import xlwt3 as xlwt
with open(input('Please drag the file here...\n'), 'r') as fin:
	date = json.loads(fin.read())
	wb = xlwt.Workbook()
	sheet = wb.add_sheet('numbers')
	for i in range(len(date)):
		for j in range(len(date[i])):
			sheet.write(i, j, date[i][j])
	wb.save('numbers.xls')

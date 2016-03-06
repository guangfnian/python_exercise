#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import xlwt3 as xlwt
with open(input('Please drag the file here...\n'), 'r') as fin:
	date = json.loads(fin.read())
	wb = xlwt.Workbook()
	sheet = wb.add_sheet('student')
	for i in range(len(date.keys())):
		row, col = i, 0
		sheet.write(row, col, i+1)
		for j in date[str(i+1)]:
			col += 1
			sheet.write(row, col, j)
	wb.save('student.xls')

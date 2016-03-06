#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import xlwt3 as xlwt
with open(input('Please drag the file here...\n'), 'r') as fin:
	date = json.loads(fin.read())
	wb = xlwt.Workbook()
	sheet = wb.add_sheet('city')
	for i in range(len(date.keys())):
		sheet.write(i, 0, i+1)
		sheet.write(i, 1, date[str(i+1)])
	wb.save('city.xls')

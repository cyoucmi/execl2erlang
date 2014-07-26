#created by chengcheng<cyoucmi@gmail>
#date:2014/7/16

import os
import xlrd
import re
import time
import codecs
import sys

useless_row_num = 10

def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        return -1
##return list
def excel_table_byindex(file= 'role.xlsx',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows 
    ncols = table.ncols 
    list =[]
    for rownum in range(nrows):

         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(ncols):
                app[i] = get_cell_value1(table.cell(rownum, i))
             list.append(app)
    return list
		
def get_cell_value1(cell):
	celltype = cell.ctype
	cellvalue = cell.value
	if celltype == xlrd.XL_CELL_NUMBER and cellvalue == int(cellvalue): 
		return str(int(cellvalue))
	else:
		return str(cellvalue)
	
def do_write_file(file_name, path, tables):
	base_name = os.path.basename(file_name)
	base_name1 = os.path.splitext(base_name)[0]
	erlname = path + "/cfg_" + base_name1 + ".erl"
	fd = codecs.open(erlname, 'w', 'utf-8')
	file_buffer = '%%% this code is auto generate by tool, do not modify by hand\n'
#	time_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#	file_buffer += '%% Data:'
#	file_buffer += "%s\n"%(time_str)
	file_buffer += '-module(cfg_%s).\n' % base_name1
	file_buffer += '-export([find/1]).\n'
	fd.write(file_buffer)
	first_list = tables.pop(0)
	list_len = len(first_list)
	for i in range(useless_row_num-1):
		tables.pop(0)
	for R in tables:
		file_buffer = ""
		for j in range(list_len):
			file_buffer += "%s%s"%(first_list[j], R[j])
		file_buffer += '\n'
		fd.write(file_buffer)
	file_buffer='find(_)->[].\n'
	fd.write(file_buffer)
	fd.flush()
	fd.close()	
	
#param1: source excel file 
#param2: write path
def main(argv):
	tables = excel_table_byindex(argv[0])
	do_write_file(argv[0], argv[1], tables)
	
if __name__=="__main__":
	main(sys.argv[1:])
	






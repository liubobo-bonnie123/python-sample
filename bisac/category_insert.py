#!/usr/bin/env python
# encoding: utf-8
"""
category_insert.py

Created by Bo Liu on 2011-03-31.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
import sys
import os
import pdb
import simpledb

# select code, category,sub1,sub2 from bisac where sub2<>'General';
# def insert_bisac(info):
#     dbconn = simpledb.SimpledbClass("pgsql", "localhost", "dev", "", "dev")
#     bisac=info.split('\t')[1].strip('\n')
#     isbn=info.split('\t')[0].zfill(7)
#     # pdb.set_trace()
    # qry = '''UPDATE raw_bookmetadata SET bisac = \'%s\' where isbn = \'%s\'''' % (bisac, isbn)
    # pdb.set_trace()
    # dbconn.ChangeQuery(qry)
#     dbconn.Commit()
#     print info.split('\t')[0], 'is done'
#     
# def select_bisac():
#     dbconn = simpledb.SimpledbClass("pgsql", "localhost", "dev", "", "dev")
#     qry = '''SELECT code, category, sub1, sub2 FROM bisac where sub2= \'%s\'''' % ('General')
#     # select code, category,sub1,sub2 from bisac where sub2='General';
#   
#     
#     pdb.set_trace()
#     dbconn.ChangeQuery(qry)
#     
#     dbconn.Commit()
#     
# if __name__ == '__main__':
#     info_list = open(sys.argv[1]).readlines()
#     
#     for info in info_list:
#         insert_bisac(info)
    



# qry3='''DELETE FROM categories WHERE category_display_name=\'%s\''''%('Sports Cards')
# dbconn.ChangeQuery(qry3)
# dbconn.Commit()



dbconn = simpledb.SimpledbClass("pgsql", "localhost", "dev", "", "dev")
qry = '''SELECT code, sub1 FROM bisac where sub2= \'%s\'''' % ('General')
code_sub1_tuple_list=dbconn.SelectQuery(qry)
# print dbconn.SelectQuery(qry)
for tuples in code_sub1_tuple_list:
    # pdb.set_trace()
    code=tuples[0]
    sub1=tuples[1]
    # pdb.set_trace()
    qry1 = '''INSERT INTO categories (category_code, category_display_name ) VALUES (\'''%s\''',\'''%s\''')''' % (code, sub1)
    print qry1

    # pdb.set_trace()
    dbconn.ChangeQuery(qry1)
    # dbconn.Commit()
qry2 = '''SELECT * FROM categories ''' 
print dbconn.SelectQuery(qry2)

    # pdb.set_trace()


    

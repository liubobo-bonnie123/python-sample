#!/usr/bin/env python
# encoding: utf-8
"""
insert_metadata.py

Created by Yuqing Dai on 2011-03-17.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import pdb
import simpledb

def insert_metadata(info):
    dbconn = simpledb.SimpledbClass("pgsql", "ix1.smint.us", "django", "", "product_server")
    isbn = info.split('\t')[0].zfill(7)
    title = info.split('\t')[2].strip().replace('\'', r'\'')
    author = info.split('\t')[1].replace('\'', r'\'')
    qry = '''UPDATE raw_bookmetadata SET contributors = \'%s\' where isbn = \'%s\'''' % (author, isbn)
    dbconn.ChangeQuery(qry)
    # general information about this book
    # qry = '''INSERT INTO raw_bookmetadata (title, isbn, imprint) VALUES (\'%s\', \'%s\', \'%s\')''' % (title, isbn, 'Gutenberg')
    # try:
    #     dbconn.ChangeQuery(qry)
    # except:
    #     print info.split('\t')[0], 'is too long'
    #     return
    # 
    # # price information about this book
    # qry_USD = '''INSERT INTO raw_bookprice (amount, currency, bookmetadata_id) VALUES (0, 'USD', \'%s\')''' % isbn #USD
    # qry_CAD = '''INSERT INTO raw_bookprice (amount, currency, bookmetadata_id) VALUES (0, 'CAD', \'%s\')''' % isbn #CAD
    # dbconn.ChangeQuery(qry_USD)
    # dbconn.ChangeQuery(qry_CAD)
    dbconn.Commit()
    print info.split('\t')[0], 'is done'
    
if __name__ == '__main__':
    info_list = open(sys.argv[1]).readlines()
    for info in info_list:
        insert_metadata(info)


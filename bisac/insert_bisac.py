
import sys
import os
import pdb
import simpledb

def insert_bisac(info):
    dbconn = simpledb.SimpledbClass("pgsql", "localhost", "django", "", "product_server")
    bisac=info.split('\t')[1].strip('\n')
    isbn=info.split('\t')[0].zfill(7)
    pdb.set_trace()
    qry = '''UPDATE raw_bookmetadata SET bisac = \'%s\' where isbn = \'%s\'''' % (bisac, isbn)
    pdb.set_trace()
    dbconn.ChangeQuery(qry)
    dbconn.Commit()
    print info.split('\t')[0], 'is done'
    
if __name__ == '__main__':
    info_list = open(sys.argv[1]).readlines()
    
    for info in info_list:
        insert_bisac(info)
    


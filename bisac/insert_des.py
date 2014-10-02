
import sys
import os
import pdb
import simpledb

def insert_bisac(info, dbconn):
    try:
        description=info.split('\t')[1].strip('\n').decode('utf_8').replace('\'', '')
        isbn=info.split('\t')[0].split('_')[1]
        qry = '''UPDATE raw_bookmetadata SET description = \'%s\' where isbn = \'%s\'''' % (description, isbn)
        try:
            dbconn.ChangeQuery(qry)
        except:
            pass
        print info.split('\t')[0], 'is done'
    except:
        log = open('./bad_textcode.txt', 'a')
        log.write(info)
        log.close()
    
if __name__ == '__main__':
    info_list = open(sys.argv[1]).readlines()
    dbconn = simpledb.SimpledbClass("pgsql", "localhost", "django", "", "product_server")
    for info in info_list:
        insert_bisac(info, dbconn)

    dbconn.Commit()
    
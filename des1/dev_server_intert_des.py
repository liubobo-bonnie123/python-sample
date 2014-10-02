
import sys
import os
import pdb
import simpledb

def insert_des(info, dbconn):
    try:
        des=info.split(' ')[1].strip('\n').encode('utf_8').replace('\'', '&#8217').replace('\"', '&#8220').replace('\"', '&#8221')
        # isbn=info.split('\t')[0].split('_')[1]
        # description.decode('utf_8').replace('\'', '&#8217').replace('\"', '&#8220').replace('\"', '&#8221')
        title = info.split(' ')[0]
        qry = '''INSERT INTO description(title, des) VALUES (\'%s\',\'%s\')''' % (title, des)
        try:
            dbconn.ChangeQuery(qry)
        except:
            pass
        print title, 'is done'
    except:
        log = open('./bad_textcode.txt', 'a')
        log.write(info)
        log.close()
    
if __name__ == '__main__':
    info_list = open(sys.argv[1]).readlines()
    dbconn = simpledb.SimpledbClass("pgsql", "localhost", "dev", "", "dev")
    for info in info_list:
        insert_des(info, dbconn)

    dbconn.Commit()

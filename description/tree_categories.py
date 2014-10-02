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


def create_category_tree(category_tree_child, category_tree_parent,dbconn):
    qry6 = '''SELECT category_tree_child, category_tree_parent from category_tree where category_tree_child = \'%s\'''' % (category_tree_child)
    print qry6
    judge=dbconn.SelectQuery(qry6)
    if judge ==[]:
        qry5 = '''INSERT INTO category_tree (category_tree_child, category_tree_parent)  VALUES (\'%s\',\'%s\')''' % (category_tree_child, category_tree_parent)
        print qry5
        dbconn.ChangeQuery(qry5)
    else:
        pdb.set_trace()
        # pdb.set_trace()
    # dbconn.Commit()
    # pdb.set_trace()
    # qry6 = '''SELECT * FROM category_tree ''' 
    # print dbconn.SelectQuery(qry6)
    
# def insert_sub3(dbconn):
#     qry = '''SELECT code,sub1,sub2,sub3 FROM bisac where trim(sub3) is not null and trim(sub3) <> \'%s\'''' % ('General')
#     code_sub1_tuple_list=dbconn.SelectQuery(qry)
#     for tuples in code_sub1_tuple_list:
#         rep2=tuples[2].replace("\'", "\\'")
#         rep1=tuples[1].replace("\'", "\\'")
#         rep3=tuples[3].replace("\'", "\\'")
#         try:
#             qry1 = '''INSERT INTO categories (category_code, category_display_name ) VALUES (\'%s\',\'%s\') RETURNING category_id, category_code, category_display_name ''' % (tuples[0], rep3)
#             print qry1
#             # pdb.set_trace()
#             dbconn.ChangeQuery(qry1)
#             # dbconn.Commit()
#             qry3 = '''SELECT category_id FROM categories where trim(category_code) = \'%s\'''' % (tuples[0])# sub
#             category_tree_child=dbconn.SelectQuery(qry3)[0][0]
#             print dbconn.SelectQuery(qry3)
#             qry5 = '''SELECT category FROM bisac where trim(code) = \'%s\'''' % (tuples[0])# category
#             category_value=dbconn.SelectQuery(qry5)[0][0]
#             qry4 = '''SELECT code FROM bisac where trim(sub1) = \'%s\' and trim(sub2) = \'%s\' and trim(sub3) = \'%s\' and category = \'%s\'''' % (rep1,rep2,'General',category_value)# sub_left
#             code_value=dbconn.SelectQuery(qry4)[0][0]
#             qry6 = '''SELECT category_id FROM categories where trim(category_code) = \'%s\'''' % (code_value)# sub
#             category_tree_parent=dbconn.SelectQuery(qry6)[0][0]
#             print dbconn.SelectQuery(qry6)
#             create_category_tree(category_tree_child, category_tree_parent,dbconn)
#             
#         except:
#             print 'insert_sub3'
#             pdb.set_trace()
#             # pdb.set_trace()
#     qry2 = '''SELECT * FROM categories ''' 
#     print dbconn.SelectQuery(qry2)
    
def insert_sub_category_General(sub_left,sub,sub_right,dbconn):
    qry = '''SELECT code, %s, %s FROM bisac where trim(%s) = \'%s\'''' % (sub_left,sub,sub_right,'General')
    code_sub1_tuple_list=dbconn.SelectQuery(qry)
    # print dbconn.SelectQuery(qry)
    for tuples in code_sub1_tuple_list:
        # pdb.set_trace()
        # code=tuples[0]
        # sub_left=tuples[1] 
        # sub=tuples[2] is the one inserted
        # pdb.set_trace()
        rep2=tuples[2].replace("\'", "\\'")
        rep1=tuples[1].replace("\'", "\\'")
        try:
            qry1 = '''INSERT INTO categories (category_code, category_display_name ) VALUES (\'%s\',\'%s\') RETURNING category_id, category_code, category_display_name ''' % (tuples[0], rep2)
            print qry1
            # pdb.set_trace()
            dbconn.ChangeQuery(qry1)
            # dbconn.Commit()
            qry3 = '''SELECT category_id FROM categories where trim(category_code) = \'%s\'''' % (tuples[0])# sub
            category_tree_child=dbconn.SelectQuery(qry3)[0][0]
            print dbconn.SelectQuery(qry3)
            qry5 = '''SELECT category FROM bisac where trim(code) = \'%s\'''' % (tuples[0])# category
            category_value=dbconn.SelectQuery(qry5)[0][0]
            qry4 = '''SELECT code FROM bisac where trim(%s) = \'%s\' and trim(%s) = \'%s\' and trim(category) = \'%s\'''' % (sub_left,rep1,sub,'General',category_value)# sub_left
            code_value=dbconn.SelectQuery(qry4)[0][0]
            qry6 = '''SELECT category_id FROM categories where trim(category_code) = \'%s\'''' % (code_value)# sub
            category_tree_parent=dbconn.SelectQuery(qry6)[0][0]
            print dbconn.SelectQuery(qry6)
            create_category_tree(category_tree_child, category_tree_parent,dbconn)
            
        except:
            print 'insert_sub_category_General'
            pdb.set_trace()
            # pdb.set_trace()
    # qry2 = '''SELECT * FROM categories ''' 
    # print dbconn.SelectQuery(qry2)
    
    
    

def insert_sub_category_NON_General(sub_left,sub,sub_right,dbconn):
    
    qry = '''SELECT code, %s, %s FROM bisac where trim(%s) is null and trim(%s) <> \'%s\' and trim(%s) <>  \'\'''' % (sub_left,sub,sub_right,sub,'General',sub)
    code_sub1_tuple_list=dbconn.SelectQuery(qry)
    # print dbconn.SelectQuery(qry)
    for tuples in code_sub1_tuple_list:
        # pdb.set_trace()
        # code=tuples[0]
        # sub_left=tuples[1]
        # sub=tuples[2] is the one inserted
        # pdb.set_trace()
        rep2=tuples[2].replace("\'", "\\'")
        rep1=tuples[1].replace("\'", "\\'")
        try:
            qry1 = '''INSERT INTO categories (category_code, category_display_name ) VALUES (\'%s\',\'%s\') RETURNING category_id, category_code, category_display_name ''' % (tuples[0], rep2)
            print qry1
            # pdb.set_trace()
            dbconn.ChangeQuery(qry1)
            # dbconn.Commit()
            qry3 = '''SELECT category_id FROM categories where trim(category_code) = \'%s\'''' % (tuples[0])# sub
            category_tree_child=dbconn.SelectQuery(qry3)[0][0]
            print dbconn.SelectQuery(qry3)
            qry5 = '''SELECT category FROM bisac where trim(code) = \'%s\'''' % (tuples[0])# category
            category_value=dbconn.SelectQuery(qry5)[0][0]
            qry4 = '''SELECT code FROM bisac where trim(%s) = \'%s\' and trim(%s) = \'%s\' and trim(category) = \'%s\'''' % (sub_left,rep1,sub,'General',category_value)# sub_left
            
            if dbconn.SelectQuery(qry4)!=[]:
                code_value=dbconn.SelectQuery(qry4)[0][0]
                qry6 = '''SELECT category_id FROM categories where trim(category_code) = \'%s\'''' % (code_value)# sub
                category_tree_parent=dbconn.SelectQuery(qry6)[0][0]
                print dbconn.SelectQuery(qry6)
                create_category_tree(category_tree_child, category_tree_parent,dbconn)
            else:
                qry7 = '''SELECT code FROM bisac where trim(sub1) = \'%s\' and trim(category) = \'%s\'''' % ('General',category_value)# sub_left
                code_value=dbconn.SelectQuery(qry7)[0][0]
                qry8 = '''SELECT category_id FROM categories where trim(category_code) = \'%s\'''' % (code_value)# sub
                category_tree_parent=dbconn.SelectQuery(qry8)[0][0]
                print dbconn.SelectQuery(qry8)
                create_category_tree(category_tree_child, category_tree_parent,dbconn)
        except:
            print 'insert_sub_category_NON_General'
            pdb.set_trace() 
            # pdb.set_trace()    
    
    # qry2 = '''SELECT * FROM categories ''' 
    # print dbconn.SelectQuery(qry2)


if __name__ == '__main__':
    dbconn = simpledb.SimpledbClass("pgsql", "localhost", "dev", "", "dev")
    insert_sub_category_General('category','sub1','sub2',dbconn)
    print 'General sub1 is done '
    insert_sub_category_General('sub1','sub2','sub3',dbconn)
    print 'General sub2 is done'
    # insert_sub3(dbconn)
    # print 'sub3 is done '
    
    # insert_sub_category_NON_General('category','category','sub1',dbconn)
    # print 'NON category is done'
    insert_sub_category_NON_General('category','sub1','sub2',dbconn)
    print 'NON sub1 is done'
    insert_sub_category_NON_General('sub1','sub2','sub3',dbconn)
    print 'NON sub2 is done'
    dbconn.Commit()
    # insert_sub_category_NON_General('sub2','sub3','sub4',dbconn)
    # print 'NON sub3 is done'

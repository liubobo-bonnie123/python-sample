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


# def create_category_tree(category_tree_child, category_tree_parent):
#     dbconn = simpledb.SimpledbClass("pgsql", "localhost", "dev", "", "dev")
#     qry5 = '''INSERT INTO category_tree (category_tree_child, category_tree_parent)  VALUES (\'%s\',\'%s\')''' % (category_tree_child, category_tree_parent)
#     print qry5
#     dbconn.ChangeQuery(qry5)
#     dbconn.Commit()
#     qry6 = '''SELECT * FROM category_tree ''' 
#     print dbconn.SelectQuery(qry6)
    
def insert_sub3(dbconn):
    qry = '''SELECT code, sub3 FROM bisac where sub3 is not null and sub3 <> \'%s\'''' % ('General')
    code_sub1_tuple_list=dbconn.SelectQuery(qry)
    for tuples in code_sub1_tuple_list:
        rep=tuples[1].replace("\'", "\\'")
        try:
            qry1 = '''INSERT INTO categories (category_code, category_display_name ) VALUES (\'%s\',\'%s\') RETURNING category_id, category_code, category_display_name ''' % (tuples[0], rep)
            print qry1
            # pdb.set_trace()
            dbconn.ChangeQuery(qry1)
        except:
            pdb.set_trace()
    qry2 = '''SELECT * FROM categories ''' 
    print dbconn.SelectQuery(qry2)
    
def insert_sub_category_General(sub_left,sub,sub_right,dbconn):
    qry = '''SELECT code, %s, %s FROM bisac where %s = \'%s\'''' % (sub_left,sub,sub_right,'General')
    code_sub1_tuple_list=dbconn.SelectQuery(qry)
    # print dbconn.SelectQuery(qry)
    for tuples in code_sub1_tuple_list:
        # pdb.set_trace()
        # code=tuples[0]
        # sub_left=tuples[1] 
        # sub=tuples[2] is the one inserted
        # pdb.set_trace()
        rep=tuples[2].replace("\'", "\\'")
        try:
            qry1 = '''INSERT INTO categories (category_code, category_display_name ) VALUES (\'%s\',\'%s\') RETURNING category_id, category_code, category_display_name ''' % (tuples[0], rep)
            print qry1
            # pdb.set_trace()
            dbconn.ChangeQuery(qry1)
        except:
            pdb.set_trace()
        # dbconn.Commit()
        # qry2 = '''SELECT * FROM categories ''' 
        # print dbconn.SelectQuery(qry2)
        # qry3 = '''SELECT category_id FROM categories where category_display_name = \'%s\'''' % (tuples[2])# sub
        # qry4 = '''SELECT category_id FROM categories where category_display_name = \'%s\'''' % (tuples[1])# sub_left
        # category_tree_child=dbconn.SelectQuery(qry3)[0][0]
        # category_tree_parent=dbconn.SelectQuery(qry4)[0][0]
        # print category_tree_child
        # print category_tree_parent
        # create_category_tree(category_tree_child, category_tree_parent)
        # dbconn.Commit()
    qry2 = '''SELECT * FROM categories ''' 
    print dbconn.SelectQuery(qry2)
    
    
    

def insert_sub_category_NON_General(sub_left,sub,sub_right,dbconn):
    
    qry = '''SELECT code, %s, %s FROM bisac where %s is null and %s <> \'%s\' and %s <>  \'\'''' % (sub_left,sub,sub_right,sub,'General',sub)
    code_sub1_tuple_list=dbconn.SelectQuery(qry)
    # print dbconn.SelectQuery(qry)
    for tuples in code_sub1_tuple_list:
        # pdb.set_trace()
        # code=tuples[0]
        # sub_left=tuples[1]
        # sub=tuples[2] is the one inserted
        # pdb.set_trace()
        tuples[2].replace("\'", "\\'")
        rep=tuples[2].replace("\'", "\\'")
        try:
            qry1 = '''INSERT INTO categories (category_code, category_display_name ) VALUES (\'%s\',\'%s\') RETURNING category_id, category_code, category_display_name ''' % (tuples[0], rep)
            print qry1
            # pdb.set_trace()
            dbconn.ChangeQuery(qry1)
        except:
            pdb.set_trace()  
        # dbconn.Commit()
        # qry2 = '''SELECT * FROM categories ''' 
        # print dbconn.SelectQuery(qry2)
        # qry3 = '''SELECT category_id FROM categories where category_display_name = \'%s\'''' % (tuples[2])# sub
        # qry4 = '''SELECT category_id FROM categories where category_display_name = \'%s\'''' % (tuples[1])# sub_left
        # category_tree_child=dbconn.SelectQuery(qry3)[0][0]
        # category_tree_parent=dbconn.SelectQuery(qry4)[0][0]
        # print category_tree_child
        # print category_tree_parent
        # create_category_tree(category_tree_child, category_tree_parent)
    
    qry2 = '''SELECT * FROM categories ''' 
    print dbconn.SelectQuery(qry2)


if __name__ == '__main__':
    dbconn = simpledb.SimpledbClass("pgsql", "localhost", "dev", "", "dev")
    insert_sub_category_General('category','sub1','sub2',dbconn)
    print 'General sub1 is done '
    insert_sub_category_General('sub1','sub2','sub3',dbconn)
    print 'General sub2 is done'
    insert_sub3(dbconn)
    print 'sub3 is done '
    
    # insert_sub_category_NON_General('category','category','sub1',dbconn)
    # print 'NON category is done'
    insert_sub_category_NON_General('category','sub1','sub2',dbconn)
    print 'NON sub1 is done'
    insert_sub_category_NON_General('sub1','sub2','sub3',dbconn)
    print 'NON sub2 is done'
    # insert_sub_category_NON_General('sub2','sub3','sub4',dbconn)
    # print 'NON sub3 is done'
    dbconn.Commit()

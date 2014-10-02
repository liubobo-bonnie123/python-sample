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


def create_category_tree(category_tree_child, category_tree_parent):
    dbconn = simpledb.SimpledbClass("pgsql", "localhost", "dev", "", "dev")
    qry = '''INSERT INTO category_tree (category_tree_child, category_tree_parent)  VALUES (\'%s\',\'%s\')''' % (category_tree_child, category_tree_parent)
    # print qry1
    dbconn.ChangeQuery(qry1)
    # dbconn.Commit()



    
if __name__ == '__main__':
# def insert_sub_category_General(sub_left,sub,sub_right):#    insert_sub_category_General(category,sub1,sub2)
    dbconn = simpledb.SimpledbClass("pgsql", "localhost", "dev", "", "dev")
    qry = '''SELECT code, category,sub1 FROM bisac where sub2 = \'%s\'''' % ('General')
    code_sub1_tuple_list=dbconn.SelectQuery(qry)
    # print dbconn.SelectQuery(qry)
    for tuples in code_sub1_tuple_list:
        # pdb.set_trace()
        # code=tuples[0]
        # sub_left=tuples[1] 
        # sub=tuples[2] is the one inserted
        pdb.set_trace()
        qry1 = '''INSERT INTO categories (category_code, category_display_name ) VALUES (\'%s\',\'%s\') RETURNING category_id, category_code, category_display_name ''' % (tuples[0], tuples[2])
        # print qry1
        # pdb.set_trace()
        dbconn.ChangeQuery(qry1)
        qry3 = '''SELECT category_id FROM categories where category_display_name = \'%s\'''' % (tuples[2])# sub
        qry4 = '''SELECT category_id FROM categories where category_display_name = \'%s\'''' % (tuples[1])# sub_left
        category_tree_child=dbconn.ChangeQuery(qry3)
        category_tree_parent=dbconn.ChangeQuery(qry4)
        create_category_tree(category_tree_child, category_tree_parent)
        # dbconn.Commit()
    qry2 = '''SELECT * FROM categories ''' 
    print dbconn.SelectQuery(qry2)
    
    
    
# def insert_sub_category_General(sub_left,sub,sub_right):#    insert_sub_category_General(sub1,sub2,sub3)
    dbconn = simpledb.SimpledbClass("pgsql", "localhost", "dev", "", "dev")
    qry = '''SELECT code, sub1,sub2 FROM bisac where sub3 = \'%s\'''' % ('General')
    code_sub1_tuple_list=dbconn.SelectQuery(qry)
    # print dbconn.SelectQuery(qry)
    for tuples in code_sub1_tuple_list:
        # pdb.set_trace()
        # code=tuples[0]
        # sub_left=tuples[1] 
        # sub=tuples[2] is the one inserted
        pdb.set_trace()
        qry1 = '''INSERT INTO categories (category_code, category_display_name ) VALUES (\'%s\',\'%s\') RETURNING category_id, category_code, category_display_name ''' % (tuples[0], tuples[2])
        # print qry1
        # pdb.set_trace()
        dbconn.ChangeQuery(qry1)
        qry3 = '''SELECT category_id FROM categories where category_display_name = \'%s\'''' % (tuples[2])# sub
        qry4 = '''SELECT category_id FROM categories where category_display_name = \'%s\'''' % (tuples[1])# sub_left
        category_tree_child=dbconn.ChangeQuery(qry3)
        category_tree_parent=dbconn.ChangeQuery(qry4)
        create_category_tree(category_tree_child, category_tree_parent)
        # dbconn.Commit()
    qry2 = '''SELECT * FROM categories ''' 
    print dbconn.SelectQuery(qry2)

# def insert_sub_category_NON_General(sub_left,sub):    insert_sub_category_NON_General(category,sub1)
    dbconn = simpledb.SimpledbClass("pgsql", "localhost", "dev", "", "dev")
    qry = '''SELECT code, category,sub1 FROM bisac where sub1 <> \'%s\'''' % ('General')
    code_sub1_tuple_list=dbconn.SelectQuery(qry)
    # print dbconn.SelectQuery(qry)
    for tuples in code_sub1_tuple_list:
        # pdb.set_trace()
        # code=tuples[0]
        # sub_left=tuples[1]
        # sub=tuples[2] is the one inserted
        pdb.set_trace()
        qry1 = '''INSERT INTO categories (category_code, category_display_name ) VALUES (\'%s\',\'%s\') RETURNING category_id, category_code, category_display_name ''' % (tuples[0], tuples[2])
        # print qry1
        # pdb.set_trace()
        dbconn.ChangeQuery(qry1)
        qry3 = '''SELECT category_id FROM categories where category_display_name = \'%s\'''' % (tuples[2])# sub
        qry4 = '''SELECT category_id FROM categories where category_display_name = \'%s\'''' % (tuples[1])# sub_left
        category_tree_child=dbconn.ChangeQuery(qry3)
        category_tree_parent=dbconn.ChangeQuery(qry4)
        create_category_tree(category_tree_child, category_tree_parent)
        # dbconn.Commit()
    qry2 = '''SELECT * FROM categories ''' 
    print dbconn.SelectQuery(qry2)


# def insert_sub_category_NON_General(sub_left,sub):    insert_sub_category_NON_General(sub1,sub2)
    dbconn = simpledb.SimpledbClass("pgsql", "localhost", "dev", "", "dev")
    qry = '''SELECT code, sub1,sub2 FROM bisac where sub2 <> \'%s\'''' % ('General')
    code_sub1_tuple_list=dbconn.SelectQuery(qry)
    # print dbconn.SelectQuery(qry)
    for tuples in code_sub1_tuple_list:
        # pdb.set_trace()
        # code=tuples[0]
        # sub_left=tuples[1]
        # sub=tuples[2] is the one inserted
        pdb.set_trace()
        qry1 = '''INSERT INTO categories (category_code, category_display_name ) VALUES (\'%s\',\'%s\') RETURNING category_id, category_code, category_display_name ''' % (tuples[0], tuples[2])
        # print qry1
        # pdb.set_trace()
        dbconn.ChangeQuery(qry1)
        qry3 = '''SELECT category_id FROM categories where category_display_name = \'%s\'''' % (tuples[2])# sub
        qry4 = '''SELECT category_id FROM categories where category_display_name = \'%s\'''' % (tuples[1])# sub_left
        category_tree_child=dbconn.ChangeQuery(qry3)
        category_tree_parent=dbconn.ChangeQuery(qry4)
        create_category_tree(category_tree_child, category_tree_parent)
        # dbconn.Commit()
    qry2 = '''SELECT * FROM categories ''' 
    print dbconn.SelectQuery(qry2)



# def insert_sub_category_NON_General(sub_left,sub):    insert_sub_category_NON_General(sub2,sub3)
    dbconn = simpledb.SimpledbClass("pgsql", "localhost", "dev", "", "dev")
    qry = '''SELECT code, sub2,sub3 FROM bisac where sub3 <> \'%s\'''' % ('General')
    code_sub1_tuple_list=dbconn.SelectQuery(qry)
    # print dbconn.SelectQuery(qry)
    for tuples in code_sub1_tuple_list:
        # pdb.set_trace()
        # code=tuples[0]
        # sub_left=tuples[1]
        # sub=tuples[2] is the one inserted
        pdb.set_trace()
        qry1 = '''INSERT INTO categories (category_code, category_display_name ) VALUES (\'%s\',\'%s\') RETURNING category_id, category_code, category_display_name ''' % (tuples[0], tuples[2])
        # print qry1
        # pdb.set_trace()
        dbconn.ChangeQuery(qry1)
        qry3 = '''SELECT category_id FROM categories where category_display_name = \'%s\'''' % (tuples[2])# sub
        qry4 = '''SELECT category_id FROM categories where category_display_name = \'%s\'''' % (tuples[1])# sub_left
        category_tree_child=dbconn.ChangeQuery(qry3)
        category_tree_parent=dbconn.ChangeQuery(qry4)
        create_category_tree(category_tree_child, category_tree_parent)
        # dbconn.Commit()
    qry2 = '''SELECT * FROM categories ''' 
    print dbconn.SelectQuery(qry2)




# if __name__ == '__main__':
# 
#     insert_sub_category_General(category,sub1,sub2)
#     insert_sub_category_General(sub1,sub2,sub3)
#     insert_sub_category_NON_General(category,sub1)
#     insert_sub_category_NON_General(sub1,sub2)
#     insert_sub_category_NON_General(sub2,sub3)


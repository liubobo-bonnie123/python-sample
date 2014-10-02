#!/usr/bin/python2.6

import sys
import psycopg2

class PGSQL(object):
  def __init__(self, host, user, password, database):
    try:
      connectstring = "dbname='"+database+"' user='"+user+"' host='"+host+"' password='"+password+"'"
      self.db_handle = psycopg2.connect(connectstring)
      self.db_cursor = self.db_handle.cursor()
    except:
      print "Conection to host "+host+" failed."
      sys.exit()

def open_cms_db():
  opened_db = PGSQL("10.176.97.140", "hearst_ro", "@Jg]dFDRm,1HD/^U#a6Jwk&QU,y@Y[5", "hearst");
  return opened_db
#!/usr/bin/python2.6

import simpledb

def OpenDB():
  """ Connect to the fsst databases via the internal IP. SimpledbClass takes database type,
  host, user, password, and database name. """
  OpenedDB = simpledb.SimpledbClass("pgsql", "10.176.97.140", "hearst_ro", "@Jg]dFDRm,1HD/^U#a6Jwk&QU,y@Y[5", "hearst")
  return OpenedDB
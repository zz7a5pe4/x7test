#/usr/bin/python

import unittest  
import ConfigParser
import os,sys,time
from tools.shcmd import syncexec_timeout as run
from tools.output import *

class vmTestCase(unittest.TestCase):  
    def setUp(self):  
        config=ConfigParser.ConfigParser()
        config.read("test.cfg")
        for e,v in config.items("openrc"):
            os.environ[e.upper()]=v
        
    def tearDown(self):  
        pass
      
    def testList(self):  
        r = run(r"nova list")
        if not r:
            print r.error
            self.assertTrue(None)
    
    def testCreate(self):
        r = run(r"nova flavor-list")
        if not r:
            print r.error
            self.assertTrue(None)
        
        for l in r.output.split("\n"):
            if not "+" in l:
                f = flavor(l)
                if f.Name == "m1.tiny":
                    flavorid = f.ID
                    break
        
        r = run(r"nova image-list")
        if not r:
            print r.error
            self.assertTrue(None)
        
        for l in r.output.split("\n"):
            if not "+" in l:
                print l
                i = image(l)
                if i.Name == "cirros-0.3.0-x86_64-uec":
                    imageid = i.ID
                    break
        
        r = run(r"nova boot {0} --image {1} --flavor {2}".format("newimage", imageid, flavorid))
        if not r:
            print r.error
            self.assertTrue(None)

if __name__ == "__main__":  
    unittest.main()

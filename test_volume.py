#/usr/bin/python

import unittest  
import ConfigParser
import os
from tools.shcmd import syncexec_timeout as run

class volumeTestCase(unittest.TestCase):  
    def setUp(self):  
        config=ConfigParser.ConfigParser()
        config.read("test.cfg")
        for e,v in config.items("openrc"):
            os.environ[e.upper()]=v
        
    def tearDown(self):  
        pass
      
    def testList(self):  
        r = run(r"nova volume-list")
        if not r:
            print r.error
            self.assertTrue(None)
    
    def testCreate(self):
        pass
    
    def testDelete(self):
        pass
  
if __name__ == "__main__":  
    unittest.main()  

#/usr/bin/python

import unittest  
import ConfigParser
import os
from tools.shcmd import syncexec_timeout as run

class flavorTestCase(unittest.TestCase):  
    def setUp(self):  
        config=ConfigParser.ConfigParser()
        config.read("test.cfg")
        for e,v in config.items("openrc"):
            os.environ[e.upper()]=v
        
    def tearDown(self):  
        pass
      
    def testList(self):  
        r = run(r"nova flavor-list")
        self.assertTrue(r,str(r))
    
    def testCreate(self):
        """usage: nova flavor-create [--ephemeral <ephemeral>] [--swap <swap>]
                          [--rxtx-factor <factor>]
                          <name> <id> <ram> <disk> <vcpus>
        """
        r = run(r"nova  flavor-create  test 123 128 1 2")
        item = '| 123 | test      | 128       | 1    | 0         |      | 2     | 1.0         |\r'
        r = run(r"nova flavor-list")
        if not r:
            raise r
        else:
            if not item in r.output.split("\n")[3:-1]:
                self.assertTrue(None)
    
    def testDelete(self):
        r = run(r"nova flavor-delete 123")
        self.assertTrue(r,str(r))
  
if __name__ == "__main__":  
    unittest.main()  

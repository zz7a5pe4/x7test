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
        
        r = run(r"nova floating-ip-list")
        if not r:
            print r.error
            self.assertTrue(None)
        else:
            for i in r.output.split("\n")[3:-1]:
                self.newip = i.split("|")[1].strip()
                break
    
    def tearDown(self):  
        pass
        
    def testCreate(self):
        r = run(r"nova add-floating-ip  {0} {1}".format("newimage", self.newip))
        if not r:
            print r.error
            self.assertTrue(None)
        
        r = run(r"ping -c 1 -i 10 {0}".format(self.newip))
        if not r:
            print r.error
            self.assertTrue(None)
            
    def testDelete(self):
        r = run(r"nova remove-floating-ip {0} {1}".format("newimage", self.newip))
        if not r:
            print r.error
            self.assertTrue(None)
  
if __name__ == "__main__":  
    unittest.main()  

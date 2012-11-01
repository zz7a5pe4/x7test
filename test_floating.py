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
            raise r
        else:
            for i in r.output.split("\n")[3:-1]:
                self.newip = i.split("|")[1].strip()
                break
    
    def tearDown(self):  
        pass
        
    def testCreate(self):
        r = run(r"nova add-floating-ip  {0} {1}".format("newimage", self.newip))
        self.assertTrue(r,str(r))
        
        r = run(r"ping -c 1 -i 10 {0}".format(self.newip))
        self.assertTrue(r,str(r))
            
    def testDelete(self):
        r = run(r"nova remove-floating-ip {0} {1}".format("newimage", self.newip))
        self.assertTrue(r,str(r))
  
if __name__ == "__main__":  
    unittest.main()  

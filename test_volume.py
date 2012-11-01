#/usr/bin/python

import unittest  
import ConfigParser
import os
from tools.shcmd import syncexec_timeout as run
import time
from tools.output import volume

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
        self.assertTrue(r,str(r))

    
    def xtestCreate(self):
        r = run(r"nova volume-list")
        self.assertTrue(r,str(r))
        for l in r.output.split("\n")[3:-1]:
            if not "+" in l:
                i = volume(l)
                if i.Name == "testvolume1":
                    break
                    #print i
        else:
            r = run(r"nova volume-create --display_name testvolume1 5")
            if not r:
                print r.error
                self.assertTrue(None)
            time.sleep(3)
        
        
    def xtestDelete(self):
        volume_id = 0
        r = run(r"nova volume-list")
        if not r:
            raise r
        else:
            for l in r.output.split("\n")[3:-1]:
                if not "+" in l:
                    i = volume(l)
                    if i.Name == "testvolume1":
                        volume_id = i.ID
                        break
        
        if volume_id:
            r = run(r"nova volume-delete {0}".format(volume_id))
            if not r:
                raise r
        else:
            self.assertTrue(None)
        time.sleep(30)

if __name__ == "__main__":  
    unittest.main()  

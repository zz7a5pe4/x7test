#/usr/bin/python

import unittest  
import ConfigParser
import os


class falvorTestCase(unittest.TestCase):  
    def setUp(self):  
        config=ConfigParser.ConfigParser()
        config.read("test.cfg")
        for e,v in config.items("openrc"):
            os.environ[e.upper()]=v
        
    def tearDown(self):  
        pass
      
    def testArea(self):  
        self.assertEqual(10,10)  
      
    def testWidth(self):  
        os.system("nova list")
 
  
if __name__ == "__main__":  
    unittest.main()  

import unittest

def sum(a, b):
    
    return a+b



class Test(unittest.TestCase):
    
    def test1(self):
        
        self.assertEqual(sum(3, 3), 6)

    def test2(self):
        
        self.assertAlmostEqual(3, 3)  

    def test3(self):
        s = '哈囉你好嗎'
        self.assertRegex(s, '你好') 

    def test3(self):
        s = '哈囉你好嗎'
        self.assertIn('你好', s) 

    def test4(self):
        self.assertLess(10, 13)
        
    def test5(self):
        s = '哈囉你好嗎'
        self.assertNotRegex(s, '08')  

    def test6(self):
        a = [1,3,4,5]
        b = [5,4,3,1]
        self.assertCountEqual(a, b) 
if __name__ == '__main__':
    
    unittest.main()

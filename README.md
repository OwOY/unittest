# unittest

## How to use unittest

若 a = b，則測試通過
>> assertEqual(a,b，[msg='測試失敗時打印的信息'])  

若a != b，則測試通過
>> assertNotEqual(a,b，[msg='測試失敗時打印的信息'])  

若x是True，則測試通過
>> assertTrue(x，[msg='測試失敗時打印的信息'])  

若x是False，則測試通過
>> assertFalse(x，[msg='測試失敗時打印的信息'])  

若a是b，則測試通過
>> assertIs(a,b，[msg='測試失敗時打印的信息']) 

若a不是b，則測試通過
>> assertNotIs(a,b，[msg='測試失敗時打印的信息'])  

若x是None，則測試通過
>> assertIsNone(x，[msg='測試失敗時打印的信息'])  

若x不是None，則測試通過
>> assertIsNotNone(x，[msg='測試失敗時打印的信息'])  

若a在b中，則測試通過
>> assertIn(a,b，[msg='測試失敗時打印的信息'])  

若a不在b中，則測試通過
>> assertNotIn(a,b，[msg='測試失敗時打印的信息'])  

若a是b的一個實例，則測試通過
>> assertIsInstance(a,b，[msg='測試失敗時打印的信息'])  

若a不是b的實例，則測試通過
>> assertNotIsInstance(a,b，[msg='測試失敗時打印的信息'])  

round(a-b, 7) == 0
>> assertAlmostEqual(a, b)  

round(a-b, 7) != 0
>> assertNotAlmostEqual(a, b)  

a > b     
>> assertGreater(a, b)  

a >= b     
>> assertGreaterEqual(a, b)  

a < b   
>> assertLess(a, b)    

 a <= b   
>> assertLessEqual(a, b) 
  
regex.search(s)   
>> assertRegex(s, re)  
  
not regex.search(s)     
>> assertNotRegex(s, re)  

sorted(a) == sorted(b) and works with unhashable objs     
>> assertCountEqual(a, b)
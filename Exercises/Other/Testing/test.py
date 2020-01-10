import unittest
import script # import the file we gonna test

class TestMain(unittest.TestCase):
  def setUp(self): # this run before every test method, only in test.py because test2.py doesnt have this method
    print('about to test a function')

  def test_do_stuff(self):
    '''helloo''' # should be one line and it will shown in terminal when run unittest with -v flag, this runs before setUp method 
    test_param = 10
    result = script.do_stuff(test_param)
    self.assertEqual(result, 15) # expected result is 10+5=15

  def test_do_stuff2(self):
    test_param = 'gdfghs'
    result = script.do_stuff(test_param)
    self.assertIsInstance(result, ValueError) # expected result this sholdn't work, we retun an instance of ValueError class
    # self.assertTrue(isinstance(result, ValueError)) #another solution

  def test_do_stuff3(self):
    test_param = None
    result = script.do_stuff(test_param)
    self.assertEqual(result, 'please enter number')

  def test_do_stuff4(self):
    test_param = ''
    result = script.do_stuff(test_param)
    self.assertEqual(result, 'please enter number')
  
  def test_do_stuff5(self):
    test_param = 0
    result = script.do_stuff(test_param)
    self.assertEqual(result, 5) # expected result is 5

  def tearDown(self): # run at the end of each method we call before return ok, not used very often unless you test on a database
    print('cleaning up')


if __name__ == '__main__':
  unittest.main() #will run tests on this file

# run test.py file if tests are successful it returns time spent and OK
#                  if tests are not successsful returns time spent and FAIL(AssertionError)
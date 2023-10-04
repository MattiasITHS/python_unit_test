### Commands to run testcases

How to run all the tests within your directory?
- python3.6 -m unittest discover

How to run all tests in a specific module?
- python3.6 -m unittest tests.test_wealth_manager #test_wealth_manager == testcase

How to run a specific test case within a module?
- python3.6 unittest tests.test_wealth_manager.TestCalculate

How to run a specific method within a test case?
- python3.6 -m unittest tests.test_wealth_manager.TestCalculate.test_calculate_easy_first

### Commands to skip testcases

Use skip for any reason
- @unittest.skip('any reason')

Use skipif to check a library version
- @unittest.skipOf(sys.version[0] > 4, "needs to be version 4")

Use skipUnless to check the os system
- @unittest.skipUnless(sys.platform.startswitch("win"), "requires Windows")

Use expectedFailure if the tests are going to pass for sure
- @unittest.expectedFailure

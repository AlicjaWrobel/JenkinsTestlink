import testlink
import unittest
from testlink.testlinkerrors import TLResponseError
from unittest import (
    TestCase,
    TestLoader,
    TextTestResult,
    TextTestRunner)
import os
from pprint import pprint
#from calculator import addition

OK = 'ok'
FAIL = 'fail'
ERROR = 'error'
SKIP = 'skip'

class TestSimple(unittest.TestCase):

    def test_addition(self):
        sum = addition(3,5)
        print(sum)
        self.assertTrue(sum==8)

class JsonTestResult(TextTestResult):
 def __init__(self, stream, descriptions, verbosity):
  super_class = super(JsonTestResult, self)
  super_class.__init__(stream, descriptions, verbosity)
  # TextTestResult has no successes attr
  self.successes = []

 def addSuccess(self, test):
  # addSuccess do nothing, so we need to overwrite it.
  super(JsonTestResult, self).addSuccess(test)
  self.successes.append(test)

 def json_append(self, test, result, out):
   suite = test.__class__.__name__
   if suite not in out:
    out[suite] = {OK: [], FAIL: [], ERROR:[], SKIP: []}
   if result is OK:
    out[suite][OK].append(test._testMethodName)
   elif result is FAIL:
    out[suite][FAIL].append(test._testMethodName)
   elif result is ERROR:
    out[suite][ERROR].append(test._testMethodName)
   elif result is SKIP:
    out[suite][SKIP].append(test._testMethodName)
   else:
    raise KeyError("No such result: {}".format(result))
   return out

 def jsonify(self):
   json_out = dict()
   for t in self.successes:
    json_out = self.json_append(t, OK, json_out)
   for t, _ in self.failures:
    json_out = self.json_append(t, FAIL, json_out)
   for t, _ in self.errors:
    json_out = self.json_append(t, ERROR, json_out)
   for t, _ in self.skipped:
    json_out = self.json_append(t, SKIP, json_out)
   return json_out

if __name__ == '__main__':

 TESTLINK_API_PYTHON_SERVER_URL="http://192.168.168.103/lib/api/xmlrpc/v1/xmlrpc.php"
 TESTLINK_API_PYTHON_DEVKEY="37167987e1b7e42a5da0cfc1edfb540a"

 tlh = testlink.TestLinkHelper()
 testLink = tlh.connect(testlink.TestlinkAPIClient)
 testLink.__init__(TESTLINK_API_PYTHON_SERVER_URL, TESTLINK_API_PYTHON_DEVKEY)

 with open(os.devnull, 'w') as null_stream:
  runner = TextTestRunner(stream=null_stream)
  runner.resultclass = JsonTestResult
  suite = TestLoader().loadTestsFromTestCase(TestSimple)
  result = runner.run(suite)
  # print json output
  res = result.jsonify()['TestSimple']
 
 #try:
  testLink.reportTCResult(testcaseid=35 , testplanid=3 , buildname='Build_1.0.0', notes='some notes', status='p', user='tester',steps=[
  #testLink.reportTCResult(None, 2, None, 'p', '', guess=True, platformname='NewPlatform', execduration=3.9, timestamp='2015-09-18 14:33', steps=[
   {'step_number' : 1, 'result' : 'p','notes' : 'Invoked'},
   {'step_number' : 2, 'result' : 'p','notes' : 'Succeeded'}
   ])
 #except TLResponseError :
  #print(f'Wrong case')

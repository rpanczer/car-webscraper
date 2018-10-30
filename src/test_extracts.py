import unittest
import extracts

class TestExtracts(unittest.TestCase):
  #ensure a string of len 0 returns None
  def test_replace_newline_extract_0(self):
    result = extracts.replaceNewlineExtract('')
    self.assertIsNone(result)
  #ensure a None obj returns None
  def test_replace_newline_extract_1(self):
    result = extracts.replaceNewlineExtract(None)
    self.assertIsNone(result)
  #ensure new lines and returns are escaped
  def test_replace_newline_extract_2(self):
    a = 'This is a \ntest to\r remove ne\nwlines from'
    b = 'This is a \\ntest to\\r remove ne\\nwlines from'
    result_a = extracts.replaceNewlineExtract(a)
    self.assertEqual(result_a,b)

if __name__ == '__main__':
  unittest.main()
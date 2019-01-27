import unittest
from timecalc import *


class TestTimestring(unittest.TestCase):
  def test_is_timestring_minutes(self):
    self.assertEqual(is_timestring('05'), True)

  def test_is_timestring_hours(self):
    self.assertEqual(is_timestring('3h'), True)

  def test_is_timestring_hours_minutes(self):
    self.assertEqual(is_timestring('5h34'), True)

  def test_is_timestring_0(self):
    self.assertEqual(is_timestring(''), True)

  def test_is_timestring_malformed_1(self):
    self.assertEqual(is_timestring('05a'), False)

  def test_is_timestring_malformed_1(self):
    self.assertEqual(is_timestring('05:50'), False)


if __name__ == '__main__':
  unittest.main(verbosity=2)

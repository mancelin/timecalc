import unittest
from timecalc import *


class TestParseTimestring(unittest.TestCase):
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


class TestParseOperators(unittest.TestCase):
  def test_is_plus(self):
    self.assertEqual(is_plus('+'), True)

  def test_is_minus(self):
    self.assertEqual(is_minus('-'), True)

  def test_is_arrow(self):
    self.assertEqual(is_arrow('->'), True)

  def test_is_operator(self):
    self.assertEqual(is_operator('+'), True)

  def test_is_operator_2(self):
    self.assertEqual(is_operator('-'), True)

  def test_is_operator_3(self):
    self.assertEqual(is_operator('->'), True)

  def test_is_not_operator(self):
    self.assertEqual(is_operator('>'), False)


class TestOperators(unittest.TestCase):
  def test_add_time(self):
    t1 = Time('5h75')
    t2 = Time('3h2')
    self.assertEqual(str(t1 + t2), '9h17')

  def test_sub_time_1(self):
    t1 = Time('5h75')
    t2 = Time('7h2')
    self.assertEqual(str(t1 - t2), '-0h47')

  def test_sub_time_2(self):
    t1 = Time('2h50')
    t2 = Time('2h20')
    self.assertEqual(str(t1 - t2), '0h30')

  def test_sub_time_3(self):
    t1 = Time('1h10')
    t2 = Time('50')
    self.assertEqual(str(t1 - t2), '0h20')

  def test_sub_time_4(self):
    t1 = Time('-8h05')
    t2 = Time('9h84')
    self.assertEqual(str(t1 - t2), '-18h29')


if __name__ == '__main__':
  # unittest.main(verbosity=2)
  unittest.main()

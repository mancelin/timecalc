import re
import sys

class Time:
  def __init__(self, timestring):
    print("timestring : " + timestring)
    time_list = timestring.split('h')
    # just minutes, ex : '30'
    if len(time_list) == 1:
      self.hours = 0
      if (timestring == ''):
        self.minutes = 0
      else:
        self.minutes = int(time_list[0])
    if len(time_list) == 2:
      self.hours = int(time_list[0])
      if time_list[1] == '':
        self.minutes = 0
      else:
        self.minutes = int(time_list[1])

  def __str__(self):
    return "{} hours {} minutes".format(self.hours, self.minutes)


def is_timestring(str):
  return re.match('^\d*h?\d*?$', str) != None


def test_is_timestring(str):
  print("is_timestring('{}') : {}".format(str, is_timestring(str)))


if __name__ == '__main__':
  print("timecalc")
  args = sys.argv[1:]
  print(args)
  t = Time(args[0])
  t = Time('')
  print(t)
  test_is_timestring(args[0])
  test_is_timestring('3h51')
  test_is_timestring('3h')
  test_is_timestring('05')
  test_is_timestring('05ee')
  test_is_timestring('text')
  print(t)

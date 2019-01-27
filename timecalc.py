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

def is_plus(str):
  return re.match('^\+$', str) != None

def is_minus(str):
  return re.match('^-$', str) != None

def is_arrow(str):
  return re.match('^->$', str) != None

def is_operator(str):
  return is_plus(str) or is_minus(str) or is_arrow(str)

if __name__ == '__main__':
  print("timecalc")
  args = sys.argv[1:]
  print(args)

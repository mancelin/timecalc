import sys

class Time:
  def __init__(self, time_string):
    print("time_string : " + time_string)
    time_list = time_string.split('h')
    # just minutes, ex : '30'
    if len(time_list) == 1:
      self.hours = 0
      self.minutes = int(time_list[0])
    if len(time_list) == 2:
      self.hours = int(time_list[0])
      if time_list[1] == '':
        self.minutes = 0
      else:
        self.minutes = int(time_list[1])

  def __str__(self):
    return "{} hours {} minutes".format(self.hours, self.minutes)


if __name__ == '__main__':
  print("timecalc")
  args = sys.argv[1:]
  print(args)
  t = Time(args[0])
  print(t)

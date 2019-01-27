#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import sys

class Time:
  def __init__(self, timestring):
    time_list = timestring.split('h')
    # just minutes, ex : '30'
    if len(time_list) == 1:
      self.hours = 0
      if (timestring == ''):
        self.minutes = 0
      else:
        self.minutes = int(time_list[0])
    elif len(time_list) == 2:
      self.hours = int(time_list[0])
      if time_list[1] == '':
        self.minutes = 0
      else:
        self.minutes = int(time_list[1])
    self.sign = ''
    self.minutes_to_hours()

  def minutes_to_hours(self):
    is_negative = False
    if self.hours < 0 or self.minutes < 0:
      self.sign = '-'
      is_negative = True
      self.hours = abs(self.hours)
      self.minutes = abs(self.minutes)
    if self.minutes >= 60:
      self.hours = self.hours + int(self.minutes / 60)
      self.minutes = self.minutes % 60
    if is_negative:
      self.hours *= -1
      self.minutes *= -1

  def to_minutes(self):
    self.minutes = 60 * self.hours + self.minutes
    self.hours = 0

  def __str__(self):
    return '{}{}h{}'.format(self.sign, abs(self.hours), str(abs(self.minutes)).zfill(2))

  def __add__(self, other):
    t = Time('')
    t.minutes = self.minutes + other.minutes
    t.hours = self.hours + other.hours
    t.minutes_to_hours()
    return t

  def __sub__(self, other):
    t = Time('')
    self.to_minutes()
    other.to_minutes()
    t.minutes = self.minutes - other.minutes
    t.minutes_to_hours()
    return t

  # -> opérator
  def to(self, other):
    return other - self


def is_timestring(str):
  return re.match('^\d*h?\d*?$', str) != None

def is_plus(str):
  return re.match('^\+$', str) != None

def is_minus(str):
  return re.match('^-$', str) != None

# use -> and also char 'v' as arrow operator to use arrow without needing '' protection on console
def is_arrow(str):
  return re.match('^->$', str) != None or re.match('^v$', str) != None

def is_operator(str):
  return is_plus(str) or is_minus(str) or is_arrow(str)

if __name__ == '__main__':
  args = sys.argv[1:]
  print(args)
  previous_arg = None
  previous_time = None
  current_operator = None
  total = Time('')
  for arg in args:
    if is_timestring(arg):
      if previous_arg == 'timestring':
        print('Malformed operation : 2 consecutive timestrings')
      else:
        current_time = Time(arg)
        if current_operator == '+':
          total += previous_time + current_time
        if current_operator == '-':
          total += previous_time - current_time
        if current_operator == '->':
          total += previous_time.to(current_time)
        previous_time = current_time
        previous_arg = 'timestring'
    if is_operator(arg):
      if previous_arg == 'operator':
        print('Malformed operation : 2 consecutive operators')
      else:
        if is_plus(arg):
          current_operator = '+'
        elif is_minus(arg):
          current_operator = '-'
        elif is_arrow(arg):
          current_operator = '->'
        previous_arg = 'operator'
  print(total)

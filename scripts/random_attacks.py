#!/bin/python

import random
from time import sleep

prob_victim = [1, 1, 2, 2, 3]
prob_attacker = [3, 1, 2, 3, 1]
min_time = 1
max_time = 5

DATA = [{
  "id": i, 
  "victim": sum(prob_victim[:i + 1])/sum(prob_victim), 
  "attacker": sum(prob_attacker[:i + 1])/sum(prob_attacker)}
  for i in range(len(prob_victim))]

def get_random(key):
  r = random.random()
  for person in DATA:
    if person[key] > r:
      return person["id"]

  raise ValueError('Cannot get {} for random number: {}'.format(key, r))

def get_random_victim():
  return get_random("victim")

def get_random_attacker():
  return get_random("attacker")

while True:
  victim = get_random_victim()
  attacker = get_random_attacker()
  print("{} attacking {}".format(attacker, victim))

  to_sleep = random.random() * (max_time - min_time) + min_time
  sleep(to_sleep)



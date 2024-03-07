# Write a Python program that invoke square root function after specific milliseconds.
import math as m
import time as t

n = int(input())
sec = int(input())
t.sleep(sec / 1000)
print(m.sqrt(n))
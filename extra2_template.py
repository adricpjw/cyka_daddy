### Question 1
def total_money(principal, annual, year, monthly):
  interest = annual/12 + 1
  amount_accrued = principal * interest ** (year*12)
  contribution = 0
  for i in range(1,year*12):
    contribution += monthly * interest ** i
  
  return round(amount_accrued + contribution,2)

### TEST
# print(total_money(100000, 0.06, 1, 1000))
# print(total_money(100000, 0.06, 15, 1000))

### Question 2
from math import *
def projectile_motion(v0, angle, gravity):
  theta = radians(angle)
  if angle < 90:
    inityVelo = v0 * sin(theta)
    initxVelo = v0 * cos(theta)
  else:
    inityVelo = v0 * sin(pi-theta)
    initxVelo = v0 * cos(pi-theta)

  curryVelo = inityVelo
  xdisp = 0
  ydisp = 0

  ydisp += inityVelo
  xdisp += initxVelo

  while ydisp > 0:
    curryVelo -=gravity
    ydisp += curryVelo
    xdisp += initxVelo


  return xdisp

### TEST
# print(projectile_motion(30, 100, 9.8))
# print(projectile_motion(30, 80, 9.8))


### Question 3
def triangle(a, b, c):

  if a+b <= c or a+c<=b or b+c<=a:
    return 'Not a triangle'
  elif a == b == c:
    return 'Equilateral'
  elif a==b or b == c or a ==c:
    return 'Isosceles'
  elif a != b != c:
    return 'Scalene'
### TEST
# print(triangle(1,1,1))
# print(triangle(1,2,2))
# print(triangle(2,3,4))
# print(triangle(1,2,1))

### Question 4
def ip_binary(ip):

  splitUp = str(ip).split(".")
  print(splitUp)
  outPut = []

  for i in splitUp:
    number = int(i)
    # print(number)
    quotient = floor(number/2)
    remainder = number % 2

    outPut.insert(,str(remainder))

    while quotient != 0:
      remainder = quotient % 2
      outPut.insert(0,str(remainder))
      quotient = floor(quotient/2)

    outPut.append('.')
  outputString = "".join(outPut)
  return outputString


### TEST
print(ip_binary('192.168.0.1'))
# print(ip_binary('127.0.0.1'))

### Question 5
def is_same_network(ip1, ip2, subnet):
  pass
### TEST
# print(is_same_network('192.168.0.1', '192.168.0.3', '255.255.255.0'))
# print(is_same_network('192.168.0.1', '192.168.0.3', '255.255.255.254'))
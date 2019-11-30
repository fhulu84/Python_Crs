# Given a range of numbers. Iterate from o^th number to the end number
# and print the sum of the current number and previous number


def sumNum(num):
  preNum = 0
  for i in range(num):
    sum = preNum + i
    print(sum)
    preNum = i


sumNum(10)

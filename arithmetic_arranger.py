import re

def arithmetic_arranger(problems,solve=False):
  #want to change the string into one that is formatted to look good once run
  #we want to limit the number of problems to no more than five in the string   
  if(len(problems) >5):
    return "Error: Too many problems."

  first = ""
  second = ""
  lines = ""
  sumx = ""
  string = ""
  for problem in problems:
    #we only want digits, so we need to return an error if anything other than digits are found (use anything other than notation)
    #remember to close the brackets
    if(re.search("[^\s0-9.+-]", problem)):
      #This code is because we only want to look at addition or subtraction problems, not multiplication or division
      if (re.search("[/]", problem) or re.search("[*]", problem)):
         return "Error: Operator must be '+' or '-'."
         #Had a random q in the line above which caused the test to fail at first
      return "Error: Numbers must only contain digits."
    
    #This identifies and labels the parts of the string, by splitting and using indexing... remember the first component is actually zero for the index 
    firstNumber = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    secondNumber = problem.split(" ")[2]
    #This code asserts that we do not want any numbers that are greater than four digits in the problems 
    if(len(firstNumber) >= 5 or len(secondNumber) >= 5):
      return "Error: Numbers cannot be more than four digits."
    #This line indicates that the sum of each of the problems will be a string
    sum = ""
    #the '==' in python indicates 'equal to'
    #The following four lines indicate that if it is an addition problem, the sum is the numbers added together... and if it is a subtraction problem, the sum is the secondNumber subtracted from the firstNumber 
    if (operator == "+"):
      sum = str(int(firstNumber)+ int(secondNumber))
    elif(operator =="-"):
      sum = str(int(firstNumber)- int(secondNumber))

    #These lines indicate the spacing for the problems. 
    length = max(len(firstNumber), len(secondNumber)) +2
    top = str(firstNumber).rjust(length)
    bottom = operator +str(secondNumber).rjust(length-1)
    line=""
    res=str(sum).rjust(length)
    for s in range(length):
      #the += adds another value with the variables value and assigns the new value to the variable 
      line += "-"

    #This code basically makes sure add spaces after every problem but the last problem, represented by '[-1]'
    #The '!=' means "not equal to"
    if problem != problems[-1]:
      first += top + '    '
      second += bottom + '    '
      lines += line + '    '
      sumx += res + '    '
    #This code refers to the lack of space after the last problem 
    else:
      first += top
      second += bottom
      lines += line 
      sumx += res
  #This last group indicates the setup of the information in lines, new lines created with '\n'
  if solve: 
    string = first + "\n" + second + "\n" + lines + "\n" + sumx
  else:
    string = first + "\n" + second + "\n" + lines
  return string 

    
    
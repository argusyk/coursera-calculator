from art import logo

def add(x, y):
  return x + y

def substract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

operations = {
  "+" : add,
  "-" : substract,
  "*" : multiply,
  "/" : divide
}

def inputs(count):
  num1 = float(input(f"What's the {count} number? "))
     
  for key in operations:
    print (f" {key} ")
  
  ops = input("What operation does you want to use: ")
  return num1, ops

def calc(num1, num2, ops):
  answer = operations[ops](num1, num2)
  print(f" {num1} {ops} {num2} = {answer}")
  return answer

ch = "yes"
count = 2

print(logo)
num1 = float(input("What's the first number? "))
 
while ch == "yes":
  num2, ops = inputs(count)
    
  answer = calc(num1, num2, ops)   
  ch = input("Another operation (yes) or (no)? ")
  if ch == "yes":
    count +=1
    num1 = answer
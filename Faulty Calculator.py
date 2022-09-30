print("What type of calculation you want to do? \n"
      "press '+' for addition \n"
      "press '-' for subtraction \n"
      "press '*' for multiplication \n"
      "press '/' for division \n")
operators = input("Enter operator: ")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

a = "+"
b = "-"
c = "*"
d = "/"

if operators==a:
      if n1 == 56 and n2 == 9:
            print("77")
      else:
            print(n1+n2)

elif operators==b:
      print(n1-n2)

elif operators==c:
      if n1 == 45 and n2 == 3:
            print("555")
      else:
            print(n1*n2)

elif operators==d:
      if n1 == 56 and n2 == 6:
            print("4")
      else:
            print(n1/n2)


print("THANKS FOR USING THE CALCULATOR")


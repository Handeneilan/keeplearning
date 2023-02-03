# Have an input 
year = int(input("Which year do you want to check?\n"))

# Leap Year Calculation
if year%4==0:
  print("leap year.")
elif year%100==0 and year%400==0:
  print("leap year.")
else:
  print("not leap year")
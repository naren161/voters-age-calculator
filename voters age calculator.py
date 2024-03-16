print("Welcome to voters age calculator ")
no_of_attempts = 3
while  no_of_attempts >=1:
  try:
    name = input("Enter your name : ").upper()
    if name.isalpha() == True:                  ##checking the give name is string or not
      age = int(input("Enter your age : "))
      if age>=18 and age<=100:
          print("Hi",name,"your age is",age, "you are elegible to vote")
          break
      else:
          no_of_attempts=no_of_attempts-1
          print("please verify your Date of Birth you have",no_of_attempts,"attempts")
          if no_of_attempts==0:
            print("sorry please try again after some time")
    else:
       no_of_attempts=no_of_attempts-1
       print("please enter a valid name you have",no_of_attempts,"attempts")
       if no_of_attempts==0:
            print("sorry please try again after some time")
  except ValueError:
    print("please enter age in correct format")  

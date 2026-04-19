n = int(input("Enter a number: "))
match n:
  case n if 100 >= n >= 80:
     print(" A+ ")
  case n if 79 >= n >= 70:
     print("A ")   
  case n if 69 >= n >= 60:
     print("A- ")  
  case n if 59 >= n >= 50:
     print("B")  
  case n if 49 >= n >= 40:
     print("C ")
  case n if 39 >= n >= 33:
     print("D ")       
  case _:
     print("Fail ")               
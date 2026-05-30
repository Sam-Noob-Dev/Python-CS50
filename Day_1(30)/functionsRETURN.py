def main ():
  name = input("Enter your name : ")
  return name

def greet(person):

  print("hello",person)
  
  # so inshort hamna ek fn se dusre fn ko bulaya directly ,abb hoga ye ki now i can access to main due to this so i can now use its local variable
  
greet(main())

"""
! wheneever you think of you want to access another fn from other fn bus yeh karo ki jo dusra fn hoga uske throgh 1st fn ko call kar do but ye yad rakhna ke pehle fn me return jarur use karna before calling it from the 2nd fn  




                  ****  LECTURE 0 FROM CS50P DONE  ****
"""
#  type conversion ,operator 

"""
Type conversion-

implicit - python will automatically convert the datatype 
eg int -> float 

explicit - python will not convert it you have to do on your own 
like this int(marks)

eg float -> int


! round(what value you want to round ,tell till what number of digit till you want)

eg shown below after type conv.
"""

#implicit 
marks  = float(input("Enter your marks : "))
print(f"So marks in int converted to float {marks}")

#explicit
marks = int(marks)
print(f"So marks in float converted to int  {marks}")


x = float(input("Give value of X : "))
y = float(input("Give value of Y : "))
z=round(x/y,2)
print(f"Your rounded ans : {z} ")
# Operators

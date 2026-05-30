 #Functions use def fn_name(){}  this how you define a fn then to call it use fn_name()
 
"""
Types 

no paremetrized function (here we dont give any parameter in fn )
,parameterised fn (here we give parameters in the fn define)
, default parameter fn (here we give parameters but with default value )

Return

so whenver using this always use a print statment and a varable also to print and store the value 

scope 

it means basically if you declared variable inside a fn1 and you wanna use that variable in a fn2 you cant use its because of scope 

Now this scope is of two types one which we seen above is a local scope or local variable which means if var is declared inside a fn1 it cant be used in any other fn

then there is global varable so they can be used inside ,outside of any fn you want and also declared outside of a fns 


"""

# now this name is correct eg of global variables 
name = input("Enter your name :")

#1st way
def hello():
  print("Hello ,"+name)

#2nd way now here the to is a local variable
def hello1(to="World"):
  print(f"hello, {to}")

#return way

def hello2(to="World"):
  return "Hello, "+to


hello()
hello1()
hello1(name)

result = hello2()
print(result)

result1 = hello2(name)
print(result1)
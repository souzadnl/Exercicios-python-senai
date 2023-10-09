"""
DRY (Don't Repeat Yourself): Simplifique o código usando uma função. 

print("Hello, John!") 

print("Hello, Jane!") 

print("Hello, Mike!") 
"""
name = input("Enter your name: ")
def hello():
    print(f"Hello, {name}!")

hello()
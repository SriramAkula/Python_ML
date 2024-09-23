# Local variable Vs Global variable
message="Hello"
def greet():
    message="Hello"
    print("Local ",message)
greet()
print(message)
# Using **kwargs
def display(**info):
    for key, value in info.items():
        print(key, value)

display(name="Ravi", age=22)

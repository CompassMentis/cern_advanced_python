# Not real code - should be broken up and run in threads

# Version 1 - No race condition

x = 5

# Thread 1 runs this code
def add_one():
    global x
    a = x
    a = a + 1
    x = a


# Then thread 2 runs this code
def add_one():
    global x
    a = x
    a = a + 1
    x = a

print(x)

# Version 2 - Race condition

x = 5

# Thread 1 runs this code
def add_one():
    global x
    a = x
    a = a + 1
    # Interrupted here
    # Subsequent code not run (yet)
    # x = a

# Next thread 2 runs this code
def add_one():
    global x
    a = x
    a = a + 1
    x = a

# Finally thread 1 finishes
def add_one():
    global x
    # a = x
    # a = a + 1
    x = a

print(x)




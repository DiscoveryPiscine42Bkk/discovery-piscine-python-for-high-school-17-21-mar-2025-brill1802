x = int(input(" type a number less than 25 "))
if x > 25:print("Error")
else:
    while x <= 25:
        print(f"Inside the loop, my variable is {x}")
        x = x + 1
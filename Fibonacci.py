def fibonacci(n):
    result = []
    x, y = 0, 1
    while x < n:    
        result.append(x)
        x, y = y, y + x
    print(result)
#LEAVE AT 35 TO GET FIRST 10 NUMBERS
fibonacci(35)

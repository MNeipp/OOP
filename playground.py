def fibonaci(num):
    if num == 1 or num == 0:
        return num
    else:
        return fibonaci(num-1) + fibonaci(num-2)

print (fibonaci (100))

from time import clock
max = 0
start = clock()
for i in range(100,1000):
 for y in range(100,1000):
    products = i * y
    str_products = str(products)
    if str_products[::-1] == str_products:
        if products > max:
            max = products

print max
print clock() - start

def triangle_route(file):
    textfile = open(file).read()
    str_triangle = [line.split(' ') for line in textfile.split('\n')]
    triangle = []
    for lines in str_triangle:
        numbers = [int(n) for n in lines]
        triangle.append(numbers) 
    u = len(triangle) 

    i = -2
    for y in range(u - 1):
        current_line = triangle[i]
        if y == 0:
            line_below = triangle[i+1]
        else:
            line_below = partial_sum
        partial_sum = []
        for n in range(len(current_line)):
            x = current_line[n]
            a, b = line_below[n], line_below[n+1]
            sum = max(x + a, x + b)
            partial_sum.append(sum)
        i += -1

    return partial_sum[0]
    
file = '67.txt'    
print triangle_route(file)
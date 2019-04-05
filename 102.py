textFileLines = open('102.txt').readlines()

NUMBER_OF_LINES = 1000
p_x, p_y = 0, 0
P = (p_x, p_y)

def crossProduct(A, B):
    return A[0]*B[1] - A[1]*B[0]

    
counter = 0
for i in range(NUMBER_OF_LINES):
    a_x, a_y, b_x, b_y, c_x, c_y = [int(a) for a in textFileLines[i].split(',')]
    A = (a_x, a_y)
    B = (b_x, b_y)
    C = (c_x, c_y)
    
    AP = (p_x - a_x, p_y - a_y)
    BP = (p_x - b_x, p_y - b_y)
    CP = (p_x - c_x, p_y - c_y)
    
    AB = (b_x - a_x, b_y - a_y)
    BC = (c_x - b_x, c_y - b_y)
    CA = (a_x - c_x, a_y - c_y)
    
    if (crossProduct(AP, AB) > 0 and crossProduct(BP, BC) > 0 and crossProduct(CP, CA) > 0):
        counter += 1
       
    if (crossProduct(AP, AB) < 0 and crossProduct(BP, BC) < 0 and crossProduct(CP, CA) < 0):
        counter += 1
        
print counter


import sys
import random

def freivald(a, b, c, n, x, m):
    # Generate a random vector
    r = [random.randint(0, 1) for _ in range(m)]
    
    # Now compute B*r for evaluating expression A * (B*r) - (C*r)
    br = [sum(b[i][j] * r[j] for j in range(m)) for i in range(x)]

    # Now compute C*r for evaluating expression A * (B*r) - (C*r)
    cr = [sum(c[i][j] * r[j] for j in range(m)) for i in range(n)]

    # Now compute A* (B*r) for evaluating expression A * (B*r) - (C*r)
    # axbr = [sum(a[i][j] * br[j] for j in range(x)) for i in range(n)]
    axbr = [0] * n
    for i in range(n):
        for j in range(x):
            axbr[i] += a[i][j] * br[j]
        if axbr[i] - cr[i] != 0:
            return False
    return True

def checkProduct(a, b, c, n, x, m, k):
    for _ in range(k):
        if not freivald(a, b, c, n, x, m):
            return False
    return True

def main():
    num_test_cases = int(sys.stdin.readline().strip())
    
    for _ in range(num_test_cases):
        sys.stdin.readline()  # Blank line
        
        n, x, y, m = map(int, sys.stdin.readline().strip().split())
        
        matrix_A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
        matrix_B = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(y)]
        matrix_C = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
        
        if x != y:
            print("Inner matrix dimensions must agree")
        else:
            if checkProduct(matrix_A, matrix_B, matrix_C, n, x, m, 10): 
                print("AC")
            else:
                print("WA")
                
if __name__ == "__main__":
    main()
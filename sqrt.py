import math
def sqrt_binary(n, epsilon):
    low = 0
    high = n + 0.25
    
    while high - low > epsilon:
        mid = (low + high) / 2
        if abs(mid * mid - n) <= epsilon:
            return mid
        elif mid * mid < n:
            low = mid
        else:
            high = mid        
    return (low + high) / 2
  
input_str = input("請輸入實數和計算精度： ")
n_str, epsilon_str = input_str.split(',')
n = float(n_str)
epsilon = float(epsilon_str)
sqrt_custom = sqrt_binary(n, epsilon)
sqrt_math = math.sqrt(n)

print(f"{sqrt_custom:.8f}")
print(f"{sqrt_math:.8f}")

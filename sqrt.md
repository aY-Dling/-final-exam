# 南華大學Python程式設計-期中報告
11124208王品雯、11124209蔡岱伶

# ex-4題目:
設計一個用二分法計算一個大於或等於 0 的實數 n 的平方根的函數sqrt_binary(n) 
實數 n和計算精度控制由使用者在同一行內輸入，用逗號進行分隔，輸出結果保留8位小數 
當(abs(x * x - n) )小於或等於設定的精度時，近似認為 x * x == n
註：初始區間取[0,n+0.25]

# 程式碼如下:
## 導入math庫以便使用math.sqrt函數
import math

def sqrt_binary(n, epsilon):
## 初始區間設定為[0, n+0.25]
    low = 0
    high = n + 0.25
## 使用二分查找法求平方根，當區間的長度大於精度時繼續迭代
    while high - low > epsilon:
## 計算區間的中點
        mid = (low + high) / 2
## 如果中點的平方與n的差值在精度範圍內，返回中點
        if abs(mid * mid - n) <= epsilon:
            return mid
## 如果中點的平方小於n，移動下界
        elif mid * mid < n:
            low = mid
## 如果中點的平方大於n，移動上界
        else:
            high = mid
    
## 返回中點，作為近似的平方根
    return (low + high) / 2

## 讀取用戶輸入的字串，用戶輸入格式應為"n,epsilon"
input_str = input("請輸入實數和計算精度： ")
## 將輸入字串以逗號為分隔符分割成兩個部分
n_str, epsilon_str = input_str.split(',')
## 將分割出的字串轉換為浮點數
n = float(n_str)
epsilon = float(epsilon_str)

## 使用自定義的二分法函數計算平方根
sqrt_custom = sqrt_binary(n, epsilon)

## 使用math庫的sqrt函數計算平方根
sqrt_math = math.sqrt(n)

## 輸出結果，保留8位小數
print(f"{sqrt_custom:.8f}")  # 輸出自定義函數計算的平方根
print(f"{sqrt_math:.8f}")  # 輸出math.sqrt函數計算的平方根

# 程式截圖:
![ex-4二分法求平方根截圖]()

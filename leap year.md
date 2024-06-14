# 南華大學Python程式設計-期中報告
11124208王品雯、11124209蔡岱伶、11124237朱瓊月
# ex-3題目:
寫一個程式用來判斷使用者輸入的年份是不是閏年，如果是輸出“True”，如果不是輸出“False”。
# 程式碼如下:
## 定義函數leap，參數為year，用來判斷是否為閏年
def leap(year):
    ## 如果年份能被400整除 或 被4整除但不能被100整除 是閏年
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        ## 如果符合條件，返回True，表示是閏年
        return True  
    else:
        ## 否則返回False，表示不是閏年
        return False
## 提示使用者輸入年份，並將輸入值轉換為整數
year = int(input())
## 呼叫leap函數，傳入輸入的年份，並將結果打印出來
print(leap(year))

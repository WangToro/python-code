y = input('請輸入公元年: ')
y = int(y)

def is_leap(year):
     if ((y % 4 == 0 and y % 100 != 0) or (y % 400== 0 and y % 3200 != 0)): 
        return True
     else:
        return False


print(is_leap(y))
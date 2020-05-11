#<------------------------------------------------------->
def cul(a, p, b):  #四則計算機函數
    if p == '+':
        ans = a + b
    elif p == '-':
        ans = a - b
    elif p == '*':
        ans = a * b
    elif p == '/':
        ans = a / b
    else:
        print('請輸入四則運算')
    return ans
#<------------------------------------------------------->
def cul2(a, p, b):#函數計算機函數
    if p == 1:
        ans = abs(a)
    elif p == 2:
        ans = max(a, b)
    elif p == 3:
        ans = min(a, b)
    return ans
#<------------------------------------------------------->
#功能選擇
print('四則計算機=1', '函數計算機=2', end='')
function = int(input('請輸入需要的功能'))
#<------------------------------------------------------->
while function == 1:#四則計算機介面
        a = int(input('數1='))
        p = input('請輸入運算符號(若想退出此功能請在此輸入exit)')
        b = int(input('數2='))
        ans = cul(a, p, b)
        print('答案是%2d' % (ans))
        print('要改用函數計算機嗎?')
        print('輸入1繼續', '輸入2更改')
        function = int(input())
#<------------------------------------------------------->
while function == 2:#函數計算機介面
        a = int(input('a='))
        b = int(input('b='))
        print('我想算出')
        print('a的絕對值=1')
        print('a,b的最大值=2')
        print('a,b的最小值=3')
        print('重新設定=4')
        p = int(input())
        ans = cul2(a, p, b)
        print('答案是%2d' % (ans))
        print('要改用四則計算機嗎?')
        print('輸入2繼續', '輸入1更改') 
        function = int(input())
#<------------------------------------------------------->
#<------------------------------------------------------->
def cul(a, b, p):#計算機函數
    if p == '+':
        ans = a + b
    elif p == '-':
        ans = a - b
    elif p == '*':
        ans = a * b
    elif p == '/':
        ans = a / b
    elif p == '1':
        ans = abs(a)
    elif p == '2':
        ans = max(a, b)
    elif p == '3':
        ans = min(a, b)
    else:
        print('請輸入四則運算或想求出的值')
    return ans  #返回值
#<------------------------------------------------------->
print('請輸入數字')#計算機介面
a = int(input('數1='))
b = int(input('數2='))
print('請輸入運算符號或想求出的值(若想退出此功能請在此輸入exit)')
print('a的絕對值=1')
print('a,b的最大值=2')
print('a,b的最小值=3')
print('重新設定=4')
p = input()
ans = cul(a, b, p)#呼叫函數
print('答案是%2d' % (ans))
#<------------------------------------------------------->
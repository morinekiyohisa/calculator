switch = True
#<------------------------------------------------------->
def calculate(a, b, p):#計算函數
    if p == '+':#四則運算
        ans = a + b
    elif p == '-':
        ans = a - b
    elif p == '*':
        ans = a * b
    elif p == '/':
        ans = a / b
#<------------------------------------------------------->
    elif p == '1':#階乘
        if a < 0:
            print('抱歉，負數没有階乘')
        elif a == 0:
            print('0 的階乘為 1')
        else:
            ans = 1
            for i in range(1,a + 1):
                ans = ans*i
#<------------------------------------------------------->             
    elif p == '2':#平方
        ans = a**b
    else:
        print('請輸入四則運算或想求出的值')
    return ans  #返回值
#<------------------------------------------------------->
while switch is True:
    print('請輸入數字')#計算機介面
    a = int(input('數1='))
    b = int(input('數2='))
    print('請輸入運算符號或想求出的值(若想退出此功能請在此輸入exit)')
    print('求a的x階乘=1')
    print('求a的x次方=2 數字2為次方數')
    print('重新設定=3')
    p = input()
    if p == '3':
      continue
    ans = calculate(a, b, p)#呼叫函數
    print('答案是%2d' % (ans))
#<------------------------------------------------------->

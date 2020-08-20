n = float(input())
txt = str('')

if n % 4 == 0 :
    txt = txt + 'Fizz'
if n % 7 == 0 : 
    txt = txt + 'Buzz'
    
print(txt)

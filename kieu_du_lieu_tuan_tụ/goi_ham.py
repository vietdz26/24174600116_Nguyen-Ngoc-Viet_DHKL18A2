def q():
    s = '-- inside f()'
    print(s)
print('before calling f()')
q()
print('after callung f()')

def f(qty , item , price):
    print(f'{qty} {item} cost ${price:.2f}')
f(6 , 'bananas' , 1)


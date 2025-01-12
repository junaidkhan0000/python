'''def Marvel(name, char):#formal argument
    print(f"name={name}")
    print(f"character={char}")
Marvel("RDJ", "Iron Man")    #actual arguments
'''
'''
def web_page(page= 'page not found'):
    print(page)
web_page('opening hotstar....')
'''
'''
def f():
    return 10
def g():
    return 7+f()
def h():
    return 5*g()
result=f()+g()+h()
print(result)
'''
def sum_of_n(a):
    if a==1:
        return 1
    else:
        return a+sum_of_n(a-1)
n = int(input('Enter a number: '))
print(sum_of_n(n))
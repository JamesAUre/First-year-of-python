def silly():
    x = 'ping'
    def g():
        print(x)
    x = 'pong'
    def f(x):
        print (x)

    g()
    f(x)

silly()
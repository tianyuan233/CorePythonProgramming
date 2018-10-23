class P():
    def foo(self):
        print('P-foo()')


class Q(P):
    def foo(self):
        print('Q-foo()')


q = Q()
q.foo()

#输出
#Q-foo()

#原因
#尽管Q继承了P的foo方法，但是因为Q定义了自己的foo方法，所以P中的foo()方法被覆盖了

#问题：
#怎么在子类中调用被覆盖的父类方法呢？

#代码


class M():
    def __init__(self):
        print('create M')
    def foo(self):
        print('M-foo()')


class N(M):
    def __init__(self):
        print('create N')
    def foo(self):
        #TODO: super()
        super(N,self).foo()

n = N()
n.foo()

#注意
#当从一个带有 __init__()的类派生时，
# 如果子类没有__init__(),他将会被继承并自动调用
# 但是如果在子类中覆盖了 __init__()， 子类被实例化时将不会调用基类的__init__()

#调用基类__init__()的方法：


class X():
    def __init__(self):
        print('create X')

class Y(X):
    def __init__(self):
        super(Y, self).__init__()
        print('create Y')


y = Y()


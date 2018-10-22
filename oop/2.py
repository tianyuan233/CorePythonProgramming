# # 类的数据属性
# class C():
#     foo = 100


# print(C.foo)


class MyClass():
    #类属性
    version = '1.0'
    def __init__(self,x,y):
        #x,y是实例属性
        self.x = x
        self.y = y

    def myMethod(self):
        print(self.version)

# print(dir(MyClass))
# print(MyClass.__dict__)

mc = MyClass(1,2)

print(mc.x)
print(mc.y)
# class Cat():  # 没有继承,定义时类名后小括号可以省
class Cat:  # 没有继承,定义时类名后小括号可以省
    """这是一个猫类"""

    # __init__ 构造函数
    def __init__(self):  # 使用__init__初始化方法,定义属性
        print("自动调用初始化方法")
        # 构造时添加属性成员
        # self.属性名 = 属性的初始值
        self.name = "Tom"

    # 成员函数
    def eat(self):  # 定义方法
        print("%s 爱吃鱼" % self.name)


# 使用类名()创建对象的时候，会自动调用初始化方法 __init__
tom = Cat()
tom.eat()

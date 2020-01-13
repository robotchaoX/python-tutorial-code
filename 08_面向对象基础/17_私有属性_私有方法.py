class Women:
    def __init__(self, name):
        # 公有属性
        self.name = name
        # 私有属性
        self.__age = 18  # __两下划线开头__私有属性

    # 公有方法
    def showAge(self):
        print("我的年龄是 %d" % self.__age)  # 内部方法可以调用私有属性

    # 私有方法
    def __secret(self):  # __两下划线开头__私有方法
        # print("我的年龄是 %d" % self.age)
        print("我的年龄是 %d" % self.__age)  # 内部方法可以调用私有属性
        # 对象内部的方法可直接访问私有属性和方法


xiaofang = Women("小芳")

# 公有属性
print("print .name", xiaofang.name)  # 外部可直接调用对象共有属性和方法
# 公有方法
xiaofang.showAge()

# 私有属性，在外界不能够被直接访问
# print("print .__age", xiaofang.__age)  # 外部不能直接调用对象私有属性和方法

# 私有方法，同样不允许在外界直接访问
# xiaofang.__secret()  # 外部不可直接调用私有方法

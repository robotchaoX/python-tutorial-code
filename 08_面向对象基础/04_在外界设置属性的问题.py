# class Cat():  # 没有继承,定义时类名后小括号可以省
class Cat:  # 没有继承,定义时类名后小括号可以省
    """这是一个猫类"""

    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)


# 创建猫对象
tom = Cat()

# 可以使用　.属性名　利用赋值语句就可以了
# tom.name = "Tom"

tom.eat()
tom.drink()
# 在使用了 属性成员 后才添加 属性
tom.name = "Tom"  # 错误

# 定义一个布尔型变量 is_employee，编写代码判断是否是本公司员工
is_employee = False

# 如果不是提示不允许入内
# 在开发中，通常希望某个条件不满足时，执行一些代码，可以使用 not
# 另外，如果需要拼接复杂的逻辑计算条件，同样也有可能使用到 not
if not is_employee:  # not
    print("非本公司人员，请勿入内")

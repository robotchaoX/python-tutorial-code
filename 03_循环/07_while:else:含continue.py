i = 0
while i < 5:
    # continue 某一条件满足时，不执行后续重复的代码,提前进行下一次循环
    if i == 3:
        # 注意：在循环中，如果使用 continue 这个关键字
        # 在使用关键字之前，需要确认循环的计数是否修改，
        # 否则可能会导致死循环
        i += 1
        print("continue跳过了 i==3 ")
        continue  # 跳到while
    print(i)
    i += 1
# while正常结束循环才会执行else语句,否则跳过,不执行,
# while中间有break退出,则不执行else语句
# while中间有continue是正常结束,执行else语句
else:
    # 3. 正常结束循环才会执行else语句
    print("正常结束循环才会执行else语句，i = %d" % i)

# 4. 观察一下，循环结束后，计数器 i 的数值是多少
print("continue跳过了i==3,不执行else, i = %d" % i)

# # 输入输出
# name = input()
# print(name)

# # 改变分隔符
# print(1,2,3,sep="-")

# # 改变结束符
# print("hello", end="")

##############################################################

# 获取所有关键字
# import keyword

# def getKeyWord():
#     kw = keyword.kwlist
#     print(kw)

# getKeyWord()

"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""
##############################################################

# s1="hello"
# s2="hello"

# print(id(s1))
# print(id(s2))

# print(type("hello"))

##############################################################

# print(6 / 4)
# print(6 // 4)
# print(3 ** 2)

# num = 100
# num /= 10
# print(num)

# num //= 4
# print(num)

# print(1 == 1)

# result = True and (1==1)
# print(result) 

# result = False or (1==1)
# print(result) 


# result = not (1==1)
# print(result) 

# print('a' in "abc")
# print(0 in [1,2,3,4,5])
# print(0 not in [1,2,3,4,5])

# s1="hello" * 1000
# s2="hello" * 1000

# # s1和s2存储的是"hello"的地址
# print(id(s1))
# print(id(s2))

# print(s1 == s2)
# print(s1 is s2)
# print(s1[0])

##############################################################

# s = "hello world"
# # 统计字符串的字符个数
# print(len(s))
# # 统计字符串中"o"的个数
# print(s.count("o"))
# # 返回字符所在的下标
# print(s.index("o"))
# # 从右侧查找
# print(s.rindex("o")) 
# # 成功：返回所在下标，失败：返回-1
# print(s.find("o")) 
# print(s.find("a")) 
# print(s.rfind("o")) 
# 替换字符 1：替换次数
# print(s.replace("o","a",1))

# url = "https://www.ceshiren.com"
# # 是否以指定字符串开头
# print(url.startswith("https://"))
# # 是否以指定字符串结尾
# print(url.endswith(".com"))
# # 判断字符串是否都是字母
# print(url.isalpha())
# # 判断字符串是否都是数字
# print(url.isdigit())
# # 至少有一个字符，并且所有字符都是字母或数字
# print("a1".isalnum())
# # 只包含空格
# print(" ".isspace())
# # 字符串中的字符都是大写
# print("AAA".isupper())
# print("Aa".isupper())
# # 字符串中的字符都是小写
# print("aaa".islower())
# print("Aa".islower())
# # 首字符是大写
# print("User".istitle())
# print("user".istitle())

# # 把字符串的第一个字符转换为大写
# print("hello World".capitalize())
# # 把字符的每个单词转换为以大写开始，其余字母为小写
# print("hello World".title())
# # 转换 string 中的小写字母为大写
# print("hello World".upper())
# # 转换 string 中的小写字母为小写
# print("hello World".lower())


# # 原字符串居中,并使用空格填充至长度 width 的新字符串，如果指定fillchar参数，则使用指定字符填充，fillchar参数长度只能为1
# print("|"+"hogworts".center(20) + "|")
# print("|"+"hogworts".center(5) + "|")
# print("|"+"hogworts".center(20, "-") + "|")
# # 左对齐,并填充至长度 width 的新字符串
# print("|"+"hogworts".ljust(20) + "|")
# print("|"+"hogworts".ljust(5) + "|")
# print("|"+"hogworts".ljust(20, "-") + "|")
# # 原字符串右对齐,并填充至长度 width 的新字符串
# print("|"+"hogworts".rjust(20) + "|")
# print("|"+"hogworts".rjust(5) + "|")
# print("|"+"hogworts".rjust(20, "-") + "|")

# # 删除 string 左右两侧的空白字符, 如果指定chars参数，则删除左右两侧指定的字符
# print("|" + "  hogworts  " + "|")
# print("|" + "  hogworts  ".strip() + "|")
# print("|" + "  hogworts".strip() + "|")
# print("|" + "hogworts  ".strip() + "|")
# print("|" + "  h o g w o r t s  ".strip() + "|")
# print("|" + "bachogwortsabc".strip("cba") + "|")
# # lstrip() 删除 string 左边的空白字符

# split() 以 sep 为分隔符分割 string，如果指定 maxsplit 参数，则仅分割 maxsplit次

# print("This is Hogworts".partition("is"))
# print("This is Hogworts".partition("iss"))

# print("".join(("a","b","c")))
# print("-".join(("a","b","c")))
# print("->".join(("a","b","c")))
# print("->".join(["a","b","c"]))
# print("->".join({"a","b","c"}))
# print("->".join({"a":"A","b":"B","c":"C"}))

# s = "abcdefg"

# 普通切片
# print(s[0: 2])
# # 省略范围
# print(s[0:])
# print(s[: 2])
# print(s[:])
# 指定步长
# print(s[::1])
# print(s[::2])
# 负下标
# print(s[-3: -1])
# # 负步长
# print(s[-1: -3: -1])
# # 逆序
# print(s[::-1])

""" 示例："""
# story = "Once upon a time, in a land far away, lived a brave knight named Arthur."

# # 统计故事中的单词数量
# word_count = len(story.split())
# print("单词数量:", word_count)

# # 查找主人公的名字在故事中的位置
# hero_name = "Arthur"
# hero_position = story.find(hero_name)
# print("主人公姓名在故事中的位置:", hero_position)

# # 将主人公的名字替换为你的名字
# your_name = "Alice"
# new_story = story.replace(hero_name, your_name)
# print("替换名字后:", new_story)

# # 将故事改写为大写和小写形式
# uppercase_story = story.upper()
# lowercase_story = story.lower()
# print("大写:", uppercase_story)
# print("小写:", lowercase_story)

##############################################################


# t1 = (1,3,2)
# print(t1)
# print(type(t1))

# l = [1,2,3,4,5]
# print(l)
# print(l[0])

# # 获取列表元素个数
# length = len(l)
# print(length)

# 统计查找操作
# count(value) 在列表中统计参数 value 出现的次数

# l = [1,2,3,4,5,1,2,3,3]
# print(l.count(3))
# index(value, start, stop) 在列表中查找参数 value 第一次出现的下标位置，如果给定范围则只在范围内查找，如果查找目标不存在则抛出错误。

# l = [1,2,3,4,5,1,2,3,3]
# print(l.index(3))
# print(l.index(3,5,10))

# l.append(10)


# # keys() 用来获取字典中所有的 key, 保存到一个列表中，并以 dict_keys类型返回
# stu = {'name': 'Tom', 'age': 23, 'gender': 'male', 'address': 'BeiJing'}
# ks = stu.keys()
# print(ks)

# # values() 用来获取字典中所有的value, 保存到一个列表中，并以 dict_values 类型返回
# stu = {'name': 'Tom', 'age': 23, 'gender': 'male', 'address': 'BeiJing'}
# ks = stu.values()
# print(ks)

# # items() 用来获取字典中所有的键值对，每一个元素键值对都以一个元组保存，将所有元素元组保存到一个列表中，并以 dict_items 类型返回
# stu = {'name': 'Tom', 'age': 23, 'gender': 'male', 'address': 'BeiJing'}
# ks = stu.items()
# print(ks)


# # get(key, default) 用来获取key对应的值，如果指定的key不存在，则返回默认值
# stu = {'name': 'Tom', 'age': 23, 'gender': 'male', 'address': 'BeiJing'}
# # print(stu["name"])
# # print(stu["hobby"])
# print(stu.get("name"))
# print(stu.get("hobby"))
# print(stu.get("hobby","无数据"))

# stu = {'name': 'Tom', 'aa': 'Tom', 'gender': 'male', 'address': 'BeiJing'}
# print(stu.get("aa"))

# s = {1, 2, 3}
# s.add(4)
# s.remove(4)

# # 是否为子集
# print(s.issubset({1, 2, 3}))
# print(s.issubset({1, 2, 3, 4}))
# print(s.issubset({3, 4, 5}))

# # 判断是否为真子集
# print(s < {1, 2, 3})
# print(s < {1, 2, 3, 4})
# print(s < {3, 4, 5})

# 并集
# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}
# s3 = {5, 6, 7, 8}
# print(s1.union(s2))
# print(s1.union(s2,s3))
# # 也可以使用 | 进行集合并集运算
# print(s1 | s2)
# print(s1 | s2 | s3)

# 交集
# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}
# s3 = {5, 6, 7, 8}
# print(s1.intersection(s2))
# print(s1.intersection(s2, s3))
# print(s1.intersection(s3))
# print("*" * 10)
# # 也可以使用 & 进行集合交集运算
# print(s1 & s2)
# print(s1 & s2 & s3)
# print(s1 & s3)

# 差集
# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}
# s3 = {5, 6, 7, 8}
# print(s1.difference(s2))
# print(s1.difference(s2, s3))
# print(s1.difference(s3))
# print("*" * 10)
# # 也可以使用 - 进行集合差集运算
# print(s1 - s2)
# print(s1 - s2 - s3)
# print(s1 - s3)

# requestMethods = {
#                     "get": "用于获取服务器上的资源，通过在URL中传递参数来发送请求。",
#                     "post": "用于向服务器提交数据，一般用于创建新的资源或进行修改操作。",
#                     "put": "用于更新服务器上的资源，一般用于修改已存在的资源的全部内容。",
#                     "delete": "用于删除服务器上的资源。"
#                 }
# for method in requestMethods:
#     print(method)

# requestMethods = {
#                     "get": "用于获取服务器上的资源，通过在URL中传递参数来发送请求。",
#                     "post": "用于向服务器提交数据，一般用于创建新的资源或进行修改操作。",
#                     "put": "用于更新服务器上的资源，一般用于修改已存在的资源的全部内容。",
#                     "delete": "用于删除服务器上的资源。"
#                 }
# for method in requestMethods.values():
#     print(method)

# requestMethods = {
#                     "get": "用于获取服务器上的资源，通过在URL中传递参数来发送请求。",
#                     "post": "用于向服务器提交数据，一般用于创建新的资源或进行修改操作。",
#                     "put": "用于更新服务器上的资源，一般用于修改已存在的资源的全部内容。",
#                     "delete": "用于删除服务器上的资源。"
#                 }
# for item in requestMethods.items():
#     print(f"请求方式【 {item[0]} 】的作用为：【 {item[1]} 】")

# requestMethods = {
#                     "get": "用于获取服务器上的资源，通过在URL中传递参数来发送请求。",
#                     "post": "用于向服务器提交数据，一般用于创建新的资源或进行修改操作。",
#                     "put": "用于更新服务器上的资源，一般用于修改已存在的资源的全部内容。",
#                     "delete": "用于删除服务器上的资源。"
#                 }
# for key, value in requestMethods.items():
#     print(f"请求方式【 {key} 】的作用为：【 {value} 】")

# s = "abcdefg"

# # print(s[-1 - 1])
# for i in range(len(s)):
#     print(-i)

# nums = list(range(1, 10))
# print(nums)

# def printMsg(n,msg):
#     for i in range(n):
#         print(i)
# printMsg(5)10

# 正确使用位置参数
# printMsg(5, "Hogworts")
# 错误使用位置参数10

# 10进制整数转换2进制，并字符串打印出结果
# result = ""
# number = int(input("输入数字："))
# while number != 0:
#     temp = number % 2
#     number = number // 2
#     result = str(temp) + result
# print(result)


# # 阶乘
# def jc(number):
#     if number == 1 or number == 0:
#         return 1
#     return number * jc(number-1)


# # 斐波那契数列
# def fb(number):
#     if number < 1:
#         return 0
#     elif number == 1 or number == 2:
#         return 1
#     return fb(number-1) + fb(number-2)
    
# if __name__ == "__main__":
#     number = int(input("输入数字："))
#     print("结果：", jc(number))

#     print("结果：", fb(number))


# def out_func():
#     out_n = 100
#     def inner_func():
#         print(out_n)
#     out_n = 200
#     return inner_func

# if __name__ == '__main__':
#     of1 = out_func()
#     of2 = out_func()

#     of1()
#     of2()



# # 接收装饰器参数的函数
# # 参数一：以字符串形式接收被装饰函数的参数列表，需要与被装饰函数参数名保持一致，例："a,b,c"
# # 参数二：以[(),(),()] 形式传入驱动数据。
# def decorator_args(vars, datas):
#     def decorator(func):
#         # 将字符串参数分割备用
#         v_keys = vars.split(",")
#         # 定义保存 [{},{},{}] 形式的数据
#         new_datas = []
#         # 遍历数据，取出一组元素数据
#         for item in datas:
#             # 定义一个新字典，用来保存 变量名与传入数据组成的字典
#             d_item = {}
#             # 使用 zip 函数，同时遍历两个元组，变量名做为key, 元素数据做为value
#             for k, v in zip(v_keys, item):
#                 # 将 变量名和值对应保存到字典中
#                 d_item[k] = v
#             # 将组合好的字典追加到新数据中备用
#             new_datas.append(d_item)
#         def inner(*args, **kwargs):
#             return func(*args, **kwargs)
#         # 遍历新数据，取出元素字典
#         for item in new_datas:
#             # 将字典中的数据解包传给内函数
#             inner(**item)
#         return inner
#     return decorator

# # 数据驱动数据
# data = [(1,2,3),(4,5,6),(7,8,9)]

# # 装饰器传参
# @decorator_args("a,b,c", data)
# def show(a,b,c):
#     print(a,b,c)




# file = open("D:\c++Code\TestBible\BasicConcepts\Python\python.md","r")
# try:
#     print("hello" * 100)
# except IOError as err:
#     print("文件不能写入", err)
# except NameError:
#     print("标识符没有定义")
# except ZeroDivisionError:
#     print("除数不能为0")
# except IndexError:
#     print("下标越界了")
# except Exception:
#     print("程序运行出错，请检查代码")
# finally:
#     print("文件已关闭")
#     file.close()



# class Student:
#     def __init__(self,name, age): # 构造函数
#         self.name = name
#         self.age = age

# s1 = Student("Tom", 22)
# s2 = Student("Jack", 23)

# print(s1.name)
# print(s1.age)

# print(s1.name)
# print(s1.age)


# class Student:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"Name: {self.name} -- Age: {self.age}"
    
# s1 = Student("Tom", 22)
# s2 = Student("Jack", 23)

# print(s1)
# print(s2)

# 定义一个饮水机类
# class WaterDispenser:
#     # 剩余水量
#     surplus_water = 1500
#     # 出水口
#     def water_outlet(self, n):
#         WaterDispenser.surplus_water -= n
#         print("剩余水量：", WaterDispenser.surplus_water)

# wd1 = WaterDispenser()
# wd2 = WaterDispenser()

# wd1.water_outlet(100)
# print(wd1.surplus_water)
# wd2.water_outlet(200)
# print(wd2.surplus_water)
# print(WaterDispenser.surplus_water)

# import datetime
# class Utils:
#     now = datetime.datetime.now()

#     @classmethod
#     def current_date_time(cls):
#         return cls.now

#     @classmethod
#     def current_date(cls):
#         return cls.now.strftime("%Y-%m-%d")

#     @classmethod
#     def current_time(cls):
#         return cls.now.strftime("%H-%M-%S")

#     @classmethod
#     def getYear(cls):
#         return cls.now.year

#     @classmethod
#     def getMonth(cls):
#         return cls.now.month

#     @classmethod
#     def getDay(cls):
#         # 调用类方法
#         print(Utils.current_date_time())
#         return cls.now.day
    
#     def show(self) -> None:
#         print("show func")

# u1 = Utils()
# u1.show()
# print(u1.current_date_time())
# print("-------------------------")
# print(Utils.current_date_time())
# print(Utils.current_date())
# print(Utils.current_time())
# print(Utils.getYear())
# print(Utils.getMonth())
# print(Utils.getDay())


# class A(object):
#     def __init__(self):
#         # 公有属性
#         self.a = 10
#         # 保护属性
#         self._b = 20
#         # 私有属性
#         self.__c = 30

#     # 公有方法
#     def show(self):
#         # 在类中使用公有属性
#         print(f"A: {self.a}")
#         # 在类中使用保护属性
#         print(f"B: {self._b}")
#         # 在类中使用私有属性
#         print(f"C: {self.__c}")
#         # 在类中使用保护权限的方法
#         self._display()
#         # 在类中使用私有方法
#         self.__info()


#     # 保护权限的方法
#     def _display(self):
#         print(f"B: {self._b}")

#     # 私有权限的方法
#     def __info(self):
#         # 在类中使用私有属性
#         print(self.__c)
# obj = A()
# # 在类外使用公有属性
# print(obj.a)
# # 在类外无法使用保护仅限的属性（不建议这样使用）
# print(obj._b)
# # 在类外使用私有属性，访问失败
# # print(obj.__c)
# # 在类外使用公有方法
# obj.show()
# # 在类外无法使用保护权限的方法（不建议这样使用）
# obj._display()
# # 在类外访问私有方法，访问失败
# # obj.__info()

# 中医
# class Father:
#     def cure(self):
#         print("使用中医方法进行治疗。。。")

# # 西医
# class Son(Father):
#     def cure(self):
#         print("使用西医方法进行治疗。。。")

# # 兽医
# class AnimalDoctor:
#     def cure(self):
#         print("使用兽医方法进行治疗。。。")

# # 患者
# class Patient:
#     def needDoctor(self, doctor):
#         doctor.cure()


# if __name__ == '__main__':
#     oldDoctor = Father()
#     littleDoctor = Son()
#     animalDoctor = AnimalDoctor()

#     patient = Patient()

#     patient.needDoctor(oldDoctor)
#     patient.needDoctor(littleDoctor)
#     patient.needDoctor(animalDoctor)

# 中医
class Father:
    def cure(self):
        print("使用中医方法进行治疗。。。")

# 西医
class Son(Father):
    def cure(self):
        print("使用西医方法进行治疗。。。")

# 兽医
class AnimalDoctor:
    def cure(self):
        print("使用兽医方法进行治疗。。。")

# 患者
class Patient:
    def needDoctor(self, doctor):
        # if isinstance(doctor, Father):
        #     doctor.cure()
        # else:
        #     print("此大夫医疗方法不适用病人。。。")

        if issubclass(doctor.__class__, Father):
            doctor.cure()
        else:
            print("此大夫医疗方法不适用病人。。。")


if __name__ == '__main__':
    oldDoctor = Father()
    littleDoctor = Son()
    animalDoctor = AnimalDoctor()

    patient = Patient()

    patient.needDoctor(oldDoctor)
    patient.needDoctor(littleDoctor)
    patient.needDoctor(animalDoctor)
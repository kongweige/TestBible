**变量**

定义两个相同的字符串时，Python会尝试优化内存以节省空间，对于相同的字符串常量，通常会共享同一块内存空间。这种优化称为字符串驻留（string interning）
```python

s1="hello"
s2="hello"

# s1和s2存储的是"hello"的地址
print(id(s1))
print(id(s2))
```

**成员运算符（in/not in）**
```python
print("a" in "abc")
print(0 in [1,2,3,4,5])
print(0 not in [1,2,3,4,5])
```

**身份运算符（is/is not）**
* 整数池：
  * 程序运行时预先创建一些整数对象，将其保存到整数池中。创建对象时，可以重用已存在的对象，而不是重新创建新的对象。减少了内存开销
* 字符串池：
  * 字符串池是一个缓存区，保存所有共享相同内容的字符串对象，创建新字符串对象时，编译器会先检查池中是否已经存在相同内容的字符串对象，如果存在，则直接重用已有的对象，减少内存开销
```python
s1="hello" * 1000
s2="hello" * 1000

3print(id(s1))
print(id(s2))

print(s1 == s2)
print(s1 is s2)

# 根据下标获取
print(s1[0])
```
**字符串**
* 查找统计替换类
```python
s = "hello world"
# 统计字符串的字符个数
print(len(s))
# 统计字符串中"o"的个数
print(s.count("o"))
# 返回字符所在的下标
print(s.index("o"))
# 从右侧查找
print(s.rindex("o")) 
# 成功：返回所在下标，失败：返回-1
print(s.find("o")) 
print(s.find("a")) 
print(s.rfind("o")) 
# 替换字符 1：替换次数
print(s.replace("o","a",1))
```

* 字符串判断类
```python
url = "https://www.ceshiren.com"
# 是否以指定字符串开头
print(url.startswith("https://"))
# 是否以指定字符串结尾
print(url.endswith(".com"))
# 判断字符串是否都是字母
print(url.isalpha())
# 判断字符串是否都是数字
print(url.isdigit())
# 至少有一个字符，并且所有字符都是字母或数字
print("a1".isalnum())
# 只包含空格
print(" ".isspace())
# 字符串中的字符都是大写
print("AAA".isupper())
print("Aa".isupper())
# 字符串中的字符都是小写
print("aaa".islower())
print("Aa".islower())
# 首字符是大写
print("User".istitle())
print("user".istitle())
```
* 字符串转换类
```python
# 把字符串的第一个字符转换为大写
print("hello World".capitalize())
# 把字符的每个单词转换为以大写开始，其余字母为小写
print("hello World".title())
# 转换 string 中的小写字母为大写
print("hello World".upper())
# 转换 string 中的小写字母为小写
print("hello World".lower())
```
* 字符对齐类
```python
# 原字符串居中,并使用空格填充至长度 width 的新字符串，如果指定fillchar参数，则使用指定字符填充，fillchar参数长度只能为1
print("|"+"hogworts".center(20) + "|")
print("|"+"hogworts".center(5) + "|")
print("|"+"hogworts".center(20, "-") + "|")
# 左对齐,并填充至长度 width 的新字符串
print("|"+"hogworts".ljust(20) + "|")
print("|"+"hogworts".ljust(5) + "|")
print("|"+"hogworts".ljust(20, "-") + "|")
# 原字符串右对齐,并填充至长度 width 的新字符串
print("|"+"hogworts".rjust(20) + "|")
print("|"+"hogworts".rjust(5) + "|")
print("|"+"hogworts".rjust(20, "-") + "|")
```
* 字符串去除空白类
```python
# 删除 string 左右两侧的空白字符, 如果指定chars参数，则删除左右两侧指定的字符
print("|" + "  hogworts  " + "|")
print("|" + "  hogworts  ".strip() + "|")
print("|" + "  hogworts".strip() + "|")
print("|" + "hogworts  ".strip() + "|")
print("|" + "  h o g w o r t s  ".strip() + "|")
print("|" + "bachogwortsabc".strip("cba") + "|")
# lstrip() 删除 string 左边的空白字符
```
* 字符串分割
```python
# split() 以 sep 为分隔符分割 string，如果指定 maxsplit 参数，则仅分割 maxsplit次
print("a-b-c-d".split("-"))
print("a-b-c-d".split("-", 2))
print("a--b-c-d".split("-"))
print("a-+b-c-d".split("-+"))
print("a b\tc\nd\re".split())
print("a b c d e".split(" ", 3))
```

* 字符串链接
```python
# 用 string 连接可迭代对象中的所有元素
print("".join(("a","b","c")))
print("-".join(("a","b","c")))
print("->".join(("a","b","c")))
print("->".join(["a","b","c"]))
print("->".join({"a","b","c"}))
print("->".join({"a":"A","b":"B","c":"C"}))
```
* 切片操作
```python
s = "abcdefg"

# 普通切片
print(s[0: 2])
# 省略范围
print(s[0:])
print(s[: 2])
print(s[:])
# 指定步长
print(s[::1])
print(s[::2])
# 负下标
print(s[-3: -1])
# 负步长
print(s[-1: -3: -1])
# 逆序
print(s[::-1])
```
* 字符串格式化

* 元祖
```python
# 元素之间必须加逗号，一个元素也要加
t0 = (1,)
t1 = (1,3,2)
print(t1)
print(type(t1))
```
* 列表
```python
l = [1,2,3,4,5]
print(l)
print(l[0])

# 获取列表元素个数
length = len(l)

# 查找3出现的次数
print(l.count(3))

# 返回3所在的位置下标
print(l.index(3))

# 向列表最后追加元素
l.append(10)

# 在指定下标位置插入
l.insert(0, "A")
print(l)
l.insert(3, "B")
print(l)

# 删除指定下标位置元素
del l[0]
print(l)

# 在列表中删除第一个指定的数据（不是下标）
l.remove(3)
print(l)


# 从列表中取出并删除指定下标位置的元素，默认取出并删除最后一个元素
print(l.pop())
print(l)
print(l.pop(3))
print(l)

# 清空列表
l.clear()
print(l)

```
* 元组和列表的区别
  * 相同点：
    * 元组和列表在python中，都是有序的，可迭代的数据结构
    * 元组和列表都是异构的，都可以存储不同数据类型的元素
  * 不同点：
    * 元组是不可变的，不可以增删改
    * 列表是可变的，可以对列表中的元素进行增删改
    * 相同元素个数的情况下，元组的内存空间更小
* 字典
```python
# 定义字典
d1 = {}
d2 = {"name": "Alice", "age": 25, "gender": "female"}

# 添加和修改
stu = {"name":"Tom", "age": 23, "gender":"male"}
print(stu)
# 添加新元素
stu["address"] = "BeiJing"
print(stu)
# 修改数据
stu["name"] = "Jack"
stu["address"] = "ShangHai"
print(stu)

# 删除元素
stu = {'name': 'Tom', 'age': 23, 'gender': 'male', 'address': 'BeiJing'}
print(stu)
# 删除元素
del stu['age']
print(stu)
del stu['address']
print(stu)
```
* 集合
```python
# 不能使用花括号 {} 来定义一个空集合
s1 = set()
s2 = {}
print(type(s1))
print(type(s2))

# 使用花括号 {}，在内部添加元素，用逗号 , 分隔
my_set = {1, 2, 3, 4, 5}

# 使用内置函数 set() 创建集合
my_set = set([1, 2, 3, 4, 5])

# 集合元素具有唯一性
s = {1,1,1,2,3,4,5,6,6,6,6,6,6,6}
print(s)


s = {1, 2, 3}
s.add(4)
s.remove(4)

# 是否为子集
print(s.issubset({1, 2, 3}))
print(s.issubset({1, 2, 3, 4}))
print(s.issubset({3, 4, 5}))

# 判断是否为真子集
print(s < {1, 2, 3})
print(s < {1, 2, 3, 4})
print(s < {3, 4, 5})
```
* 深浅拷贝
  * 浅拷贝只是创建了一个引用，不同的地址指向同一块内存空间，对数据改变会影响原数据
  * 深拷贝，重新开辟了一块内存空间，与原数据互不影响

* 匹配语句

与C++中的switch区别是case中自带break，如果case 101:匹配后不会继续匹配后面的case
```python
httpCode = int(input("请输入一个HTTP状态码："))

match httpCode:
    case 101:
        print("临时响应")
    case 200:
        print("请求成功")
    case 301:
        print("重定向")
    case 404:
        print("页面找不到")
    case 500:
        print("服务器内部错误")
    case _: 
        # 处理所有其他情况的匹配（相当于默认情况）
        print("无效的状态码")

##################匹配多个值#######################
httpCode = int(input("请输入一个HTTP状态码："))

match httpCode:
    case 100 | 101:
        print("临时响应")
    case 200 | 201 | 203 | 204 | 205:
        print("请求成功")
    case 301 | 304 | 307:
        print("重定向")
    case 401 | 403| 404 | 405:
        print("页面找不到")
    case 500 | 502 | 503:
        print("服务器内部错误")
    case _:
        print("无效的状态码")

##################变量匹配#############################
# point is an (x, y) tuple
x = int(input("x:"))
y = int(input("y:"))
point = (x, y)
match point:
    case (0, 0):
        print("坐标在原点上")
    case (0, y):
        print(f"坐标在Y轴上")
    case (x, 0):
        print(f"坐标在X轴上")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("没有这个坐标点")
```

* while循环
```python
# 循环变量实始化
n = 1
# 循环条件
while n<=100:
    # 数字对7求模为0，则表示该数字是7的倍数
    # 将数字转换为字符串类型，使用成员运算符判断字符7是否在字符串中，检查包含关系
    if n % 7 == 0 or "7" in str(n):
        # 输出满足条件的数字
        print(n)
    # 改变循环变量趋近于结束条件
    n += 1
```

* for循环
```python

# 遍历字符串
s = "Hello Hogworts!"
for c in s:
    print(c)

# 遍历元组
t = (1,2,3,4,5)
for n in t:
    print(n)

# 遍历列表
requestMethods = ["get", "post", "put","delete", "patch", "header", "options",'trace']
for method in requestMethods:
    print(method)

# 遍历字典，默认遍历key
requestMethods = {
                    "get": "用于获取服务器上的资源，通过在URL中传递参数来发送请求。",
                    "post": "用于向服务器提交数据，一般用于创建新的资源或进行修改操作。",
                    "put": "用于更新服务器上的资源，一般用于修改已存在的资源的全部内容。",
                    "delete": "用于删除服务器上的资源。"
                }
for method in requestMethods:
    print(method)

# 遍历字典的key和val
for key, value in requestMethods.items():
    print(f"请求方式 [ {key} ] 的作用为：[ {value} ]")
```
* 推导式
  * 优点：一行代码中完成复杂的生成操作，避免了使用显式的循环和临时变量的繁琐过程。大大减少代码量，并提高编码效率
```python
###########元组推导式##################
# 简单的元组推导式
t1 = (x for x in range(1,10))
# 生成128位ASCII码元组
t2 = (chr(x) for x in range(128))
# 生成100以内能被7整除所有数字的元组
t3 = (x for x in range(100) if x%7==0)
# 生成99乘法表结果元组
t4 = (x*y for x in range(1,10) for y in range(1, x+1))
words = ["apple", "banana", "cherry"]
upper_words = (word.upper() for word in words)

###########列表推导式##################
# 简单的元组推导式
l1 = [x for x in range(1,10)]
# 生成128位ASCII码元组
l2 = [chr(x) for x in range(128)]
# 生成100以内能被7整除所有数字的元组
l3 = [x for x in range(100) if x%7==0]
# 生成99乘法表结果元组
l4 = [x*y for x in range(1,10) for y in range(1, x+1)]
# 将列表中的字符串转换为大写
words = ["apple", "banana", "cherry"]
upper_words = [word.upper() for word in words]

###########字典推导式##################
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {name:len(name) for name in names}

```
* 函数参数
```python
# 指定默认值的形式参数必须放在所有未指定默认值参数的后面，否则会产生语法错误
def show(a, b=2, c):
    print(a, b, c)


######可变位置参数########
# 不确定个数数字求和
def my_sum(*args):
    print(args)
    print(*args)
    print(type(args))
    s = 0
    for i in args:
        s += i

    print(s)
    print("*" * 10)

my_sum(1,2,3)
my_sum(1,2,3,4)
my_sum(1,2,3,4,5)
my_sum(1,2,3,4,5,6)

#######可变关键字参数##############
# 定义可变关键字参数
def print_info(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k,v in kwargs.items():
        print(k, v)
    print("*" * 10)

print_info(Tom=18, Jim=20, Lily=12)
print_info(name="tom",age=22,gender="male",address="BeiJing")
```

* 闭包&装饰器
  * **闭包**：由内函数和外函数组成的一个块，外函数返回内函数的函数引用，内函数可以访问外函数内的变量
    * 保护私有变量：保护了内部的变量，限制外部访问
    * 延迟执行：可以使用闭包来延迟某个函数的执行，将想要延迟的函数作为内函数
  * **装饰器**：本质上是一个闭包函数，能够保证原有函数代码结构不变，为函数增加额外功能
```python
##################通用装饰器#####################
# 做为装饰器名的外函数，使用参数接收被装饰函数的引用
def decorator(func):
    # 内函数的可变参数用来接收被装饰函数使用的参数
    def inner(*args, **kwargs):
        # 装饰器功能代码
        # 调用被装饰函数，并将接收的参数传递给被装饰函数，保存被装饰函数执行结果
        result = func(*args, **kwargs)
        # 返回被装饰函数执行结果
        return result
    # 返回内函数引用
    return inner

##################带参装饰器#####################
def decorator_args(vars, datas):
    def decorator(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner
    return decorator

data = [(1,2,3),(4,5,6),(7,8,9)]
# 装饰器传参
@decorator_args("a,b,c", data)
def show(a,b,c):
    print(a,b,c)
```

* 异常处理
```python
file = open("data.txt","r")
try:
    # 写入数据时可能会有问题
    # file.write("写入的数据")
    # print(a)
    # print(3 / 0)
    # print([][10])
    print("hello" + 100)
except IOError as err:
    print("文件不能写入", err)
except NameError:
    print("标识符没有定义")
except ZeroDivisionError:
    print("除数不能为0")
except IndexError:
    print("下标越界了")
except Exception:
    print("程序运行出错，请检查代码")
finally:
    print("文件已关闭")
    file.close()
```

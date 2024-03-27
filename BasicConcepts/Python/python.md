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


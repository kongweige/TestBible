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


## 命名规范
|类型|规则|
|-------|-------|
|文件|test_开头 或者 _test 结尾|
|类|Test 开头|
|方法/函数|	test_开头|
> 注意：测试类中不可以添加__init__构造函数	
## 测试装置
|类型|规则|
|-------|-------|
|setup_module/teardown_module |全局模块级 |
|setup_class/teardown_class |类级，只在类中前后运行一次 |
|setup_function/teardown_function |函数级，在类外,每个函数执行前后 |
|setup_method/teardown_method |方法级，类中的每个方法执行前后 |	
## 参数化
* 将参数提取出来，每个参数就是一个测试用例

**参数化方式**
```python
@pytest.mark.parametrize("username,password",[["right","right"],["wrong","wrong"]])
def test_param(username,password):
    login(username,password)

############单参数############
search_list = ['appium','selenium','pytest']

@pytest.mark.parametrize('name',search_list)
def test_search(name):
    login(username,password)

############多参数###########
# 数据放在元组中
@pytest.mark.parametrize("test_input,expected",[
    ("3+5",8),("2+5",7),("7+5",12)
])
def test_mark_more(test_input,expected):
    assert eval(test_input) == expected

# 数据放在列表中
@pytest.mark.parametrize("test_input,expected",[
    ["3+5",8],["2+5",7],["7+5",12]
])
def test_mark_more(test_input,expected):
    assert eval(test_input) == expected

###########笛卡尔积###########
# 由近到远执行
@pytest.mark.parametrize("b",["a","b","c"])
@pytest.mark.parametrize("a",[1,2,3])
def test_param1(a,b):
    print(f"笛卡积形式的参数化中 a={a} , b={b}")
```

**标记测试用例**

只执行符合要求的某一部分用例 可以把一个web项目划分多个模块，然后指定模块名称执行
```python
# 标记命令
pytest -s test_mark_zi_09.py -m=str
pytest -s test_mark_zi_09.py -m str
pytest -s test_mark_zi_09.py -m "str"
##################
# filename: test_mark_zi_09.py
@pytest.mark.str
def test_double_str():
    assert 'aa' == double('a')

@pytest.mark.str
def test_double_str1():
    assert 'aa' == double('a')

@pytest.mark.zero
def test_double_zero():
    assert 0 == double(0)

```
**跳过测试用例**
* skip - 始终跳过该测试用例
* skipif - 遇到特定情况跳过该测试用例
* xfail - 遇到特定情况,产生一个“期望失败”输出
```python

# 跳过测试用例
@pytest.mark.skip(reason="代码没实现")

# 代码中添加 跳过代码块
def check_login():
    return True 

def test_function():
    if not check_login():
        pytest.skip("未登录")
    print("end")

################# 条件跳过###########
# 根据测试条件 跳过相应的测试用例
import sys
import pytest

@pytest.mark.skipif(sys.platform =='darwin',reasom="does not run on mac")
def test_case1():
    assert True
@pytest.mark.skipif(sys.platform =='win',reasom="does not run on windows")
def test_case2():
    assert True
```
**测试用例执行方式**
* 执行包下所有的用例：pytest/py.test [包名]
* 执行单独一个 pytest 模块：pytest 文件名.py
* 运行某个模块里面某个类：pytest 文件名.py::类名
* 运行某个模块里面某个类里面的方法：pytest 文件名.py::类名::方法名

**命令行参数**
* —help 
* -x   用例一旦失败(fail/error)，就立刻停止执行
* --maxfail=num 用例达到
* -m  标记用例
* -k  执行包含某个关键字的测试用例
* -v 打印详细日志
* -s 打印输出日志（一般-vs一块儿使用）
* —collect-only（测试平台，pytest 自动导入功能 ）

## 数据驱动
* 将测试数据放到文件当中，通过测试用例执行

**yaml文件**
```python
import yaml

# 读取yaml文件
def get_yaml():
    """
    获取json数据
    :return: 返回数据的结构：[[1, 1, 2], [3, 6, 9], [100, 200, 300]]
    """
    with open('../datas/data.yaml', 'r') as f:
        data = yaml.safe_load(f)
        return data

```
**excel**


**csv**

**json**


## 生命周期管理
**fixture**
```python
# @pytest.fixture()

# 定义了登录的fixture
@pytest.fixtur()
def login():
    print("完成登录")

def test_search():
    print("测试搜索")

# 先执行登录在执行测试用例
def test_cart(login):
    print("测试购物车")
```
* 作用域
    * function	函数级	每一个函数或方法都会调用
    * class	类级别	每个测试类只运行一次
    * module	模块级	每一个.py 文件调用一次
    * package	包级	每一个 python 包只调用一次(暂不支持)
    * session	会话级	每次会话（运行期间）只需要运行一次，会话内所有方法及类，模块都共享这个方法

**yeild**
```python
# @pytest.fixture()

# 定义了登录的fixture
@pytest.fixtur()
def login():
    # setup 操作
    print("完成登录")
    token = "1312313"
    yield token # 相当于return
    # teardown 操作
    print("完成登出")

def test_search():
    print("测试搜索")

# 先执行登录在执行测试用例
def test_cart(login):
    print("测试购物车")
```
**conftest**
* 存放公共数据，如果在文件中要使用conftest中的函数需要将方法加上@pytest.fixture()
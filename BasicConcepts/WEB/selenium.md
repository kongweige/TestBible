|| 自动化测试用例 | 说作用明 |
|-------|-------|-------|
|用例标题|	测试包、文件、类、方法名称|	用例的唯一标识|
|前提条件|	setup、setup_class(Pytest); BeforeEach、BeforeAll（JUnit）	|测试用例前的准备动作，比如读取数据或者driver的初始化|
|用例步骤|	测试方法内的代码逻辑|	测试用例具体的步骤行为|
|预期结果|	assert 实际结果 = 预期结果|	断言，印证用例是否执行成功|
|实际结果|	assert 实际结果 = 预期结果|	断言，印证用例是否执行成功|
|后置动作|	teardown、teardown_class(Pytest); @AfterEach、@AfterAll（JUnit）||

## 浏览器控制
|	|操作|	使用场景|
|-------|-------|-------|
|get|	打开浏览器|	web自动化测试第一步|
|refresh|	浏览器刷新|	模拟浏览器刷新|
|back|	浏览器退回|	模拟退回步骤|
|maximize_window|	最大化浏览器|	模拟浏览器最大化|
|minimize_window|	最小化浏览器|	模拟浏览器最小化|
```python
from selenium import webdriver

def open_browser():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    # 刷新浏览器
    driver.refresh()
    # 退回上一步
    driver.back()
    # 最大化
    driver.maximize_window()
    # 最小化
    driver.minimize_window()

if __name__ == '__main__':
    # 打开浏览器
    open_browser()
```
## 常见控件定位方法
|方式|	描述|
|-------|-------|
|class name|class 属性对应的值|
|css selector（重点）|	css 表达式|
|id（重点）|	id 属性对应的值|
|name（重点）|	name 属性对应的值|
|link text|	查找其可见文本与搜索值匹配的锚元素|
|partial link text|	查找其可见文本包含搜索值的锚元素。如果多个元素匹配，则只会选择第一个元素|
|tag name|	标签名称|
|xpath（重点）|	xpath表达式|
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

def open_browser():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study/frame")

    # ID定位，第一个参数定位方式，第二个参数定位元"素
    web_element = driver.find_element(By.ID,"locate_id")
    print("ID: ",web_element)

    # name定位
    web_element = driver.find_element(By.NAME,"locate")
    print("NAME: ",web_element)

    # CSS表达式定位
    web_element = driver.find_element(By.CSS_SELECTOR,"#locate_id > a > span")
    print("CSS: ",web_element)

    # Xpath定位
    web_element = driver.find_element(By.XPATH,'//*[@id="locate_id"]/a/span')
    print("Xpath: ",web_element)

    # 链接文本定位，元素一定是<a>标签，输入的元素为标签内的文本
    web_element = driver.find_element(By.LINK_TEXT,'元素定位').click() # click() 点击操作
    print("LINK: ",web_element)

if __name__ == "__main__":
    open_browser()
```

## 三种等待
> 加等待的原因：定位某个元素的时候，如果界面还没加载完成，此时需要定位的元素还没加载出来，导致定位不到该元素，发生报错
* 强制(直接)等待: 线程休眠一定时间，等待元素完全加载(不能确定加载时间)
    * 带来的问题：
        * 等待时间过长，降低执行效率
        * 等待时间过短，元素未加载出来，产生错误
* 隐式等待: 设置一个等待时间，轮询查找（默认0.5秒）元素是否出现，如果没出现就抛出异常（只能解决元素查找，不能解决元素交互）
* 显示等待: 在最长等待时间内，轮询，是否满足结束条件
```python
# 强制等待
time.sleep(3)

# 隐式等待
# 隐式等待就是对webdriver的实例对象做一个配置，如果没有设置隐式等待webdriver里面的超时时间属性默认是0
# 隐式等待是全局生效的，在每个find_elenemt动作之前都会执行

# 元素可以找到，使用点击等操作，出现报错
# 界面元素加载是异步的，html加载完成，在加载js、css
# html只关注元素是否存在，交互有js和css决定
driver.implicitly_wait(3)

# WebDriverWait(driver实例, 最长等待时间, 轮询时间).until(结束条件)
WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.ID,"success_btn")))

```
## 定位策略
* 与研发约定的属性优先(class属性： [name='locate'])
* 身份属性 id，name(web 定位)
* 复杂场景使用组合定位：
    * xpath，css
    * 属性动态变化（id，text）
    * 重复元素属性（id，text，class）
    * 父子定位（子定位父）
* js定位
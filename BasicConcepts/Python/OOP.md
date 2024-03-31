* 封装：封装属性和方法，只对外部暴露需要的接口，隐藏内部的实现细节
* 继承：子类继承父类，子类拥有父类的属性和方法，并且可以扩展
* 多态：相同的接口实现不同的功能

* 构造方法
```python
class Student:
    def __init__(self,name, age): # 构造函数
        self.name = name
        self.age = age

s1 = Student("Tom", 22)
s2 = Student("Jack", 23)

print(s1.name)
print(s1.age)

print(s1.name)
print(s1.age)
```
* 类属性(跟c++中的static相似)
  * 所有的实例对象名共享一个类属性
  * 实例对象只能获取类属性的值，不能直接进行修改，只能通过方法进行修改
```python
# 定义一个饮水机类
class WaterDispenser:
    # 剩余水量
    surplus_water = 1500
    # 出水口
    def water_outlet(self, n):
        WaterDispenser.surplus_water -= n
        print("剩余水量：", WaterDispenser.surplus_water)

wd1 = WaterDispenser()
wd2 = WaterDispenser()

wd1.water_outlet(100)
print(wd1.surplus_water)
wd2.water_outlet(200)
print(wd2.surplus_water)
print(WaterDispenser.surplus_water)
```
* 类方法
  * 需要用@classmethod装饰器装饰
  * cls默认参数
  * 类方法内不可调用实例方法
  * 一般作为类内的一个功能块
```python
import datetime
class Utils:
    now = datetime.datetime.now()

    @classmethod
    def current_date_time(cls):
        return cls.now

    @classmethod
    def current_date(cls):
        return cls.now.strftime("%Y-%m-%d")

    @classmethod
    def current_time(cls):
        return cls.now.strftime("%H-%M-%S")

    @classmethod
    def getYear(cls):
        return cls.now.year

    @classmethod
    def getMonth(cls):
        return cls.now.month

    @classmethod
    def getDay(cls):
        # 调用类方法
        print(Utils.current_date_time())
        return cls.now.day
    
    def show(self) -> None:
        print("show func")

u1 = Utils()
u1.show()
print(u1.current_date_time())
print("-------------------------")
print(Utils.current_date_time())
print(Utils.current_date())
print(Utils.current_time())
print(Utils.getYear())
print(Utils.getMonth())
print(Utils.getDay())
```
* 静态方法
  * @staticmethod 装饰器进行装饰
  * 没有默认参数
  * 不建议在静态方法内使用类属性
  * 一般作为类内的一个功能块
```python
class Calc:
    @staticmethod
    def add(n1, n2):
        return n1 + n2

    @staticmethod
    def sub(n1, n2):
        return n1 - n2

    @staticmethod
    def mul(n1, n2):
        return n1 * n2

    @staticmethod
    def div(n1, n2):
        return n1 / n2


print(Calc.add(10, 20))
print(Calc.sub(10, 20))
print(Calc.mul(10, 20))
print(Calc.div(10, 20))

```
* 封装
  * 公有权限：不带下划线，类内外都可访问
  * 保护权限：_var(一个下划线)，类内可以访问，类外可以访问，但是编译器不会显式的告诉，不建议这么用
  * 私有权限：__var(两个下划线)，只可以类内访问，类外不可访问
```python
class A(object):
    def __init__(self):
        # 公有属性
        self.a = 10
        # 保护属性
        self._b = 20
        # 私有属性
        self.__c = 30

    # 公有方法
    def show(self):
        # 在类中使用公有属性
        print(f"A: {self.a}")
        # 在类中使用保护属性
        print(f"B: {self._b}")
        # 在类中使用私有属性
        print(f"C: {self.__c}")
        # 在类中使用保护权限的方法
        self._display()
        # 在类中使用私有方法
        self.__info()


    # 保护权限的方法
    def _display(self):
        print(f"B: {self._b}")

    # 私有权限的方法
    def __info(self):
        # 在类中使用私有属性
        print(self.__c)
obj = A()
# 在类外使用公有属性
print(obj.a)
# 在类外无法使用保护仅限的属性（不建议这样使用）
print(obj._b)
# 在类外使用私有属性，访问失败
# print(obj.__c)
# 在类外使用公有方法
obj.show()
# 在类外无法使用保护权限的方法（不建议这样使用）
obj._display()
# 在类外访问私有方法，访问失败
# obj.__info()
```

* 计算属性
  * 可以访问和修改私有属性
  * 先定义@property，才能使用@username.setter
```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def username(self):
        return self._name

    @username.setter
    def username(self, name):
        if name.isalpha():
            self._name = name


if __name__ == '__main__':
    tom = Person("tom")
    print(tom.username)
    tom.username = "Tom"
    print(tom.username)
```
* 继承
```python
###########super() 子类使用父类的方法#############
class A(object):
    # A 继承自 object 根类
    def __init__(self, a, b, c):
        self.a = a
        self._b = b
        self.__c = c

    def show(self):
        print(f"A: {self.a}")
        print(f"B: {self._b}")
        print(f"C: {self.__c}")


class B(A):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.d = d

    def show(self):
        super().show()
        print(f"D: {self.d}")

b = B(1,2,3,4)
b.show()

################多继承##############
class FA(object):
    def fa_show(self):
        print("FA Show Run...")

class FB(object):
    def fb_show(self):
        print("FB Show Run...")

class S(FA, FB):
    def s_show(self):
        print("S Show Run...")


s = S()
s.s_show()
s.fa_show()
s.fb_show()

#############多继承初始化#############
class FA(object):
    def __init__(self, a):
        self.a = a

class FB(object):
    def __init__(self, b):
        self.b = b

class S(FB, FA):
    def __init__(self, a, b, c):
        FA.__init__(self, a)
        FB.__init__(self, b)
        self.c = c


c = S(1,2,3)
print(c.a)
print(c.b)
print(c.c)
```
* 多态
  * 相比于静态类型语言，python在编译时没有类型检查
    * isinstance(obj, type) 判断 obj 对象是否是 Type 指定类型或其父类类型的实例
    * issubclass(Type1, Type2) 判断 Type1 是否是 Type2 的子类
  * 本身就是动态类型语言，自身就支持多态，在运行时确定类型
```python
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
        #print(isinstance(littleDoctor, Father))
        #print(isinstance(littleDoctor, Son))
        #print(isinstance(littleDoctor, AnimalDoctor))
        if isinstance(doctor, Father):
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
```
* 类型注解
```python
num: int = 10
print(num)

def show(n: int, msg: str) -> None:
    for i in range(n):
        print(msg.upper())

show(3, "hello")

def show(data : tuple) -> None:
    for d in data:
        print(d)


show((1, 2, 3))
show(('a', 'b', 'c'))
show((1, 2, 3, 'a', 'b', 'c'))

def show(data : tuple[int]) -> None:
    for d in data:
        print(d)

show((1,))
show((1, 2, 3)) # 不符合注解类型
show(('a', 'b', 'c')) # 不符合注解类型
show((1, 2, 3, 'a', 'b', 'c')) # 不符合注解类型
```
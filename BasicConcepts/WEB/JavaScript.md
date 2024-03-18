* 内部方式：\<script> alert("test js"); \</script>
* 外部方式：\<script src="js 文件路径">\</script>

* 函数: function
* 对象: {}
* 声明变量: var
* 比较运算符: === 从内容到类型都相同
```js
// 创建一个包含姓名、年龄和性别属性的对象
var person = {
    name: "John",
    age: 30,
    gender: "boy"
};

// 访问对象的属性并调用函数
myFunction(person.gender, person.age); 

function myFunction(a, b) {
    // 将性别输出到 HTML 页面
    document.write(a);
    // 在控制台输出年龄
    console.log(b);
    
    // 弹窗显示姓名和年龄
    window.alert("Name: " + person.name + ", Age: " + b); 
}

```
**查找html元素**
* 通过 id：var x=document.getElementById("xx");
* 通过标签名：var y=x.getElementsByTagName("p");
* 通过类名：var x=document.getElementsByClassName("xx");

**改变html**
* 内容：document.getElementById(id).innerHTML=新的 HTML
* 属性：document.getElementById(id).attribute=新属性值
* document.getElenementById(id).val = 新属性值

**获取cookie**
* var x = document.cookie;
* 
**使用事件**

* 当用户点击鼠标时： onclick=JavaScript
* 当网页已加载时：onload=JavaScript
* 当图像已加载时：onunload=JavaScript
* 当鼠标移动到元素上时：onmouseover=JavaScript
* 当输入字段被改变时：onchange=JavaScript
* 当用户触发按键时：onmousedown=JavaScript

**窗口属性**
* 获取浏览器窗口尺寸：
  * window.innerHeight - 浏览器窗口的内部高度(包括滚动条)
  * window.innerWidth - 浏览器窗口的内部宽度(包括滚动条)
* 打开新窗口：window.open()
* 关闭当前窗口：window.close()

**屏幕属性**
  * 可用的屏幕宽度：screen.availWidth
  * 可用的屏幕高度：screen.availHeight

**当前页面的地址**
* 返回 web 主机的域名：location.hostname
* 返回当前页面的路径和文件名：location.pathname
* 返回所使用的 web 协议：location.protocol

**浏览器的历史**
* 与在浏览器点击后退按钮相同：history.back()
* 与在浏览器中点击向前按钮相同：history.forward()
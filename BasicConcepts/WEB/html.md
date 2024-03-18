**超文本标记语言**

* \<!--注释-->
* 全局属性
  * class：规定元素的类名
  * id：规定元素的唯一id
  * lang：设置元素中内容的语言代码
  * style：规定元素的行内样式
  * title：规定元素的额外信息
##### 事件属性
**点击html的某个元素时触发一段js代码**
* 窗口事件
  * 适用于\<body>标签
    * onblur：窗口失去焦点时运行脚本
    * onfocus：窗口获得焦点时运行脚本
    * onload：文档加载时运行脚本
* form表单内元素
  * onblur：窗口失去焦点时运行脚本
  * onchange：元素改变时运行脚本
  * onfocus：窗口获得焦点时运行脚本
  * onreset：表单重置是运行脚本，HTML5 不支持
  * onsubmit：当提交表单时运行脚本 
* 键盘事件
  * onkeydown：按下按键时运行脚本
  * onkeypress：按下松开按键时运行脚本
  * onkeyup：松开按键时运行脚本
* 鼠标事件
  * onclick：当单击鼠标时运行脚本
  * ondblclick：当双击鼠标时运行脚本
  * onmousedown：当按下鼠标按钮时运行脚本
  * onmousemove：当鼠标指针移动时运行脚本
  * onmouseout：当鼠标指针移出元素时运行脚本
  * onmouseover：当鼠标指针移至元素之上时运行脚本
  * onmouseup：当松开鼠标按钮时运行脚本
* 多媒体事件
  * onabort：当发生中止事件时运行脚本

----
标题标签：
* \<title>\</title>
* \<h1> - \<h6>
  * \<h1>这是标题 1\</h1>
  * \<h2>这是标题 2\</h2>
* \<p>\</p> 定义段落

容器标签
* \<span>\</span> 用于对文档中的行内元素进行组合，提供了一种将文本的一部分或者文档的一部分独立出来的方式
* \<div>\</div> 标签定义 HTML 文档中的一个分隔区块或者一个区域部分，\<div> 元素经常与 CSS 一起使用，用来布局网页

图片标签

* \<img /> 标签定义 HTML 页面中的图像
  * 属性：
    * src：规定显示图像的 URL（必须）
    * alt：规定图像的替代文本（必须）
    * title：鼠标悬停于图像时显示的文本
    * width：图像的宽度
    * height：图像的高度
    * border：设置图像边框的宽度

超链接标签
* \<a>\</a> 标签定义超链接：用于从一个页面链接到另一个页面
  * href：规定链接的目标 URL

列表标签
* \<ul>\<li>...\</li>\</ul> 定义无序列表：\<ul> 标签与 \<li> 标签一起使用，创建无序列表
* \<ol><\ol> 有序列表

表格标签
* 表格：\<table>\</table>
  * border：规定表格单元是否拥有边框
* 行：\<tr>\</tr>
* 单元格：\<td>\</td>

表单域
* 标签：\<form>\</form> 创建供用户输入的 HTML 表单
  * action : 指定接收并处理表单信息的服务器url地址
  * method : 表单数据的提交方式
  * name : 指定表单名称

* 标签：\<input>规定了用户可以在其中输入数据的输入字段，输入字段可通过多种方式改变，取决于 type 属性
  * type：规定要显示的 \<input> 元素的类型
    * text：单行文本输入框（不换行的）
    * password：密码输入框
    * radio：单选框（配合name 可以实现单选效果）
    * checkbox：复选框
    * button：普通按钮
    * submit：提交按钮
    * reset：重置按钮
    * image：图像形式的提交按钮
    * file：文件域, 点击之后打开文件选择器
    * name：控件名称 , name 相同则表示是同一组数据
    * value：指定 \<input> 元素 value 的值
    * size：显示大小
    * checked：是否被选中
    * maxlength：控制输入的最大字符数量
* \<textarea>\</textarea> 多行文本
* 

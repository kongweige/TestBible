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
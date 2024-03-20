## PostMan使用
##### 脚本编写
```js
// Status Code：Code is 200
// 验证响应状态码
pm.test("响应状态码为 200", function () {
    pm.response.to.have.status(200);
});

// Response Body：contains string 
// 验证响应体中是否包含某个字符串
pm.test("响应体中包含预期的字符串", function () {
    pm.expect(pm.response.text()).to.include("doggie");
});

// Response Body：JSON value check
// 验证 JSON 中的某个值是否等于预期的值
pm.test("宠物名称为 doggie", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData[0].name).to.eql("doggie");
});

// Response Body：Is equal to a string
// 验证响应体是否与某个字符串完全相同
pm.test("响应体正确", function () {
    pm.response.to.have.body("response_body_string");
});

// Response Body：Content-Type header check
// 验证响应头信息中的 Content-Type 是否存在
pm.test("Content-Type is present", function () {
    pm.response.to.have.header("Content-Type");
});

// Response time is less than 200ms
// 验证响应时间是否小于某个值
pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});
```
##### 测试集

##### 变量
* Postman 中变量的种类与作用域
* Data：在测试集中上传的数据
* Environment：环境范围
* Collection：集合范围
* Global：全局范围
* Local：在脚本中设置的变量
-----
* 全局变量：Environments -> Globals
* 测试集变量：测试集页面 -> Variables
* 环境变量：Environments -> +
----
##### 变量使用
请求 URL, Params 参数或 Body 表格或JSON/XML 文本中通过 {{变量名}} 使用

在 Pre-request Script 和 Tests 脚本中使用封装好的语句获取或者设置对应变量
* 数据类型
  * 数字类型：
    * TINTINT	0～255 或 -128～127，1字节，最小的整数
    * SMALLINT	0～65535 或 -32768～32767，2字节，小型整数
    * MEDIUMINT	0～16777215 或 -8388608～8388607，3字节，中型整数
    * INT	0～4294967295 或 -2147683648～2147683647，4字节，标准整数
    * BIGINT	8字节，大整数
    * FLOAT	单精度浮点值
    * DOUBLE	双精度浮点值
    * BOOLEAN	布尔值
  * 字符类型：
    * CHAR	1～255 个字符，固定长度字符串
    * VARCHAR	长度可变，最多不超过 255 个字符
    * TEXT	最大长度为 64K 的变长文本
    * TINYTEXT	与 TEXT 相同，但最大长度为 255 字节
    * MEDIUMTEXT	与 TEXT 相同，但最大长度为 16K
    * LONGTEXT	与 TEXT 相同，但最大长度为 4GB
  * 日期类型：
    * DATE	日期，格式 YYYY-MM-DD
    * TIME	时间，格式 HH:MM:SS
    * DATETIME	日期和时间，格式 YYYY-MM-DD HH:MM:SS
    * TIMESTAMP	时间标签，功能和 DATETIME 相同，但范围较小
    * YEAR	年份可指定两位数字和四位数字的格式

* 开启 mysql 服务：
```sql
net start mysql
```
* 登录：
```sql
mysql -h主机IP -u用户名 -p密码

mysql -u root -p 
```
* 修改密码：
```sql
alter user 'root'@'localhost' identified by '密码';
```
* 退出：exitss
* 关闭 mysql 服务：
```sql
net stop mysql
```

### 操作数据库
**创建**
```sql
-- 创建基本的数据库
CREATE DATABASE test_db;
-- 创建名为test_db2的数据库，并制定字符集为utf8
CREATE DATABASE test_db2 CHARACTER SET utf8;
-- 创建数据库时，先进行判断，如果不存在再创建
CREATE DATABASE IF NOT EXISTS test_db3 CHARACTER SET utf8;
```
**查看**
```sql
-- 查看所有数据库
SHOW DATABASES;

-- 选择数据库
USE test_db;

-- 查看选定数据库的创建信息
SHOW CREATE DATABASE test_db;

```
**修改**
```sql
-- 修改test_db数据库的字符集为GBK
ALTER DATABASE test_db CHARACTER SET GBK;
```
**删除**
```sql
DROP DATABASE IF EXISTS test_db; 
```

### 操作数据表
**创建**

列名 数据类型 [NOT NULL | NULL] [DEFAULT 默认值] [AUTO_INCREMENT]
[PRIMARY KEY ] [注释]

* NOT NULL | NULL：该列是否允许是空值
* DEFAULT：表示默认值
* AUTO_INCREMENT：表示是否是自动编号
* PRIMARY KEY：表示是否为主键
```sql

-- 创建一个表名为student的表，设置名为id和name的两个列
CREATE TABLE student(
id INT,
name VARCHAR(20)
);
```
**查看**

```sql
-- 查看所有表名
SHOW TABLES;

-- 查看表结构
DESCRIBE s2;
DESCRIBE s2 id;

-- 查看表结构简写
DESC s2;
DESC s2 name;
```
**修改**


```sql

```
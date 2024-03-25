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

-- 创建表S2将student复制到S2
CREATE TABLE S2 LIKE student;

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

* 添加新列
```sql
-- 选择数据库
USE test_db;
-- 添加新列
ALTER TABLE student ADD email VARCHAR(50) NOT NULL;
-- 查看表结构
DESC student;
```
* 修改列定义
```sql
-- 添加分数列，先定义为字符类型
ALTER TABLE student ADD score VARCHAR(10);
-- 修改字段类型
ALTER TABLE student MODIFY score INT;
-- 查看表结构
DESC student;
```
* 修改列名
```sql
-- 修改列名并指定列的默认值
ALTER TABLE student CHANGE COLUMN NAME stu_name VARCHAR(30) DEFAULT NULL;
-- 查看表结构
DESC student;
```
* 删除列
```sql
-- 将数据表 student 中的列 score 删除
ALTER TABLE student DROP score;
-- 查看表结构
DESC student;
```
* 修改表名
```sql
-- 将数据表 student 更名为 stu
ALTER TABLE student RENAME AS stu;
-- 将数据表 stu 更名为 stu_table
RENAME TABLE stu TO stu_table;
-- 查看表名
SHOW TABLES;
```
**删除**
```sql
DROP TABLE student;

-- 判断是否存在，再删除
DROP TABLE IF EXISTS student;
```
### 操作表数据

**插入**
```sql
-- 创建usr表
CREATE TABLE usr (
id INT,
name varchar(20),
addr varchar(20)
);

-- 插入表数据
INSERT INTO usr (id, name,  addr) VALUES(10,'张三','北京');

INSERT INTO usr (id, name,  addr) VALUES(10,'张三','北京'), (20,'AAA','hanghai'),(30,'BBB','hanghai');
```

**修改**
```sql
-- 选择 db1 为当前数据库
USE db1;

-- 创建 student 表
CREATE TABLE student( 
  id INT,
  name VARCHAR(20),
  sex CHAR(1),
  age TINYINT,
  city VARCHAR(50)
);

-- 插入 5 条数据
INSERT INTO student
VALUES(1,'小李','男', 18, '北京'),
(2,'小白','女', 20, '成都'),
(3,'小王','男', 23, '上海'),
(4,'小赵','女', 21, '深圳'),
(5,'小周','男', 25, '杭州');

-- 不带条件修改，将所有的性别改为女
UPDATE student SET sex = '女';

-- 带条件的修改，将 id 为 3 的学生，性别改为男
UPDATE student SET sex = '男' WHERE id = 3;

-- 一次修改多个列， 将 id 为 2 的学员，年龄改为 30，地址改为 北京
UPDATE student SET age = 30, city = '北京' WHERE id = 2;
```
**删除**
```sql
-- 删除表中指定行的数据
DELETE FROM usr WHERE name='AAA';
```
### 表查询
**单表查询**
```sql
-- 查询整个表中的信息
SELECT * FROM departments;
```
**字段查询**
```sql
-- 查询部门的名称
SELECT dept_name FROM departments;
```
**起别名**
```sql
-- 查询员工信息，并将列名改为中文
SELECT 
    emp_no AS '编号',
    first_name AS '名',
    last_name AS '姓',
    gender AS '性别',
    hire_date AS '入职时间'
FROM
    employees emp;
```
**去重**
```sql
-- 去掉重复职级信息 
SELECT DISTINCT title FROM titles;
```
**运算查询**
```sql
-- 所有员工的工资 +1000 元进行显示
SELECT emp_no , salary + 1000 FROM salaries;
```
**条件查询**
| 运算符 | 说明 |
|-------|-------|
| > < <= >= = <> != | 大于、小于、小于等于、大于等于、等于、不等于 | 单元格3 |
| BETWEEN...AND... | 范围限定 |
| IN | 子集限定 |
| LIKE | '%or%'	模糊查询 |
| IS NULL | 为空 |
| % | 匹配任意多个字符 |
| - | 匹配一个字符 |
	
	
```sql
--------------------BETWEEN----------------------------
-- 查询年薪介于 70000 到 70003 之间的员工编号和年薪
SELECT 
    emp_no, salary
FROM
    salaries
WHERE
    salary BETWEEN 70000 AND 70003;


--------------------IN---------------------------


-- 查询入职日期为 1995-01-27 和 1995-03-20 日的员工信息
SELECT 
    *
FROM
    employees
WHERE
    hire_date IN ('1995-01-27', '1995-03-20');


--------------------IS NULL-----------------------------


-- 选择 hog_demo 为当前数据库
USE hog_demo;

-- 更新 student 表中 id 为 2 的 age 值为 NULL
UPDATE student SET age = NULL WHERE id = 2;

-- 查询学生表中年龄为 NULL 的学生信息
SELECT 
    *
FROM
    student
WHERE
    age IS NULL;


-----------------------LIKE-----------------------

-- 查询名字中包含 fai 的员工的信息
SELECT 
    *
FROM
    employees
WHERE
    first_name LIKE '%fai%';

-- 查询名字中 fa 开头的名字长度为 3 位的员工信息
SELECT 
    *
FROM
    employees
WHERE
    first_name LIKE 'fa_';

```

**排序**
- ASC 表示升序排序（默认）
- DESC 表示降序排序
```sql
-- 在入职时间排序的基础上，再使用 emp_no 进行排序
SELECT 
    emp_no, hire_date
FROM
    employees
ORDER BY 
    hire_date DESC,
    emp_no DESC;
```
**聚合函数**
* COUNT()：统计指定列不为 NULL 的记录行数
* MAX()：计算指定列的最大值
* MIN()：计算指定列的最小值
* SUM()：计算指定列的数值和
* AVG()：计算指定列的平均值
```sql
-- 查询职级名称为 Senior Engineer 的员工数量
SELECT 
    COUNT(*)
FROM
    titles
WHERE
    title = 'Senior Engineer';

-- 查询员工编号为 10002 的员工的最高年薪
SELECT 
    MAX(salary)
FROM
    salaries
WHERE
    emp_no = 10002;

-- 查询员工编号为 10002 的员工的最低年薪
SELECT 
    MIN(salary)
FROM
    salaries
WHERE
    emp_no = 10002;

-- 查询员工编号为 10002 的员工的薪水总和
SELECT 
    SUM(salary)
FROM
    salaries
WHERE
    emp_no = 10002;

-- 查询员工编号为 10002 的员工的平均年薪
SELECT 
    AVG(salary)
FROM
    salaries
WHERE
    emp_no = 10002;
```
**分组查询**
* WHERE 子句：从数据源中去掉不符合其搜索条件的数据
* GROUP BY 子句：搜集数据行到各个组中，统计函数为各个组计算统计值
* HAVING 子句：去掉不符合其组搜索条件的各行数据行
```sql
-- 查询每个员工的薪资和
SELECT 
    emp_no, SUM(salary)
FROM
    salaries
GROUP BY emp_no;

-- 查询员工编号小于 10010 的，薪资和小于 400000 的员工的薪资和
SELECT 
    emp_no, SUM(salary)
FROM
    salaries
WHERE
    emp_no < 10010
GROUP BY emp_no
HAVING SUM(salary) < 400000;


-------------对结果分组结果进行排序----------------------
select 
    university,
    avg(question_cnt) AS avg_question_cnt
FROM
    user_profile
group by
    university
ORDER BY 
    avg_question_cnt;
    
```

**limit**
```sql
-- 展示前 10 条员工信息
SELECT * FROM employees LIMIT 10;
SELECT * FROM employees LIMIT 0, 10;
SELECT * FROM employees LIMIT 10 OFFSET 0;

-- 显示年薪从高到低排序，第 15 位到第 20 位员工的编号和年薪
SELECT 
    emp_no, salary
FROM
    salaries
ORDER BY salary DESC
LIMIT 14, 6;

SELECT 
    emp_no, salary
FROM
    salaries
ORDER BY salary DESC
LIMIT 6 OFFSET 14;
```
### 主键
主键是用于唯一标识数据库表中的每条记录的字段

**主键约束**
```sql
--------------------------创建主键------------------------------
-- 创建一个带主键的表
CREATE TABLE emp1(
    -- 设置主键 唯一 非空 
    eid INT PRIMARY KEY, 
    ename VARCHAR(20), 
    sex CHAR(1)
);

-- 给存在的表添加主键
CREATE TABLE emp2( 
    eid INT , 
    ename VARCHAR(20), 
    sex CHAR(1) 
)

-- 通过 DDL 语句进行设置 
ALTER TABLE emp2 ADD PRIMARY KEY(eid);


----------------------自增AUTO_INCREMENT------------------------

-- 创建主键自增的表 
CREATE TABLE emp3(
    eid INT PRIMARY KEY AUTO_INCREMENT, 
    ename VARCHAR(20), 
    sex CHAR(1) 
);


----------------------------删除主键约束---------------------------


-- 删除表中的主键
ALTER TABLE 表名 DROP PRIMARY KEY;

-- 使用 DDL 语句删除表中的主键 
ALTER TABLE emp2 DROP PRIMARY KEY; 
-- 查看表结构
DESC emp2;
```

**非空约束**
```sql
-- 添加非空约束
CREATE TABLE emp5( 
    eid INT PRIMARY KEY AUTO_INCREMENT, 
    -- ename 字段不能为空 
    ename VARCHAR(20) NOT NULL, 
    sex CHAR(1) 
);
```

**唯一约束**

表中的某一列的值不能重复
```sql
-- 创建带有唯一约束的表  
CREATE TABLE emp6(
    eid INT PRIMARY KEY AUTO_INCREMENT,
    -- 为 ename 字段添加唯一约束
    ename VARCHAR(20) UNIQUE,
    sex CHAR(1) 
);
```
**默认值**
```sql
-- 创建带有默认值的表 
CREATE TABLE emp7( 
    eid INT PRIMARY KEY AUTO_INCREMENT,
    ename VARCHAR(20), 
    -- 为 sex 字段添加默认值 
    sex CHAR(1) DEFAULT '女'
);
```
### 外键约束
```sql
# 创建一个关联到主表的从表
CREATE TABLE emp_part(  
emp_id INT PRIMARY KEY AUTO_INCREMENT,  
ename VARCHAR(20),  
age INT ,  
gender VARCHAR(10),
dept_id INT,
-- 添加外键约束 
CONSTRAINT emp_dept FOREIGN KEY(dept_id) REFERENCES dept(id)
);

# 插入一条非法数据
INSERT INTO emp_part VALUES(1,'cindy',20,'female','4')


----------------------删除------------------------------
# 删除外键约束 
ALTER TABLE emp_part DROP FOREIGN KEY emp_dept 

# 插入一条非法数据
INSERT INTO emp_part VALUES(1,'cindy',20,'female','4') 

SELECT * FROM emp_part  

# 向主表中插入一条数据
INSERT INTO dept VALUES(2,'运营部','张三','北京') 
# 向从表中插入一条数据
INSERT INTO emp_part VALUES(1,'cindy',20,'female','2') 
# 删除主表中的数据 
DELETE FROM dept WHERE id=2

select id,socre from S group by socre>80;

```

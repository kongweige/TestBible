**查看手机状态**
* device 正常
* offline 连接出现异常，设备无响应
* unauthorized 未授权
  * adb devices
  * adb get-state

**命令格式**
* 格式 ：
  * adb [-d｜-e｜-s <serialNumber>]<command>
    * -d 指定当前唯一通过 Usb 连接的 android 设备为命令目标（了解）
    * -e 指定当前唯一运行的模拟器为命令目标（了解）
    * -s 指定相应的设备为命令目标（重点）

**安装**
* 普通安装 
  * adb install <apk路径>
* 覆盖安装/替代安装 
  * adb install -r <apk路径>

**卸载**
* 卸载应用
  * adb uninstall 包名
* 卸载应用（不删除配置文件，保存数据缓存信息）
  * adb uninstall -k 包名

**获取当前页面名**
* 1、打开手机 app 应用的某个页面
* 2、打开命令行工具
  * 执行命令：adb shell "dumpsys window | grep mCurrentFocus"

**获取启动页面的 activity**
* mac：adb logcat ActivityManager:I | grep "cmp"
* win：adb logcat ActivityManager:I | findstr "cmp"

**启动页面**
* 命令：adb shell am start -n <包名>/<avticity名>

**命令**
* 查看目录结构：adb shell ls
* 查看系统当前日期：adb shell date
* 查看系统 CPU 使用情况：adb shell cat /proc/cpuinfo
* 查看系统内存使用情况：adb shell cat /proc/meminfo

**查看应用列表**
* 显示所有应用：adb shell pm list packages
* 显示系统自带应用：adb shell pm list packages -s
* 显示第 3 方应用：adb shell pm list packages -3

**查看当前的页面名**
* adb shell "dumpsys window |grep mCurrentFocus"

**清除应用数据及缓存**
* adb shell pm clear <包名>

**传输文件**
* adb push 电脑路径 设备路径
* adb pull 设备路径 电脑路径

**日志查看**
* V — 明细 verbose(最低优先级)
* D — 调试 debug
* I — 信息 info
* W — 警告 warn
* E — 错误 error
* F — 严重错误 fatal
* S — 无记载 silent（最高优先级，绝不会输出任何内容）
  * adb logcat --help

**模拟按键操作**

打开【指针位置】设置
```shell
adb shell input
点击事件
adb shell input tap x坐标 y坐标
输入事件
adb shell input text <输入内容>
滑动事件
adb shell swipe <起点x> <起点y> <终点x> <终点y> <滑动时长>
模拟手机按键
返回键：
adb shell input keyevent 4
Home 键：
adb shell input keyevent 3（置应用于后台运行）
音量放大：
adb shell input keyevent 24
音量缩小：
adb shell input keyevent 25
```
**adb性能分析**
> 解决的问题：崩溃（Crash，弱网）、卡顿（掉帧，gc，cpu）、响应慢（启动时间，交互响应，h5加载）、发热（cpu，mem，io，network，gps等硬件问题）、掉电快（硬件占用）、兼容性问题（机型覆盖，回归）

* 查看当前系统 CPU 使用情况
  * adb shell dumpsys cpuinfo
* 查看当前系统的内
  * adb shell dumpsys meminfo
* 查看某个应用的内存
  * adb shell dumpsys meminfo <应用名>
* 查看某个包的一些性能指标
  * adb shell top ｜grep "包名" 
  * adb shell top -d 1 |grep "包名"

**压力测试**
* adb shell monkey [参数] {随机发送事件数}
```shell
adb shell monkey 100
```
* 常用选项
  * -v ：用于指定反馈信息级别，总共分 3 个级别
    * adb shell monkey -v -v -v 10
  * -s <seednumber>：用于指定伪随机数生成器的 seed（种子）值
    * adb shell monkey -s 123 10
  * --throttle <milliseconds>：每个事件结束后的间隔时间
    * adb shell monkey --throttle 300 10
  * -p： 用于约束限制，用此参数指定一个或多个包
    * adb shell monkey -p com.android.browser 10
  * --ignore-crashes：忽略崩溃
  * --ignore-timeouts：忽略超时
  * --ignore-security-exceptions：忽略安全异常
  * --ignore-native-crashes：忽略本地代码导致的崩溃异常
  * --monitor-native-crashes：跟踪本地方法的崩溃问题

* 事件选项
  * --pct-touch：触摸事件
  * --pct-motion：滑动事件
  * --pct-appswitch：activity 之间的切换
  * --pct-pinchzoom：缩放事件
  * --pct-rotation：屏幕旋转事件
  * --pct-flip：键盘事件
  * --pct-anyevent：任意事件

**注意：所有类型属性比例加起来不能超过 100**

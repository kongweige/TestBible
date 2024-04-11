# 企业微信自动登录脚本
import time
import yaml
from selenium import webdriver


class TestCookieLogin:
    def setup_class(self):
        self.driver = webdriver.Chrome()

    def teardown_class(self):

    # 获取cookie信息
    def test_get_cookies(self):
        # 进入企业微信首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 等待手动登录
        time.sleep(20)
        # 登录成功后获取cookie信息
        cookie = self.driver.get_cookies()
        # print(cookie)
        # 将cookie存入一个持久化存储的地方，数据库or文件
        with open("cookie.yaml","w") as f:
            yaml.safe_dump(cookie,f)

    # 植入cookie信息
    def test_add_cookie(self):
        pass
        # 1. 访问企业微信主页界面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 2. 定义cookie,从文件中获取cookie信息
        cookie = yaml.safe_load(open("cookie.yaml"))
        # 3. 植入cookie
        for c in cookie:
            self.driver.add_cookie(c)
        time.sleep(3)
        # 4. 再次访问企业微信界面，发现无需扫码自动登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

from selenium import webdriver
from selenium.webdriver.common.by import By

from log_utils import logger

# 日志与脚本结合
class TestDataRecord:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_log_data_record(self):
        # 实例化self.driver
        # search_content = "霍格沃兹测试开发"
        search_content = "霍格沃兹测试开发学社"
        # 打开百度首页
        self.driver.get("https://www.sogou.com/")
        logger.debug("打开搜狗首页")
        # 输入霍格沃兹测试学院
        self.driver.find_element(By.CSS_SELECTOR, "#query"). \
            send_keys(search_content)
        logger.debug(f"搜索的内容为{search_content}")
        # 点击搜索
        self.driver.find_element(By.CSS_SELECTOR, "#stb").click()
        # 搜索结果
        search_res = self.driver.find_element(By.CSS_SELECTOR, "em")
        logger.info(f"搜索结果为{search_res.text}")
        assert search_res.text == search_content


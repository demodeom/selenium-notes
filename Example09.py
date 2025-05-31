from selenium.common import NoSuchElementException
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

# 设置 浏览器驱动路径
firefox_service = Service(executable_path="/usr/local/bin/geckodriver")

# 设置浏览器文件路径
firefox_options = Options()
firefox_options.binary_location = "/usr/bin/firefox"

# 打开浏览器
firefox_driver = Firefox(options=firefox_options, service=firefox_service)

# 设置窗口最大化
firefox_driver.maximize_window()

# 访问 百度
baidu_url = "https://www.baidu.com/"
firefox_driver.get(baidu_url)

# 元素查找 通过 css 选择器 查找元素
try:
    kw_ele = firefox_driver.find_element(By.CSS_SELECTOR, "#k123")
    print(kw_ele.get_attribute("outerHTML"))
except NoSuchElementException:
    exit("未找到元素")
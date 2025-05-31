from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import Firefox, FirefoxProfile

# 设置 浏览器驱动路径
firefox_service = Service(executable_path="/usr/local/bin/geckodriver")

# 设置浏览器文件路径
firefox_options = Options()
firefox_options.binary_location = "/usr/bin/firefox"

# 打开浏览器
firefox_driver = Firefox(options=firefox_options, service=firefox_service)

# 设置元素查找默认等待时间， 单位秒
firefox_driver.implicitly_wait(5)


# 设置窗口最大化
firefox_driver.maximize_window()



# 访问 淘宝
baidu_url = "https://www.taobao.com/"
firefox_driver.get(baidu_url)

# 元素查找 通过 css 选择器 查找元素
kw_ele = firefox_driver.find_element(By.CSS_SELECTOR, "#q123")

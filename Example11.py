from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import Keys
# 设置 浏览器驱动路径
firefox_service = Service(executable_path="/usr/local/bin/geckodriver")

# 设置浏览器文件路径
firefox_options = Options()
firefox_options.binary_location = "/usr/bin/firefox"

# 打开浏览器
firefox_driver = Firefox(options=firefox_options, service=firefox_service)

# 设置元素查找默认等待时间， 单位秒
firefox_driver.implicitly_wait(30)

# 设置窗口最大化
firefox_driver.maximize_window()

# 访问 百度
baidu_url = "https://www.baidu.com/"
firefox_driver.get(baidu_url)

# 模拟输入
kw_ele = firefox_driver.find_element(By.CSS_SELECTOR, "#kw")
kw_ele.send_keys("2025致富新方式")

# 模拟按 Enter 键
kw_ele.send_keys(Keys.ENTER)


# 模拟点击
# su_btn = firefox_driver.find_element(By.CSS_SELECTOR, "#su")
# su_btn.click()
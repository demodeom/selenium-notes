from selenium.webdriver import Firefox
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

# 设置窗口大小 1600x900
# firefox_driver.set_window_size(1600, 900)

# 访问 百度
baidu_url = "https://www.baidu.com/"
firefox_driver.get(baidu_url)
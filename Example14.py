from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
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

# 访问 慕课网
index_url = "https://coding.imooc.com/"
firefox_driver.get(index_url)

# 查找第一个课程
course_ele = firefox_driver.find_element(By.CSS_SELECTOR, ".course-card a")
course_ele.click()

# 获取窗口所有 句柄
all_window = firefox_driver.window_handles

# 切换到第二个窗口，索引值 从 0 开始的
firefox_driver.switch_to.window(all_window[1])

# 获取课程简介
desc_box_ele = firefox_driver.find_element(By.CSS_SELECTOR, ".desc-box")
print(desc_box_ele.text)


# 切换到最后一个窗口， -1 最后一个窗口
firefox_driver.switch_to.window(all_window[-1])
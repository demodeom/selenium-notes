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

# 查找所有新闻
title_contents = firefox_driver.find_elements(By.CSS_SELECTOR, ".title-content")
for title_content in title_contents:
    # print(title_content.get_attribute("outerHTML"))
    # .text 属性 获取标签文本
    news_title = title_content.text
    # get_attribute("属性名") 方法获取属性值
    news_href = title_content.get_attribute("href")
    print(f"新闻标题: {news_title}, 新闻地址: {news_href}")
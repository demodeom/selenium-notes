# 等待

## 例子1：元素查找失败


```python
# 访问 淘宝
baidu_url = "https://www.taobao.com/"
firefox_driver.get(baidu_url)
# 元素查找 通过 css 选择器 查找元素
try:
    kw_ele = firefox_driver.find_element(By.CSS_SELECTOR, "#q")
    print(kw_ele.get_attribute("outerHTML"))
except NoSuchElementException:
    exit("未找到元素")
```



当网速慢时， 以上代码输入结果可能是  **未找到元素**

**为什么 ？**



## 显式等待

```python
import time

# 访问 淘宝
baidu_url = "https://www.taobao.com/"
firefox_driver.get(baidu_url)

# 显式等待, 单位： 秒
time.sleep(5)

# 元素查找 通过 css 选择器 查找元素
try:
    kw_ele = firefox_driver.find_element(By.CSS_SELECTOR, "#q")
    print(kw_ele.get_attribute("outerHTML"))
except NoSuchElementException:
    exit("未找到元素")
```

## 隐式等待

隐式等待配置通常放在打开浏览器之后， 单位：秒

```python
# 打开浏览器
firefox_driver = Firefox(options=firefox_options, service=firefox_service)

# 设置元素查找默认等待时间， 单位：秒
firefox_driver.implicitly_wait(30)


# 访问 淘宝
baidu_url = "https://www.taobao.com/"
firefox_driver.get(baidu_url)

# 元素查找 通过 css 选择器 查找元素
kw_ele = firefox_driver.find_element(By.CSS_SELECTOR, "#q123")
```

在等待时间范围之内， 如果查找到元素， 立即返回元素，超出时间未找到元素， 抛出 **NoSuchElementException** 错误



## 显式等待 VS 隐式等待


|          | 作用范围                   | 灵活性                                   |
| -------- | :------------------------- | ------------------------------------------ |
| 显式等待 | 当前行生效                 | 不灵活（必须等待指定时间）                                   |
| 隐式等待   | 全局生效  | 灵活（找到元素立即返回，不必等待时间结束） |







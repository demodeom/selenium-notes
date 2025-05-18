# 模拟事件



## 例子1：百度-模拟输入

```python
# 模拟输入
kw_ele = firefox_driver.find_element(By.CSS_SELECTOR, "#kw")
kw_ele.send_keys("2025致富新方式")
```

## 例子2：百度-模拟点击

```python
# 模拟点击
su_btn = firefox_driver.find_element(By.CSS_SELECTOR, "#su")
su_btn.click()
```

## 例子3：百度-模拟按键

```python
from selenium.webdriver import Keys

# 模拟输入
kw_ele = firefox_driver.find_element(By.CSS_SELECTOR, "#kw")
kw_ele.send_keys("2025致富新方式")

# 模拟按 Enter 键
kw_ele.send_keys(Keys.ENTER)
```

## 例子4：慕课网-鼠标悬停

```python
from selenium.webdriver import ActionChains

# 访问 慕课网
baidu_url = "https://www.imooc.com/"
firefox_driver.get(baidu_url)

# 模拟鼠标悬停（鼠标移入）
kw_ele = firefox_driver.find_element(By.PARTIAL_LINK_TEXT, "发现")
ActionChains(firefox_driver).move_to_element(kw_ele).perform()
```

## 更多事件。。。

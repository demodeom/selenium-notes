# 切换 标签

当浏览器打开新标签时，需要查新标签的内容，需要将当前**句柄**切换到新标签

句柄：每个标签拥有一个唯一的标识，这个标识就是句柄，在 Selenium 框架中， 使用字符串表示句柄， 大概像这样 `"59eb8a0a-3f56-4396-b9ac-193cace50e8a"`

默认打开浏览器， 访问一个网站， 浏览器只打开一个标签， 所以不需要切换句柄



## 获取句柄

使用属性 `window_handles` 获取所有的句柄 

返回值

- 类型：list, 
- 元素类型：str , 比如： "59eb8a0a-3f56-4396-b9ac-193cace50e8a"


以 百度首页热点新闻 为例

```py
# 访问 百度
baidu_url = "https://www.baidu.com/"
firefox_driver.get(baidu_url)

# 查找所有新闻
title_contents = firefox_driver.find_elements(By.CSS_SELECTOR, ".title-content")

for title_content in title_contents:
    title_content.click()

all_windows = firefox_driver.window_handles

print(f"window_handles 返回值类型 {type(all_windows)}")

for window in all_windows:
    print(f"window 类型 {type(window)}, 值：{window}")
```

输出信息如下 (句柄是软件随机生成的临时的唯一标识，不是固定，每次输出结果可能都不一样)

```
window_handles 返回值类型 <class 'list'>
window 类型 <class 'str'>, 值：ae44a37e-756e-4875-8cf3-bce00681bd66
window 类型 <class 'str'>, 值：7789b378-857a-4c16-b0c5-550b6620e422
window 类型 <class 'str'>, 值：c42314bb-fbcd-4e79-aa23-c9445260457c
window 类型 <class 'str'>, 值：d2415dd6-a017-4f22-89a3-ad5c0338d20f
window 类型 <class 'str'>, 值：8af28463-6b26-42fa-ad75-35950f98eb66
window 类型 <class 'str'>, 值：b65997ff-bbec-4167-bf84-868f5e534d72
window 类型 <class 'str'>, 值：3671d86e-fcc2-4250-be8d-998e2fdad021
window 类型 <class 'str'>, 值：9ca3a72d-7eec-474d-a3eb-335a2f43cd8f
window 类型 <class 'str'>, 值：ded16738-7866-4d7f-8f16-651db0389be1
window 类型 <class 'str'>, 值：47069978-3a18-4b12-8120-a7ab96fc9205
window 类型 <class 'str'>, 值：c43a1736-d91b-4933-8290-cffa2d8c822f
```

## 切换标签

切换标签(选项卡)需要使用句柄，所以需要先获取句柄

`firefox_driver.switch_to.window()` 方法可以切换标签(选项卡)

参数： 标签(选项卡)句柄
返回值： 无


以慕课网为例, 获取课程简介

```python
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
```

## 多学一招


```Py
# 切换到第二个窗口，索引值 从 0 开始的
firefox_driver.switch_to.window(all_window[1])
```

```Py
# 切换到最后一个窗口， -1 最后一个窗口
firefox_driver.switch_to.window(all_window[-1])
```










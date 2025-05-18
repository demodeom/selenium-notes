# 查找 元素

# 元素查找

selenium 框架提供了两个方法用于查找元素， 分别是 **find_element()** 和 **find_elements()**

**功能， 返回值**

- **find_element()** 查找第一个匹配条件的元素，返回值类型 **WebElement**

- **find_elements()** 查找多有匹配条件的元素， 返回值类型 List ，List 中元素类型  **WebElement**

**形参**

- 参数1： 元素匹配方式
- 参数2： 匹配方式对应的值

匹配方式

| 匹配方式                 | 说明                         | 备注                                                 |
| :----------------------- | ---------------------------- | ---------------------------------------------------- |
| **By.ID**                | 通过 ID 属性选择元素         |                                                      |
| **By.CLASS_NAME**        | 通过 **class 属性** 选择元素 |                                                      |
| **By.NAME**              | 通过 name 属性定位元素       | 通常用于form表单、iframe元素查找                     |
| **By.TAG_NAME**          | 通过 标签名 选择元素         |                                                      |
| **By.LINK_TEXT**         | 通过精确文本匹配选择链接元素 | 通常用于查找特定文本超链接，比如： 下一页            |
| **By.PARTIAL_LINK_TEXT** | 通过部分文本匹配选择链接元素 |                                                      |
|                          |                              |                                                      |
| **By.XPATH**             | 通过 XPATH 选择元素          |                                                      |
| **By.CSS_SELECTOR**      | 通过 CSS 选择器 定位元素     | <b style="color: red">常用</b>（语法灵活、功能强大） |



## 例子1： 百度首页-搜索框



```html
<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off" placeholder="多地疾控提醒新冠阳性率上升">
```

<tabs>
<tab title="Id 属性">
<code-block lang="Python">
# 通过 ID 属性查找元素
kw_ele = firefox_driver.find_element(By.ID, "kw")
print(kw_ele.get_attribute("outerHTML"))
</code-block>
</tab>

<tab title="Name 属性">
<code-block lang="Python">
# 通过 name 查找元素
kw_ele = firefox_driver.find_element(By.NAME, "wd")
print(kw_ele.get_attribute("outerHTML"))
</code-block>
</tab>


<tab title="Class 属性">
<code-block lang="Python">
# 通过 class 查找元素
kw_ele = firefox_driver.find_element(By.CLASS_NAME, "s_ipt")
print(kw_ele.get_attribute("outerHTML"))
</code-block>
</tab>


<tab title="Css 选择器">
<code-block lang="Python">
# 通过 css 选择器 查找元素
kw_ele = firefox_driver.find_element(By.CSS_SELECTOR, "#kw")
print(kw_ele.get_attribute("outerHTML"))
</code-block>
</tab>


<tab title="Css 选择器">
<code-block lang="Python">
# 通过 css 选择器 查找元素
kw_ele = firefox_driver.find_element(By.CSS_SELECTOR, ".s_ipt")
print(kw_ele.get_attribute("outerHTML"))
</code-block>
</tab>


<tab title="Css 选择器">
<code-block lang="Python">
# 通过 css 选择器 查找元素
kw_ele = firefox_driver.find_element(By.CSS_SELECTOR, "input[id='kw']")
print(kw_ele.get_attribute("outerHTML"))
</code-block>
</tab>

<tab title="Css 选择器">
<code-block lang="Python">
# 通过 css 选择器 查找元素
kw_ele = firefox_driver.find_element(By.CSS_SELECTOR, "input[name='wd']")
print(kw_ele.get_attribute("outerHTML"))
</code-block>
</tab>

</tabs>


> 查找元素方法有很多，根据实际情况， 灵活应变
> 推荐 Css 选择器，语法灵活、简单、功能强大




## 例子2： 百度首页-热点新闻

查找多个元素， 并遍历结果， 获取数据

```python
# 查找所有新闻
title_contents = firefox_driver.find_elements(By.CSS_SELECTOR, ".title-content")
for title_content in title_contents:
    # print(title_content.get_attribute("outerHTML"))
    # .text 属性 获取标签文本
    news_title = title_content.text
    # get_attribute("属性名") 方法获取属性值
    news_href = title_content.get_attribute("href")
    print(f"新闻标题: {news_title}, 新闻地址: {news_href}")
```



## 多学一招


```python
# 元素查找 通过 css 选择器 查找元素
kw_ele = firefox_driver.find_element(By.CSS_SELECTOR, "#k123")
print(kw_ele.get_attribute("outerHTML"))
```


>  如果元素未找到， 会抛出错误， 错误类型 NoSuchElementException， 错误信息如下

```
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: #k123; 
```

所以， 当查找元素时， 最好 使用  `try ... except...  ` 捕获异常，大多数场景下无法确保查找的元素百分百存在

```python
# 元素查找 通过 css 选择器 查找元素
try:
    kw_ele = firefox_driver.find_element(By.CSS_SELECTOR, "#k123")
    print(kw_ele.get_attribute("outerHTML"))
except NoSuchElementException:
    exit("未找到元素")
```


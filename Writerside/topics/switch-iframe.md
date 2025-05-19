# 切换 iframe

iframe 技术目前使用的频率越来越少了，仅作为笔记

比如以下页面

```HTML
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    
    <div id="box1"></div>
    <iframe id="page1" name="name2" src="https://www.abc.com" >
        <div id="box2"></div>
    </iframe>
    
</body>
</html>
```

默认情况下， 直接查找 id 属性值为 box2 的元素， 是无法找到的，毕竟 iframe 是一个单独的页面

需要先切换 iframe 页面， 再查找 id 属性值为 box2 的元素

```py
# 切换 iframe
firefox_driver.switch_to.frame("page1")
# 查找 id 属性值为 box2 的元素
firefox_driver.find_element(By.CSS_SELECTOR, "#box2")
```

switch_to.frame() 方法用于切换 iframe, 参数值可以是id属性值， 也可以是name属性值，源码如下


```Py
def frame(self, frame_reference: Union[str, int, WebElement]) -> None:
    if isinstance(frame_reference, str):
        try:
            frame_reference = self._driver.find_element(By.ID, frame_reference)
        except NoSuchElementException:
            try:
                frame_reference = self._driver.find_element(By.NAME, frame_reference)
            except NoSuchElementException as exc:
                raise NoSuchFrameException(frame_reference) from exc

    self._driver.execute(Command.SWITCH_TO_FRAME, {"id": frame_reference})
```

通过源码知道， iframe 切换时， 先尝试使用 ID 属性， 如果未找到，就使用 name 属性

假如 iframe 标签有 id 属性， 使用 id 属性，没有 id 属性， 使用 name 属性


```HTML

    <iframe  src="https://www.abc.com" >
        <div id="box2"></div>
    </iframe>
    
    <iframe  src="https://www.123.com" >
        <div id="box3"></div>
    </iframe>

```



假如 iframe 标签既没有id属性，也没有name属性， 也可以使用索引

索引从 1 开始， 1 表示第一个iframe, 2 表示第二个iframe

```python
firefox_driver.switch_to.frame(1)
```


## 退出 iframe


```HTML
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    
    <div id="box1"></div>
    <iframe id="page1" name="name2" src="https://www.abc.com" >
        <div id="box2"></div>
    </iframe>
    
</body>
</html>
```

当切换到 iframe 后，无法查询父页面的元素， 比如： id 属性为 box1 的标签无法找到

需要退出 iframe 后，才能查找父页面的元素

```
# 退出 iframe
firefox_driver.switch_to.parent_frame()
```

## 扩展知识

假如 iframe 嵌套 iframe ，比如


```html
<iframe id="page1"  src="https://www.abc.com" >
    <iframe id="page2"  src="https://www.123.com" >
        <iframe id="page3"  src="https://www.456.com" ></iframe>
    </iframe>
</iframe>
```

```Py
# 切换到 id属性值为page3的页面
firefox_driver.switch_to.frame("page1")
firefox_driver.switch_to.frame("page2")
firefox_driver.switch_to.frame("page3")
```

退出时(switch_to.parent_frame()执行一次就退出一个iframe)

```Py
firefox_driver.switch_to.parent_frame()
firefox_driver.switch_to.parent_frame()
firefox_driver.switch_to.parent_frame()
```
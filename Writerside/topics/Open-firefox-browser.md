# 打开 火狐浏览器

# 打开火狐浏览器

启动火狐浏览器

```bash
from selenium.webdriver import Firefox

# 打开浏览器
firefox_driver = Firefox()
```

> 第一次启动浏览器可能并不顺利， 主要有以下两个原因：
>
> 1. 找不到浏览器
> 2. 找不到浏览器驱动

如果你经过长时间的等待， 浏览器仍然无法启动，可以通过以下方法配置浏览器路径和驱动路径


<tabs>
<tab title="Linux">
<code-block lang="python">
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
</code-block>
</tab>

<tab title="Windows">
<code-block lang="python">
待补充
</code-block>
</tab>

</tabs>



## 访问指定页面

访问百度

```bash
# 访问 百度
baidu_url = "https://www.baidu.com/"
firefox_driver.get(baidu_url)
```



## 浏览器窗口大小设置

> 假如浏览器窗口大小太小， 页面的元素会被遮挡， 被遮挡的元素可能无法执行模拟操作，比如： 点击、输入等
>
> 通常在浏览器打开之后设置窗口大小


<tabs>
<tab title="窗口最大化">
<code-block lang="Python">
# 设置窗口最大化
firefox_driver.maximize_window()
</code-block>
</tab>
<tab title="自定义大小(1600x900)">
<code-block lang="Python">
# 设置窗口大小 1600x900
firefox_driver.set_window_size(1600, 900)
</code-block>
</tab>
</tabs>



selenium 框架提供了 get_window_size() 方法获取窗口大小， 

- 返回值类型: 字典，
  - 使用 **width** 获取宽度
  - 使用 **height** 获取高度

```python
# 获取窗口大小
window_size = firefox_driver.get_window_size()

print(window_size["width"], window_size["height"])
```






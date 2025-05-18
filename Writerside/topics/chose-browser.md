# 选择浏览器

## 常用浏览器

|                | 浏览器下载地址      | 驱动下载地址         | 浏览器版本VS驱动版本一致性 |
|----------------|--------------|----------------|----------------|
| 火狐浏览器          | 官网正常访问       | 正常访问(开源GitHub) | 一般（通常最新版即可）    |
| Google  Chrome | 官网正常访问       | 镜像站下载          | 严格版本匹配         |
| Microsoft Edge | 官网正常访问(系统自带) | 官网正常访问         | 严格版本匹配         |

|                | 浏览器下载地址                                                                         | 驱动下载地址                                                                          |
|----------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| 火狐浏览器          | [点击链接访问](http://firefox.com.cn/download/#product-desktop-release)               | [点击链接访问](https://github.com/mozilla/geckodriver/releases)                       |
| Google  Chrome | [点击链接访问](https://googlechromelabs.github.io/chrome-for-testing/)                | [点击链接访问](https://googlechromelabs.github.io/chrome-for-testing/)                |
| Microsoft Edge | [点击链接访问](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) | [点击链接访问](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) |

**如何查看Google Chrome浏览器版本**

通过浏览器地址栏输入 `chrome://version/` 查看版本号

**如何查看Edge浏览器版本**

通过浏览器地址栏输入 `edge://settings/help` 查看版本号

## 扩展知识

### Safari

内置驱动，无需额外下载，但需在「偏好设置」中启用「允许远程自动化」。

### Chromium 内核

**基于 Chromium 的浏览器**（如 QQ、360、Opera）

使用 ChromeDriver，需在代码中指定浏览器和驱动的路径。

### Internet Explorer（IEDriverServer）**

1. **下载地址**  
   • https://selenium-release.storage.googleapis.com/index.html  
   • **推荐版本**：2.5.x 版本兼容 IE11。

2. **配置要求**  
   • 需在 IE 的「Internet 选项」中取消勾选「启用保护模式」并设置缩放为 100%。
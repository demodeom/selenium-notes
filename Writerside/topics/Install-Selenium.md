#  Selenium

## Selenium 简介 {id="selenium_1"}

Selenium 是一个用于 Web 应用程序自动化测试 的开源工具集，支持多种编程语言（如 Python、Java、C#、JavaScript 等）和浏览器（Chrome、Firefox、Edge 等）。它的核心功能是模拟用户与浏览器的交互（如点击、输入、导航等），主要用于自动化测试，也可用于网页数据抓取或自动化操作。
主要组件：

1. Selenium WebDriver
    - 核心工具，通过代码直接控制浏览器，实现自动化操作（如填写表单、点击按钮等）。 
    - 支持动态网页（处理 JavaScript 渲染的内容）。

2. Selenium IDE
   - 浏览器插件（Chrome/Firefox），提供图形化界面录制和回放操作，适合快速生成测试脚本。

3. Selenium Grid
    - 分布式测试工具，可在多台机器上并行运行测试，提高效率。

常见用途：

1. 自动化测试：验证网页功能是否正常（如登录、表单提交）。 
2. 数据抓取：爬取动态渲染的网页内容（如电商价格、社交媒体数据）。 
3. 自动化任务：自动完成重复性网页操作（如批量上传、定时签到）。


## 安装 Selenium

使用 pip 命令安装 Selenium

```bash
pip install selenium
```

## 多学一招

>  如果下载速度慢， 在命令中添加 **-i** 参数， 使用国内镜像下载

<tabs>
<tab title="清华大学镜像">
<code-block lang="bash">
pip install  selenium -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
</code-block>
</tab>
<tab title="阿里云">
<code-block lang="bash">
pip install  selenium -i https://mirrors.aliyun.com/pypi/simple/
</code-block>
</tab>
</tabs>

**国内其它可用的镜像**

|  镜像名称 | 镜像地址                                                   |
|---|------------------------------------------------------|
|  清华大学 | https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple |
|  阿里云 |    https://mirrors.aliyun.com/pypi/simple/   |
| 中国科技大学  |   https://pypi.mirrors.ustc.edu.cn/simple/        |
|  华为云 |     https://repo.huaweicloud.com/repository/pypi/simple/    |
|  腾讯云 |     https://mirrors.cloud.tencent.com/pypi/simple/    |



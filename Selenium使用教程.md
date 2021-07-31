# Selenium使用教程

## 一, selenium

```python
from selenium import webdriver		#导入selenium包
brower = webdriver.Chrome()		#实例化浏览器对象
url = "https://www.baidu.com/"		#打开链接
brower.get(url=url)				#打开链接
print(brower.page_source)			#打印获取页面信息
brower.close()						#关闭浏览器对象
```



## 二, selenium元素定位

```python
根据ID定位
browser.find_element_by_id("kw").send_keys("selenium")

根据name定位
browser.find_element_by_name("wd").send_keys("test")

根据class定位
browser.find_element_by_class_name("s_ipt").send_keys("test")

根据tag定位(有问题,报错)
browser.find_element_by_tag_name("input").send_keys("test")

根据link定位
browser.find_element_by_link_text("学术").click()

根据partial_link模糊定位
browser.find_element_by_partial_link_text("学").click()

根据xpath定位
browser.find_element_by_xpath('//*[@id="kw"]').send_keys("test")

根据css定位
browser.find_element_by_css_selector("#kw").send_keys("test")
```


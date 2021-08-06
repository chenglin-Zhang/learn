# Appium自动化测试





## 介绍

中文文档网址：http://appium.io/docs/cn/about-appium/intro/



### 1、启动项配置

参数参考：https://blog.csdn.net/ljl6158999/article/details/80594521



## ADB常用命令

| 命令                       | 作用           |
| -------------------------- | -------------- |
| adb connect 10.1.22.95     | 链接设备       |
| adb devices                | 查看设备       |
| adb kill-server            | 杀死进程       |
| adb start-server           | 启动进程       |
| adb pull 手机路径 电脑路径 | 手机文件传递pc |
| adb push 电脑路径 手机路径 | pc文件传递手机 |



## 基础操作api



### 获取应用包名应用名

```dockerfile
adb shell "dumpsys window | grep mFocusedApp"
```



### 1、应用内跳转页面

```python
driver.start_activity("包名","应用名")
```



### 2、获取应用包名 | 应用名

```python
print(driver.current_package)
print(driver.current_activity)
```



### 3、关闭 close_app() | 退出 quit()

```python
driver.close_app()
driver.quit()
```



### 4、判断app是否安装

```python
if driver.is_app_installed("com.aw.project.aldi"):
    driver.remove_app("com.aw.project.aldi")
else:
    driver.install_app(r"D:\DiskTop\ALDI_ACO_V8.7.0.6.apk")
```



### 5、进入后台返回前台

```python
driver.backgroud_app("放置后台时间,单位秒")
```





## 元素定位api



### 1、元素定位

```python
driver.find_element_by_id()
driver.find_element_by_class_name()
driver.find_element_by_xpath()
```

```python
driver.find_elements_by_id()
driver.find_elements_by_class_name()
driver.find_elements_by_xpath()
```



### 2、显示等待 | 隐式等待

隐式等待

```python
driver.implicitly_with(时间,单位秒)
```

显示等待

```python
WebDriverWait(driver, 超时时间, 间隔执行).until(lambda x:x.element)
```





## 元素操作api



### 1、点击 | 输入 | 清空

- send_keys()默认不输入中文,使用时需配置参数

  ```python
  desired_caps['unicodeKeyboard'] = True
  desired_caps['resetKeyboard'] = True
  ```

```python
element.click()
element.send_keys(value)
element.clear()
```



### 2、获取文本 | 获取位置 | 获取大小

```python
element.text
element.location
element.size
```



### 3、获取元素属性值

- value="text" 返回 text 值
- value="name" 返回 content-desc/text 值
- value="className" 返回 class 值，api=>18支持
- value="resourceid" 返回 resource-id 值，api=>18支持

```python
element.get_attribute("enable")
element.get_attribute("text")
element.get_attribute("name")
element.get_attribute("className")
element.get_attribute("resourcedId")
```



### 4、滑动 swipe() | scroll() | drage_and_drop()

```python
driver.swipe(x,y,x1,y1,持续时间:d.单位毫秒)
driver.scroll(element1,element2)
driver.drag_and_drop(element1,element2)
```





## 高级手势TouchAction



### 1、轻敲 tap()

```python
TouchAction(driver).tap(element).perform()
TouchAction(driver).tap(x=x, y=y, count=1).perform()
```



### 2、按下 press()| 抬起 release()

```python
TouchAction(driver).press(element | x,y).perform()
TouchAction(driver).release().perform()
```

按下后抬起

```python
TouchAction(driver).press(element | x,y).release().perform()
```



### 3、等待 wait() | 长按 long_press()

```python
TouchAction(driver).press(element | x,y).wait(2).perform()
TouchAction(dricer).long_press(element,duration=2000).perform()
```



### 4、移动 move_to()

```python
TouchAction(driver).press(100,100).move_to(100,200).perform()
```





## 手机操作API



### 1.获取设备分辨率 get_window_size()

```python
driver.get_window_size()		#{'height': 2560, 'width': 1440}
driver.get_window_size()['width']	# 1440
```



### 2、手机截图 get_screenshot_as_file()

```python
driver.get_screenshot_as_file('fileName.png')
```



### 3、获取网络属性 network_connection()

```python
Value (Alias)      | Data | Wifi | Airplane Mode
-------------------------------------------------
0 (None)           | 0    | 0    | 0
1 (Airplane Mode)  | 0    | 0    | 1
2 (Wifi only)      | 0    | 1    | 0
4 (Data only)      | 1    | 0    | 0
6 (All network on) | 1    | 1    | 0

from appium.webdriver.connectiontype import ConnectionType

class ConnectionType(object):
    NO_CONNECTION = 0
    AIRPLANE_MODE = 1
    WIFI_ONLY = 2
    DATA_ONLY = 4
    ALL_NETWORK_ON = 6
```

```python
driver.network_connection()
driver.set_network_connection(int:i)
```



### 4、发送键到设备 press_keycode()

https://blog.csdn.net/feizhixuan46789/article/details/16801429

| code                 | name         | Num  |
| -------------------- | ------------ | ---- |
| KEYCODE_CALL         | 拨号键       | 5    |
| KEYCODE_ENDCALL      | 挂机键       | 6    |
| KEYCODE_HOME         | 按键Home     | 3    |
| KEYCODE_MENU         | 菜单键       | 82   |
| KEYCODE_BACK         | 返回键       | 4    |
| KEYCODE_SEARCH       | 搜索键       | 84   |
| KEYCODE_CAMERA       | 拍照键       | 27   |
| KEYCODE_FOCUS        | 拍照对焦键   | 80   |
| KEYCODE_POWER        | 电源键       | 26   |
| KEYCODE_NOTIFICATION | 通知键       | 83   |
| KEYCODE_MUTE         | 话筒静音键   | 91   |
| KEYCODE_VOLUME_MUTE  | 扬声器静音键 | 164  |
| KEYCODE_VOLUME_UP    | 音量增加键   | 24   |
| KEYCODE_VOLUME_DOWN  | 音量减小键   | 25   |

```python
driver.press_keycode(keycode)
```



### 5、操作通知栏

- 打开通知栏

  ```python
  driver.open_notifications()
  ```

- 关闭通知栏

  ```python
  官方未提供关闭api,可使用返回键或滑动关闭
  driver.press_keycode(4)
  ```

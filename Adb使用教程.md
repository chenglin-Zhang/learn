# Adb使用教程

安装软件

```
安装软件
abd install
adb install <apk文件路径> :这个命令将指定的apk文件安装到设备上

卸载软件
adb uninstall <软件名>
adb uninstall -k <软件名> 如果加 -k 参数,为卸载软件但是保留配置和缓存文件.

进入设备或模拟器的shell
adb shell

发布端口
adb forward tcp:5555 tcp:8000

从电脑上发送文件到设备
adb push <本地路径> <远程路径>

从设备上下载文件到电脑
adb pull <远程路径> <本地路径>
```


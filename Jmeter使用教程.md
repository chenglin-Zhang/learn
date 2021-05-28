# Jmeter使用教程



## 命令行运行Jmeter

```
jmeter -n -t <testplan filename> -l <listener filename>
示例： jmeter -n -t testplan.jmx -l test.jtl


-h 帮助 -> 打印出有用的信息并退出
-n 非 GUI 模式 -> 在非 GUI 模式下运行 JMeter
-t 测试文件 -> 要运行的 JMeter 测试脚本文件
-l 日志文件 -> 记录结果的文件
-r 远程执行 -> 在Jmter.properties文件中指定的所有远程服务器
-H 代理主机 -> 设置 JMeter 使用的代理主机
-P 代理端口 -> 设置 JMeter 使用的代理主机的端口号

例如：jmeter -n -t test1.jmx -l logfile1.jtl -H 192.168.1.1 -P 8080
```


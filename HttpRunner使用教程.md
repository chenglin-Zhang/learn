# HttpRunner使用教程



> ##### 参考：https://www.ontheway.cool/HttpRunner3DocsForCN/

## 1、安装

```
pip install httprunner
pip install har2case

验证: hrun -V
	 har2case -V
```

## 2、五个命令

```
httprunner 主命令
1、hrun		httprunner run别名，运行yml、json、py测试用例
2、hmake		httprunner make别名，yml、json转py文件
3、har2case	httprunner har2case别名，har文件转yml、json文件
4、locust	性能测试
```

## 3、测试用例

- config：每个测试用例都必须有config部分，可以配置用例。
  1. **name(必须)：**测试用例的名称，将在log和报告中展示。
  2. **base_url(可选)：**测试用例中的通用Host，例如https://postman-echo.com。如果base_url被指定，测试步骤中的url只能写相对路径。当你要在不同环境下测试时，这个配置非常有用。
  3. **variables(可选的)：**定义的全局变量，作用域为整个用例。每个测试步骤都可以引用config variables。也就是说，step variables 优先级高于 config variables.
  4. **parameters(可选的)：**全局参数，用于实现数据化驱动，作用域为整个用例。
  5. **verify(可选的)：**指定是否验证服务器的TLS证书。如果我们想记录测试用例执行的HTTP流量，这将特别有用，因为如果没有设置verify或将其设置为True，则会发生SSLError。
  6. **export(可选的)：**指定输出的测试用例变量。将每个测试用例看作一个黑盒，config variables是输入变量，config export是输出变量。当一个测试用例在另一个测试用例的步骤中被引用时，config export将被提取并在随后的测试步骤中使用。

- teststeps：每个测试用例都有1个或多个测试步骤（List[step]），每个测试步骤对应一个API请求或其他用例的引用。

  1. **name(必须)**：name用来定义测试步骤 name，将出现在log和测试报告中

  2. **variables(可选的)：**测试步骤中定义的变量，作用域为当前测试步骤。如果想在多个测试步骤中共享变量，需要在config variables中定义。测试步骤中的变量，会覆盖config variables中的同名变量。

  3. extract(可选)：从当前 HTTP 请求的响应结果中提取参数，并保存到参数变量中（例如token），后续测试用例可通过$token的形式进行引用。

  4. validate(可选)：测试用例中定义的结果校验项，作用域为当前测试用例，用于实现对当前测试用例运行结果的校验。

     ```
     运算符包括:
     equal: 等于
     contained_by: 实际结果是否被包含在预期结果中
     contains: 预期结果是否被包含在实际结果中
     endswith: 以...结尾
     greater_or_equals: 大于等于
     greater_than: 大于
     length_equal: 长度等于
     length_greater_or_equals: 长度大于等于
     length_greater_than: 长度大于
     length_less_or_equals: 长度小于等于
     length_less_than: 长度小于
     less_or_equals: 小于等于
     less_than: 小于
     not_equal: 不等于
     regex_match: 字符串是否符合正则表达式匹配规则
     startswith: 以...开头
     string_equals: 字符串相等
     type_match: 类型是否匹配
     jmespath: jmespath表达式，详见JMESPath Tutorial
     expected_value: 指定期望值或变量，也可以调用方法
     message(optional): 用于描述断言失败原因
     ```

  5. hooks(可选)：

     ```
     setup_hooks函数放置于debugtalk.py中，并且必须包含三个参数：
     method: 请求方法，比如：GET,POST,PUT
     url: 请求URL
     kwargs: request的参数字典
     
     teardown_hooks函数放置于debugtalk.py中，并且必须包含一个参数:
     resp_obj: requests.Response实例
     ```

     

  6. variables：跟request中的variables一样

  7. testcase：指定引用的测试用例

  8. export：从引用的测试用例中提取的变量，该变量在后面的test steps中可以引用

     
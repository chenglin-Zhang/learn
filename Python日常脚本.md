# Python日常脚本



## 1、邮件发送

```

```

## 2、excel操作



## 3、数据库操作



## 4、os模块



## 5、进制转化

```
# 二进制 to 十进制: int(str,n=10) 
def bin2dec(string_num):
    return str(int(string_num, 2))
```

```
# 十进制 to 二进制: bin() 
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 2)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])
```

```
# 十六进制 to 二进制: bin(int(str,16)) 
def hex2bin(string_num):
    return dec2bin(hex2dec(string_num.upper()))
```

```
# 二进制 to 十六进制: hex(int(str,2)) 
def bin2hex(string_num):
    return dec2hex(bin2dec(string_num))
```


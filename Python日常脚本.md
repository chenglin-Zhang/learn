# Python日常脚本



## 1、邮件发送

```

```

## 2、excel操作

> xlrd-读取excel数据

```python
def get_date(self, path):
    '''
    获取SNJ-交易号、微信金额、支付宝金额数据
    :param path: SNJ报表路径
    :return: list数据
    '''
    wook_book = xlrd.open_workbook(path)
    sheet = wook_book.sheet_by_name("店铺租金收益报表")
    date_list = []
    for item in range(sheet.nrows):
        wechat_pay = sheet.row(item)[24].value
        ali_pay = sheet.row(item)[26].value
        transaction_no = sheet.row(item-1)[12].value
        if len(transaction_no.split('-')) == 4:
            ta_no = transaction_no.split('-')[3]
        else:
            ta_no = ""

        index = sheet.row(item)[1].value
        if index == "小计：":
            date_list.append({
                "transaction_no": transaction_no,
                "ta_no": ta_no,
                "wechat_pay": wechat_pay,
                "ali_pay": ali_pay
            })
    print("Success--GetData")
    return date_list
```

> xlwt--写入excel

```python
def set_date(self, date):
    '''
    根据获取的数据，把数据写入excel
    :param date:
    :return:
    '''
    work_book = xlwt.Workbook()
    new_sheet = work_book.add_sheet("Deal_Data", cell_overwrite_ok=True)
    new_sheet_sum = work_book.add_sheet("Sum", cell_overwrite_ok=True)
    index_list = []
    title = ['门店交易号', '交易号', '微信支付', '支付宝支付']
    for item in range(len(title)):
        new_sheet.write(0, item, title[item])
    for item in range(len(date)):
        new_sheet.write(item+1, 0, date[item]["transaction_no"])
        new_sheet.write(item+1, 1, date[item]["ta_no"])
        new_sheet.write(item+1, 2, date[item]["wechat_pay"])
        new_sheet.write(item+1, 3, date[item]["ali_pay"])
        if int(date[item]["wechat_pay"]) > 0:
            index_list.append(date[item]["wechat_pay"])
        if int(date[item]["ali_pay"]) > 0:
            index_list.append(date[item]["ali_pay"])
    print(r"Success--Sheet")
    index_list.sort(reverse=True)
    new_sheet_sum_title = ["金额", "", "汇总金额"]
    for item in range(len(new_sheet_sum_title)):
        new_sheet_sum.write(0, item, new_sheet_sum_title[item])
    new_sheet_sum.write(1, 2, sum(index_list))
    for item in range(len(index_list)):
        new_sheet_sum.write(item+1, 0, index_list[item])
    print(r"Success--SheetSum")
    work_book.save(r"C:\Users\Administrator\Downloads\1.xls")
    print(r"Success--Save--Path--C:\Users\Administrator\Downloads\1.xls")
```



## 3、数据库操作



## 4、os模块

```
dir_path = r"C:\Users\Administrator\Desktop\img"
for root, dir, files in os.walk(dir_path):
    for file in files:
        img_file = os.path.join(root, file)
        img = Image.open(img_file)
        img = circle_corner(img, radii)
        img_name = os.path.join(root, file.replace("jpg","png"))
        img.save(img_name, 'png', quality=1000)
        print(f"{img_name}-----文件已经生成")
```



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


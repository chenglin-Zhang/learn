import xlrd

path = r"C:\Users\shanzhi_feng_ext\Downloads\自营店铺明细报表.XLS"

book = xlrd.open_workbook(filename=path)
sheets = book.sheet_names()
for sheet in sheets:
    data = book.sheet_by_name(sheet)
    for line in range(data.nrows):
        col_date = data.row(line)[24].value
        if str(col_date) != "0.0":
            # print(type(col_date))
            print(data.row(line-1)[12].value, )

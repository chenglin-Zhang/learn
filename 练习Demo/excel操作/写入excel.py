import xlrd

class Read_excel(object):

    def __init__(self):
        file_path = r"C:\Users\shanzhi_feng_ext\Desktop\交易.xlsx"
        self.wook_book = xlrd.open_workbook(file_path)

    def get_all_date(self):
        for item in self.wook_book.sheet_names():
            date = self.wook_book.sheet_by_name(item)
            for row in range(date.nrows):
                for col in range(date.ncols):
                    val = date.row(row)[col].value
                    print(val)


if __name__ == '__main__':
    excel = Read_excel()
    excel.get_all_date()
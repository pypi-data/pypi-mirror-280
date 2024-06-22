import pyexcel
book = pyexcel.get_book(file_name="data.xls")
print(book['Sheet1'])
from pyecharts import Line
import xlrd


class Burn(object):
    def __init__(self, file_name, sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        if not isinstance(file_name, str):
            self._file_name = file_name
        else:
            self._file_name = file_name

    @property
    def sheet_name(self):
        return self._sheet_name

    @sheet_name.setter
    def sheet_name(self, sheet_name):
        if not isinstance(sheet_name, str):
            self._sheet_name = str(sheet_name)
        else:
            self._sheet_name = sheet_name

    def open_sheet(self):
        data = xlrd.open_workbook(self.file_name)
        sheet = data.sheet_by_name(self.sheet_name)
        rows = sheet.nrows
        cols = sheet.ncols
        print(rows, cols)
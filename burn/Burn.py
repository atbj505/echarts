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

    def get_data(self):
        """
        获取excel数据
        """
        data = xlrd.open_workbook(self.file_name)
        sheet = data.sheet_by_name(self.sheet_name)
        cols = sheet.ncols
        # 表头(日期，实际故事点，计划故事点)
        index = sheet.row_values(0)
        # 数据
        values = []
        for col in range(0, cols):
            values.append(sheet.col_values(col)[1:])
        return (index, values)

    def get_velocity(self, values):
        """
        计算速率
        """
        dates = values[0]
        plans = values[2]
        n = plans[-1] / dates[-1]
        velocities = []
        for date in dates:
            velocity = n * date
            velocities.append(velocity)
        return velocities

    def draw(self, index, values, velocities):
        """
        绘制
        """
        line = Line('燃尽图')
        line.add(index[1], values[0], values[1], is_label_show=True, xais_name="日期", yais_name="故事点",line_width=4)
        line.add(index[2], values[0], values[2], is_label_show=True, xais_name="日期", yais_name="故事点", line_width=4)
        line.add("速率", values[0], velocities, xais_name="时间", yais_name="故事点")
        line.render('Burn.html')
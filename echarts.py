#!/usr/bin/env python
# -*- coding: utf-8 -*-

import optparse
import sqlite3

from pyecharts import Line


class Burn():
    def __init__(self):
        self.conn = sqlite3.connect('point.db')
        self.cursor = self.conn.cursor()

    def draw_line(self, point):
        if point[0] == 0:
            pre_expect = self.cursor.execute(
                'select expect_point from t_point order by rowid desc LIMIT 1'
            ).fetchall()
            if not pre_expect:
                raise ValueError('invalid value')
            self.cursor.execute('insert into t_point values(%d, %d)' %
                                (pre_expect[0][0], point[1]))
        else:
            self.cursor.execute('insert into t_point values(%d, %d)' %
                                (point[0], point[1]))
        points = self.cursor.execute(
            'select expect_point, real_point from t_point').fetchall()
        start_day = 15
        attr = [str(x) for x in range(start_day, start_day + len(points))]
        v1 = [x[0] for x in points]
        v2 = [x[1] for x in points]
        v3 = self.calculate_velocity([x for x in range(0, len(v2))], 30,
                                     max(v1))
        line = Line('燃尽图')
        line.add(
            "预期故事点",
            attr,
            v1,
            is_label_show=True,
            xaxis_name="日期",
            yaxis_name="故事点",
            line_width=4)
        line.add(
            "预期速率",
            attr,
            v3,
            is_smoth=True,
            xaxis_name="日期",
            yaxis_name="故事点",
            line_type="dotted")
        line.add(
            "实际故事点",
            attr,
            v2,
            is_label_show=True,
            xaxis_name='日期',
            yaxis_name="故事点",
            mark_point=[{
                "coord": [attr[-1], point[1]],
                "name": "今日完成任务"
            }],
            line_width=4)
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
        line.render()

    def calculate_velocity(self, points, x_dates, y_points):
        n = y_points // x_dates
        velocities = []
        for point in points:
            y = n * point
            velocities.append(y)
        return velocities

    def set_optparse(self):
        p = optparse.OptionParser()
        p.add_option(
            "-e",
            "--expect_point",
            action="store",
            default=None,
            help="enter expect point")

        p.add_option(
            "-r",
            "--real_point",
            action="store",
            default=None,
            help="enter real point")
        options, argument = p.parse_args()

        if options.expect_point and options.real_point:
            self.draw_line((int(options.expect_point),
                            int(options.real_point)))
        elif options.real_point:
            self.draw_line((0, int(options.real_point)))

    def set_database(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS "t_point" (
                "expect_point" integer(20),
                "real_point" integer(20)
            );
        '''
        self.cursor.execute(sql)


if __name__ == "__main__":
    burn = Burn()
    burn.set_database()
    burn.set_optparse()

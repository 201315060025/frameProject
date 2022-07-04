# encoding: utf-8
"""
画图类说明
"""
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Page


class DrawPic(object):
    def __init__(self):
        pass

    def tab0(self, name, color):  # 标题
        c = (Pie().
            set_global_opts(
            title_opts=opts.TitleOpts(title=name, pos_left='center', pos_top='center',
                                      title_textstyle_opts=opts.TextStyleOpts(color=color, font_size=20))))
        return c

    def tab1(self, name, color):  # 标题
        c = (Pie().
            set_global_opts(
            title_opts=opts.TitleOpts(title=name, pos_left='center', pos_top='center',
                                      title_textstyle_opts=opts.TextStyleOpts(color=color, font_size=30))))
        return c

    def tab2(self, name, color):
        c = (Pie().
            set_global_opts(
            title_opts=opts.TitleOpts(title=name, pos_left='center', pos_top='center',
                                      title_textstyle_opts=opts.TextStyleOpts(color=color, font_size=25))))
        return c

    def line(self, all_time, all_cpu):
        line = (
            Line()
                .add_xaxis(all_time)
                .add_yaxis("CPU_info：%", all_cpu)
                .set_global_opts(title_opts=opts.TitleOpts(title="CPU_info"))
        )
        line.render()

        return line

    def line1(self, all_time, all_mem_percent):
        line = (
            Line()
                .add_xaxis(all_time)
                .add_yaxis("Mem_percent：%", all_mem_percent)
                .set_global_opts(title_opts=opts.TitleOpts(title="内存使用占比"))
        )
        line.render()

        return line

    def bar(self, disk_percent):
        bar = (Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))  # 在这里输入啊，设置绘图主题为CHALK
               .add_xaxis(["C盘", "D盘", "E盘", "F盘", "G盘"])
               .add_yaxis("磁盘使用占比：%", disk_percent))
        bar.render()
        return bar

    def pie_base(self, mem_data):
        c = (
            Pie()
                .add("", [list(z) for z in zip(['mem_free', 'mem_used'],
                                               [mem_data[0][0], mem_data[0][3]])])
                .set_global_opts(title_opts=opts.TitleOpts(title="内存使用占比"))
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )
        return c


    def generate_page(self):
        page = Page()
        page.add(
            self.tab0("Python数据分析实例", "#2CB34A"),
            self.line(all_time, all_cpu),
            self.tab1("系统信息监控数据可视化大屏", "#2CB34A"),
            self.tab2("可用内存:{mem_free}\n\n总内存:{mem_total}\n\n内存占比:{mem_percent}\n\n占用内存:{mem_used}".format(
                mem_free=mem_data[0][0], mem_total=mem_data[0][1], mem_percent=mem_data[0][2], mem_used=mem_data[0][3]),
                 "#000000"),
            self.bar(disk_percent),
            self.pie_base(),
            self.line1(all_time, all_mem_percent)
        )
        page.render("html/data_center.html")


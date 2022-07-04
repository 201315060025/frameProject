# encoding: utf-8

from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Page
from pyecharts.globals import ThemeType
from format_data import cpu_info_data,memory_used_data, memory_rank_data


def cpu_info_graphical():
    """生成cpu 信息的使用率折线图"""
    data = cpu_info_data()
    # <editor-fold des="">
    c = (
        Line()
            .add_xaxis(data[0])
            .add_yaxis("数量", data[1])
            .set_global_opts(title_opts=opts.TitleOpts(title="Cpu info"))
    )

    c.width = "100%"
    html = c.render_notebook()
    return html


def memory_used_graphical():
    """内存使用率的饼状图"""
    data = memory_rank_data()
    c = (
        Pie()
            .add(
            "",
            # [["a",10], ["b", 90]]
            data
            ,
            center=["40%", "50%"],
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="内存使用占比"),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

    )
    c.width = "100%"
    # </editor-fold>
    html = c.render_notebook()
    return html


def memory_used_line_graphical():
    """内存使用率折线图"""
    data = memory_used_data()
    # <editor-fold des="">
    c = (
        Line()
            .add_xaxis(data[0])
            # .add_yaxis("时间", Faker.values())
            .add_yaxis("数量", data[2])
            .set_global_opts(title_opts=opts.TitleOpts(title="内存使用占比"))

    )

    c.width = "100%"
    html = c.render_notebook()
    return html

if __name__ == '__main__':
    pass
# encoding: utf-8
import time, os
import pandas as pd
import numpy as np
from pywebio.input import NUMBER, TEXT
from pywebio.input import input, textarea, select, checkbox, radio, slider, actions, file_upload
from pywebio.input import input_group, input_update
from pywebio.output import put_text, put_markdown, put_buttons, put_scope, get_scope, put_info, put_warning, put_error, \
    put_success, put_html, put_link, put_processbar, put_loading, put_code, put_table, put_button, put_buttons, \
    put_image, put_file, put_tabs, put_collapse, put_scrollable, put_widget, put_row, put_column, put_grid
from pywebio.output import popup, toast, span, style
from pywebio import start_server

# 导入本地文件
# from generate_pie_data import generate_pie, generate_pie_remark, generate_data_from as pie_data_source
# from generate_link_data import generate_link, generate_link_remark
# from data import data_to_table
from graphical import cpu_info_graphical, memory_used_graphical, memory_used_line_graphical
from init_info import *

current_workspace = os.path.join(os.path.dirname(os.path.abspath(__file__)))
out_path = os.path.join(current_workspace, 'output')
'''pywebio中 Input组件介绍:
input(), 输入框
textarea(), 多行文本输入框
select(), 下拉选框
checkbox(), 多(复)选框
radio(), 单选框
slider(), 进度条
file_upload(), 文件上传按钮
actions(), 按钮
input_group(), 是以上几个组件的一个组合，我们可以认为是一个表单：Input group
input_update(), 动态更新组件的内容：Update attributes of input field
input_control(), 发送input命令，监听事件，验证输入项，返回结果

注意事项: 单个标签不能添加name属性，input_group中需要添加name属性。
'''



def main():
    # 网页标题
    put_markdown('''# 系统信息监控可视化大屏系统''')
    put_row(
        content=[
            put_html(cpu_info_graphical())]
        ),
    put_row([put_text('')])

    put_row(
        content=[
            put_html(memory_used_graphical()),
            None,
            put_html(memory_used_line_graphical()
                     )]
        , size='60% 5px 40%'),
    put_row([put_text('')])

    pass



if __name__ == "__main__":
    start_server(main, debug=True, port=8083)
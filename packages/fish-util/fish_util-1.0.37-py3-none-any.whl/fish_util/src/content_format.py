# author: delta1037
# Date: 2022/01/08
# mail:geniusrabbit@qq.com
import datetime

import dateutil.parser


# 获取mention的格式
import NotionDump


def get_mention_format(mention_content):
    return "@(" + mention_content + ")"


# 获取page的格式 运行过程中只填充id，后续调整页面供定位使用
def get_page_format_md(page_id, page_name, export_child):
    if export_child:
        return "[" + page_id + "]()"
    else:
        return "[" + page_name + "](" + page_id + ")"


# 数据库title格式
def get_database_title_format(title_id, title_ret, export_child):
    if export_child:
        return "[" + title_id + "]()"
    else:
        # 不导出子页面直接把标题填上去
        return title_ret


# 获取page的格式 纯文本只填充名字即可
def get_page_format_plain(page_name):
    return page_name


# 封装URL的格式
def get_url_format(url_plain, name="link"):
    return "[" + name + "](" + url_plain + ")"


def format_date_or_time(date_time):
    # print(date_time)
    t_datetime = dateutil.parser.parse(date_time)
    # print(date_time, t_datetime)
    if date_time.find('T') != -1:
        # datetime
        return t_datetime.strftime(NotionDump.FORMAT_DATETIME)
    else:
        # date
        return t_datetime.strftime(NotionDump.FORMAT_DATE)


# 封装date的格式
def get_date_format(start, end):
    ret_str = ""
    if start is not None:
        ret_str = format_date_or_time(start)
    if end is not None:
        ret_str += " ~ " + format_date_or_time(end)  # 日期之间用“~”分割
    return ret_str


# 封装文件链接格式
def get_file_format_md(filename, file_url, file_id="", export_child=False):
    if export_child:
        if file_id == "":
            return "[" + filename + "](" + file_url + ")"
        else:
            # 等待重定位
            return "[" + file_id + "]()"
    else:
        # 不导出子页面直接把标题填上去
        return "[" + filename + "](" + file_url + ")"


# 封装文件链接格式
def get_file_format_plain(filename, file_url):
    return filename + "(" + file_url + ")"


# 行内公式格式
def get_equation_inline(equation):
    return "$ " + equation + " $"


# 块级公式格式
def get_equation_block(equation):
    return "$$ " + equation + " $$"


def color_transformer(input_color, background=False):
    if background:
        color_str = "b_" + input_color
    else:
        color_str = "f_" + input_color
    color_ret = ""
    if NotionDump.S_THEME_TYPE == "dark":
        # dark
        if color_str in NotionDump.S_THEME_DARK:
            color_ret = NotionDump.S_THEME_DARK[color_str]
    elif NotionDump.S_THEME_TYPE == "self_define":
        # self_define
        if color_str in NotionDump.S_THEME_SELF_DEFINE:
            color_ret = NotionDump.S_THEME_SELF_DEFINE[color_str]
    else:
        # default light
        if color_str in NotionDump.S_THEME_LIGHT:
            color_ret = NotionDump.S_THEME_LIGHT[color_str]
    if color_ret != "":
        return color_ret
    return input_color


def color_transformer_db(input_color):
    if input_color == "default":
        color_str = "d_light_gray"
    else:
        color_str = "d_" + input_color

    color_ret = ""
    if NotionDump.S_THEME_TYPE == "dark":
        # dark
        if color_str in NotionDump.S_THEME_DARK:
            color_ret = NotionDump.S_THEME_DARK[color_str]
    elif NotionDump.S_THEME_TYPE == "self_define":
        # self_define
        if color_str in NotionDump.S_THEME_SELF_DEFINE:
            color_ret = NotionDump.S_THEME_SELF_DEFINE[color_str]
    else:
        # default light
        if color_str in NotionDump.S_THEME_LIGHT:
            color_ret = NotionDump.S_THEME_LIGHT[color_str]
    if color_ret != "":
        return color_ret
    return input_color

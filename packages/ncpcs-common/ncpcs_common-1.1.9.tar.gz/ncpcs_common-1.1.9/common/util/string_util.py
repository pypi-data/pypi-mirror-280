import re

BEST_LEN = 15
# 常见的单字和复姓列表
common_surnames = [
    "李", "王", "张", "刘", "陈", "杨", "黄", "赵", "周", "吴",
    "徐", "孙", "马", "朱", "胡", "林", "郭", "何", "高", "罗",
    "郑", "梁", "谢", "宋", "唐", "许", "韩", "冯", "邓", "曹",
    "彭", "曾", "肖", "田", "董", "袁", "潘", "于", "蒋", "蔡",
    "余", "杜", "叶", "程", "苏", "魏", "吕", "丁", "任", "沈",
    "姚", "卢", "姜", "崔", "钟", "谭", "陆", "汪", "范", "金",
    "石", "廖", "贾", "夏", "韦", "傅", "方", "白", "邹", "孟",
    "熊", "秦", "邱", "江", "尹", "薛", "闫", "段", "雷", "侯",
    "龙", "史", "陶", "黎", "贺", "顾", "毛", "郝", "龚", "邵",
    "万", "钱", "严", "赖", "覃", "洪", "武", "莫", "孔", "汤",
    "习", "尤", "苗", "俞", "鲍", "章", "施", "窦", "岑", "乐",
    "成", "詹", "欧阳", "司马", "端木", "上官",  # 复姓
]


def any_match(string, match_list):
    result = []
    for match in match_list:
        if string.find(match) != -1:
            result.append(match)
    return result


def any_match_bool(string, match_list):
    for match in match_list:
        if string.find(match) != -1:
            return True
    return False


def extract_digit(string):
    result = ""
    for ch in string:
        if ch.isdigit():
            result += ch
    return result


def find_all(string, substring):
    positions = []
    start = string.find(substring)

    while start != -1:
        positions.append(start)

        # 更新起始位置为当前子串后面的位置
        start += len(substring)
        next_pos = string[start:].find(substring)
        if next_pos == -1:
            break
        start = next_pos + start

    return positions

#去掉所有的空格、回车等特殊符号
def remove_special_symbols(string):
    return string.replace("\n", "").replace("\r", "").replace("\b", "").replace("\t", "").replace(" ", "").replace('', '')

def remove_bracket(string):
    return string.replace("(", "").replace(")", "").replace("（", "").replace("）", "")

def has_chinese(sentence):
    for ch in sentence:
        if is_chinese(ch):
            return True
    return False


# ---------------------------功能:判断字符是不是汉字-------------------------------
def is_chinese(char):
    if '\u4e00' <= char <= '\u9fff':
        return True
    return False


def handle_short_sentence(segment_list):
    temp_split_pos_list = []
    i = 0
    while i < len(segment_list) - 1:
        cur_seg_begin, cur_seg_end = segment_list[i]
        next_seg_begin, next_seg_end = segment_list[i+1]
        if cur_seg_end - cur_seg_begin < BEST_LEN and next_seg_end - next_seg_begin < BEST_LEN:
            temp_split_pos_list.append((cur_seg_begin, next_seg_end))
            i += 2
        else:
            temp_split_pos_list.append((cur_seg_begin, cur_seg_end))
            i += 1
    if i < len(segment_list):
        temp_split_pos_list.append(segment_list[i])
    return temp_split_pos_list


def split_text(text, pattern="。"):
    if text == '-':
        return []
    split_pos_list = []
    begin = 0
    for match in re.finditer(pattern, text):
        pos = match.start()
        split_pos_list.append((begin, pos))
        begin = pos+1
    split_pos_list.append((begin, len(text)))

    #TODO 长句处理
    #短句处理
    split_pos_list = handle_short_sentence(split_pos_list)
    split_text_list = []
    for begin, end in split_pos_list:
        if begin >= end:
            continue
        split_text_list.append(text[begin: end])
    return split_text_list


def locate_two_word(content, word1, word2, keep_order=True):
    word1_index_list = find_all(content, word1)
    word2_index_list = find_all(content, word2)

    if not word1_index_list or not word2_index_list:
        return None

    index_tuple_list = []
    for word1_index in word1_index_list:
        for word2_index in word2_index_list:
            index_tuple_list.append((word1_index, word2_index))

    index_tuple_list.sort(key=lambda ele: abs(ele[0]-ele[1]))
    if keep_order:
        for index_tuple in index_tuple_list:
            if index_tuple[0] < index_tuple[1]:
                return index_tuple
    return index_tuple_list[0]


def cut_from_back_to_front(text, length):
    if length <= len(text):
        return text[-length:]
    return text


def is_chinese_name(name):
    # 正则表达式检查全部为中文字符
    if not re.match(r'^[\u4e00-\u9fa5]+$', name):
        return False

    # 检查名字长度为2到4个汉字
    if len(name) < 2 or len(name) > 4:
        return False

    # 检查是否以常见姓氏开头
    if any(name.startswith(surname) for surname in common_surnames):
        return True

    return False

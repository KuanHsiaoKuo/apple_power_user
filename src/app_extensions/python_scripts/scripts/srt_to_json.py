import re
import json
import spacy
import sys


def parse_time(time_string):
    hours = int(re.findall(r'(\d+):\d+:\d+,\d+', time_string)[0])
    minutes = int(re.findall(r'\d+:(\d+):\d+,\d+', time_string)[0])
    seconds = int(re.findall(r'\d+:\d+:(\d+),\d+', time_string)[0])
    milliseconds = int(re.findall(r'\d+:\d+:\d+,(\d+)', time_string)[0])

    return (hours * 3600 + minutes * 60 + seconds) * 1000 + milliseconds


def parse_srt(srt_string):
    srt_list = []

    for line in srt_string.split('\n\n'):
        if line != '':
            index = int(re.match(r'\d+', line).group())

            pos = re.search(r'\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+',
                            line).end() + 1
            content = line[pos:]
            start_time_string = re.findall(
                r'(\d+:\d+:\d+,\d+) --> \d+:\d+:\d+,\d+', line)[0]
            end_time_string = re.findall(
                r'\d+:\d+:\d+,\d+ --> (\d+:\d+:\d+,\d+)', line)[0]
            start_time = parse_time(start_time_string)
            end_time = parse_time(end_time_string)

            srt_list.append({
                'index': index,
                'content': content,
                'start': start_time,
                'end': end_time
            })

    return srt_list


def remove_modals(total_words: list):
    modal_words = ['Yeah', 'yeah', 'Yep', 'yep', 'Uh', 'uh', 'okay', 'oh', 'Um', 'um', 'right']
    # 替换为删除线
    for index, word in enumerate(total_words):
        if word in modal_words:
            total_words[index] = f"~~{word}~~"


# 从当前位置开始，前/后找到一个有效位置
def find_valid_index(words_list: list, index, direction):
    if direction == 'pre':
        while index >= 0 and words_list[index].startswith("~~"):
            index -= 1
        if index >= 0:
            return index
        else:
            return None
    elif direction == 'after':
        while index < len(words_list) - 1 and words_list[index].startswith("~~"):
            index += 1
        if index < len(words_list):
            return index
        else:
            return None
    else:
        sys.exit('方向不对')


# 去除三个以内的重复词
def delete_duplicate(words_list: list):
    for index, word in enumerate(words_list):
        if word.startswith('~~'):
            continue
        # 以index为中心点向两边找
        pre_word_third, pre_word_secondary, pre_word, word_secondary, word_third = '', '', '', '', ''
        pre_index = find_valid_index(words_list, index - 1, 'pre')
        if pre_index:
            pre_word = words_list[pre_index]
        if pre_word:
            pre_index = find_valid_index(words_list, pre_index - 1, 'pre')
            if pre_index:
                pre_word_secondary = words_list[pre_index]
        if pre_word_secondary:
            pre_index = find_valid_index(words_list, pre_index - 1, 'pre')
            if pre_index:
                pre_word_third = words_list[pre_index]
        after_index = find_valid_index(words_list, index + 1, 'after')
        if after_index:
            word_secondary = words_list[after_index]
        if word_secondary:
            after_index = find_valid_index(words_list, after_index + 1, 'after')
            if after_index:
                word_third = words_list[after_index]
        # 先判断三个词的情况：
        if [pre_word_third, pre_word_secondary, pre_word] == [word, word_secondary, word_third]:
            print([pre_word_third, pre_word_secondary, pre_word])
            words_list[index], words_list[index + 1], words_list[index + 2] = \
                f"~~{words_list[index]}~~", f'~~{words_list[index + 1]}~~', f'~~{words_list[index + 2]}~~'
        elif [pre_word_secondary, pre_word] == [word, word_secondary]:
            print([pre_word_secondary, pre_word])
            words_list[index], words_list[index + 1] = \
                f"~~{words_list[index]}~~", f'~~{words_list[index + 1]}~~'
        elif pre_word == word:
            print(pre_word)
            words_list[index] = f"~~{words_list[index]}~~"
        # print(pre_word_third, pre_word_secondary, pre_word, word, word_secondary, word_third)
    return words_list


def parse_sentence(srt_strings: list):
    raw_total_words = ' '.join([item['content'] for item in srt_strings]).split(' ')
    total_words = [item.strip() for item in raw_total_words]
    # 借助python的默认用法：容器类型（列表、字典、对象等）在函数参数是传地址，原生类型(字符串、数字等)在函数参数是传值。
    remove_modals(total_words)
    delete_duplicate(total_words)
    # python -m spacy download en_core_web_sm
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(' '.join(total_words))
    # for sent in doc.sents:
    #     print(sent.text_with_ws.replace(' ', ' '))
    #     print('\n')
    # print('#' * 50)
    sents = [sent.text_with_ws.replace('  ', ' ') for sent in doc.sents]
    return sents


if __name__ == "__main__":
    srt_filename = 'Substrate Execute Block Code Walkthrough with Joe Petrowski and Shawn Tabrizi.srt'
    json_out_filename = srt_filename.replace('.srt', '.json')
    md_out_filename = srt_filename.replace('.srt', '.md')
    srt = open(srt_filename, 'r', encoding="utf-8").read()
    parsed_srt = parse_srt(srt)
    # parse_txt(parsed_srt)
    sentences = parse_sentence(parsed_srt)
    # open(json_out_filename, 'w', encoding="utf-8").write(
    #     json.dumps(parsed_srt, indent=2, sort_keys=True))
    # open(txt_out_filename, 'w', encoding='utf-8').write(
    #     '\n'.join([item['content'] for item in parsed_srt])
    # )
    open(md_out_filename, 'w', encoding='utf-8').write(
        '\n\n'.join(sentences)
    )

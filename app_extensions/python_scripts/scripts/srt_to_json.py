import re
import json
import spacy


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


def parse_txt(srt_strings: list):
    modal_words = ['Um', ' um ', 'Yeah', 'yeah', 'Uh', 'uh']
    conjunction_words = ['to', 'which', 'where', ',', 'gonna', 'through', 'and', 'this', 'of', 'the', 'called', 'an',
                         'is', 'get']
    lines = []
    line = ''
    last_start = 0
    for item in srt_strings:
        start, component = item['start'], item['content']
        for word in modal_words:
            component = component.replace(word, ',')
        delta = start - last_start
        # print(delta)
        end_word = line.split(' ')[-1]
        start_word = component.split(' ')[0]
        # 如果这一部分以连接词开头，或者上一行以连接词结尾
        if start_word in conjunction_words or end_word in conjunction_words:
            line += ' ' + component
        else:
            if line:
                print(line)
            line = component
        # print(component)
        # if delta < 3000:
        #     line += ' ' + component
        # else:
        #     print(line)
        #     line = ''
        last_start = start
    # print(lines)


def parse_sentence(srt_strings: list):
    modal_words = ['Yeah', 'yeah', 'Yep', 'yep', 'Uh', 'uh', 'okay', 'oh']
    special_words = ['Um', 'um']
    total_words = ' '.join([item['content'] for item in srt_strings])
    for word in special_words:
        total_words = total_words.replace(f" {word} ", ' ')
    for word in modal_words:
        total_words = total_words.replace(word, ' ')
    # python -m spacy download en_core_web_sm
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(total_words)
    # for sent in doc.sents:
    #     print(sent.text_with_ws.replace(' ', ' '))
    #     print('\n')
        # print('#' * 50)
    return [sent.text_with_ws.replace('  ', ' ') for sent in doc.sents]


if __name__ == "__main__":
    srt_filename = 'Substrate Execute Block Code Walkthrough with Joe Petrowski and Shawn Tabrizi.srt'
    json_out_filename = srt_filename.replace('.srt', '.json')
    txt_out_filename = srt_filename.replace('.srt', '.txt')
    srt = open(srt_filename, 'r', encoding="utf-8").read()
    parsed_srt = parse_srt(srt)
    # parse_txt(parsed_srt)
    sentences = parse_sentence(parsed_srt)
    # open(json_out_filename, 'w', encoding="utf-8").write(
    #     json.dumps(parsed_srt, indent=2, sort_keys=True))
    # open(txt_out_filename, 'w', encoding='utf-8').write(
    #     '\n'.join([item['content'] for item in parsed_srt])
    # )
    open(txt_out_filename, 'w', encoding='utf-8').write(
        '\n\n'.join(sentences)
    )

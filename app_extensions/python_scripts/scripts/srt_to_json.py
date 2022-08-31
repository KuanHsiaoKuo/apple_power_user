import re
import json
from sys import argv


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


if __name__ == "__main__":
    srt_filename = 'Substrate Execute Block Code Walkthrough with Joe Petrowski and Shawn Tabrizi.srt'
    json_out_filename = srt_filename.replace('.srt', '.json')
    txt_out_filename = srt_filename.replace('.srt', '.txt')
    srt = open(srt_filename, 'r', encoding="utf-8").read()
    parsed_srt = parse_srt(srt)
    open(json_out_filename, 'w', encoding="utf-8").write(
        json.dumps(parsed_srt, indent=2, sort_keys=True))
    open(txt_out_filename, 'w', encoding='utf-8').write(
        '\n'.join([item['content'] for item in parsed_srt])
    )

import os
import re
import sys


# brew install ffmpeg


def supported_merge(file_list, target_dir):
    """
    ffmpeg只支持默认格式合并:
    Unsupported audio codec. Must be one of mp1, mp2, mp3, 16-bit pcm_dvd, pcm_s16be, ac3 or dts.
    :param file_list:
    :param target_dir:
    :return:
    """
    merge_cmd = " ffmpeg -i 'concat:%s' -c copy %s/%s.mpg"
    files_arg = '|'.join([item.replace('mp4', 'mpg') for item in file_list])
    target_file = "output"
    status = os.system(merge_cmd % (files_arg, target_dir, target_file))
    os.system(f"ffmpeg -i {target_dir}/{target_file}.mpg -y -qscale 0 -vcodec libx264 {target_dir}/{target_file}.mp4")
    # os.system(f"ffmpeg -i {target_file}.mpg {target_file}.MP4")
    print(status)


def mp4_to_mpg(file_list):
    for index, mp4 in enumerate(file_list):
        file_name = mp4.replace('.mp4', '')
        status = os.system(f'ffmpeg -i {mp4} -qscale 4 {file_name}.mpg')
        print(f"{index + 1}/{len(file_list)}: {status} {file_name}.mpg")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("请传入待合并视频文件夹📁目录")
    else:
        target_dir = sys.argv[1]
    cmd_res = os.popen(f'ls {target_dir}/*.mp4').read()
    file_list = [item for item in cmd_res.split('\n') if item]
    pattern = re.compile(r'([0-9]+)')
    file_list.sort(key=lambda x: int(pattern.findall(x)[0]))
    mp4_to_mpg(file_list)
    supported_merge(file_list, target_dir)

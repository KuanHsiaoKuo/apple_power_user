import os
import re
import sys

# brew install ffmpeg


def supported_merge(files, target_dir):
    """
    ffmpeg只支持默认格式合并:
    Unsupported audio codec. Must be one of mp1, mp2, mp3, 16-bit pcm_dvd, pcm_s16be, ac3 or dts.
    :param files:
    :param target_dir:
    :return:
    """
    merge_cmd = " ffmpeg -i 'concat:%s' -c copy %s/%s.mpg"
    files_arg = '|'.join(files)
    target_file = "output"
    # 合并mpg
    merge_status = os.system(merge_cmd % (files_arg, target_dir, target_file))
    # 转为mp4
    if merge_status == 0:
        convert_status = os.system(f"ffmpeg -i {target_dir}/{target_file}.mpg -y -qscale 0 -vcodec libx264 {target_dir}/{target_file}.mp4")
    else:
        sys.exit('合并视频出错')
    if convert_status != 0:
        sys.exit('转化视频出错')
    os.system(f"rm -rf {target_dir}/*.mpg")
    # os.system(f"ffmpeg -i {target_file}.mpg {target_file}.MP4")


def mp4_to_mpg(file_list):
    """
    文件名问题：
    1. 空格
    2. 括号: 英文括号需要加'\'
    2. 竖线：需要替换
    :param file_list:
    :return:
    """
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
    try:
        mp4_to_mpg(file_list)
    except Exception:
        sys.exit('转化分视频出错！')

    mpg_cmd_res = os.popen(f'ls {target_dir}/*.mpg').read()
    mpg_file_list = [item for item in mpg_cmd_res.split('\n') if item]
    mpg_file_list.sort(key=lambda x: int(pattern.findall(x)[0]))

    try:
        supported_merge(mpg_file_list, target_dir)
    except Exception:
        print("使用前记得调整一下文件名: 空格、括号等")

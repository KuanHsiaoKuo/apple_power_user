import os
import re
import sys
import subprocess
from subprocess import CalledProcessError


# brew install ffmpeg


def supported_merge(files, target_dir, merged_name):
    """
    ffmpeg只支持默认格式合并:
    Unsupported audio codec. Must be one of mp1, mp2, mp3, 16-bit pcm_dvd, pcm_s16be, ac3 or dts.
    :param files:
    :param target_dir:
    :return:
    """
    merge_cmd = " ffmpeg -i 'concat:%s' -c copy %s/%s.mpg"
    files_arg = '|'.join(files)
    # 合并mpg
    merge_status = os.system(merge_cmd % (files_arg, target_dir, merged_name))
    # 转为mp4
    if merge_status == 0:
        convert_status = os.system(
            f"ffmpeg -i {target_dir}/{merged_name}.mpg -y -qscale 0 -vcodec libx264 {target_dir}/{merged_name}.mp4")
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


def subprocess_run(cmd: str):
    try:
        subprocess.run(cmd, shell=True, check=True, capture_output=True)
    except CalledProcessError as e:
        sys.exit(f'执行{cmd} 失败: {e}')
    except Exception as e:
        sys.exit(e)


def get_title_pic(title, pic_path):
    """ffmpeg加文字水印
    drawtext：绘制文本，也就是文字水印，相关参数第一个似乎要写=，其它参数写:。默认字体 Sans
    fontfile：字体文件
    > [Mac 电脑查看字体文件位置 | 温欣爸比的博客](https://wxnacy.com/2019/04/03/mac-fonts-path/)
    text：文字水印内容
    fontsize：水印字体大小，直接填数字
    box --是否使用背景框，默认为0
    boxcolor --背景框的颜色
    borderw --背景框的阴影，默认为0
    bordercolor --背景框阴影的颜色
    """
    target_pic_path = pic_path
    if not pic_path.endswith('.jpg'):
        pic_format = pic_path.split('.')[-1]
        jpg_pic_path = pic_path.replace(pic_format, 'jpg')
        convert_cmd = f"ffmpeg -i {pic_path} {jpg_pic_path}"
        subprocess_run(convert_cmd)
        target_pic_path = jpg_pic_path
        rm_convert_jpg_cmd = f"rm {target_pic_path}"
    else:
        rm_convert_jpg_cmd = None
    output_path = f"{'/'.join(pic_path.split('/')[:-1])}/{title}_video_cover.jpg"
    # x=w-tw-th:y=h-th， 文本的位置，放置图片右下方位置；w、h 表示原图的宽、高；tw、th 表示文本宽高；在减去th 作为间距
    drawtext_config = {
        # "fontfile": "MiSans-Normal.ttf",
        "fontfile": "/System/Library/Fonts/PingFang.ttc",
        "text": title,
        "x": "110",
        "y": "250",
        "fontsize": "38",
        "fontcolor": "black",
        "shadowy": "0"
    }
    drawtext = ':'.join([f"{key}={value}" for key, value in drawtext_config.items()])
    insert_cmd = f'ffmpeg  -i {target_pic_path}  -vf drawtext={drawtext} -y {output_path}'
    subprocess_run(insert_cmd)
    if rm_convert_jpg_cmd:
        subprocess_run(rm_convert_jpg_cmd)
    return output_path


def get_cover_video(video_path):
    mp3_path = video_path.replace('.mp4', '.mp3')
    extract_mp3_cmd = f"ffmpeg -i {video_path} -f mp3 -vn {mp3_path}"
    subprocess_run(extract_mp3_cmd)
    video_name = video_path.split('/')[-1]
    video_dir = '/'.join(video_path.split('/')[:-1])
    title = '-'.join(video_name.split('.')[:-1])
    pic_path = video_path.replace(".mp4", ".jpg")
    cover_path = get_title_pic(title, pic_path)
    cover_video = f"{video_dir}/{video_name}_covered.mp4"
    convered_mp4_cmd = f"ffmpeg -loop 1 -i {cover_path} -i {mp3_path} -c:a copy -c:v libx264 -shortest {cover_video}"
    subprocess_run(convered_mp4_cmd)
    subprocess_run(f"rm {mp3_path}")
    subprocess_run(f"rm {cover_path}")
    return cover_video


def merge(target_dir, covered=False):
    print('*' * 20, target_dir)
    os.popen(f"rm -rf {target_dir}/*.mpg")
    cmd_res = os.popen(f'ls {target_dir}/*.mp4').read()
    output_file = target_dir.split("/")[-1]
    file_list = [file for file in cmd_res.split('\n') if file]
    if covered:
        file_list = [get_cover_video(file) for file in file_list]
    pattern = re.compile(r'(\d+)')
    file_list.sort(key=lambda x: int(pattern.findall(x)[-2]))
    try:
        mp4_to_mpg(file_list)
    except Exception:
        sys.exit('转化分视频出错！')

    mpg_cmd_res = os.popen(f'ls {target_dir}/*.mpg').read()
    mpg_file_list = [mpg_file for mpg_file in mpg_cmd_res.split('\n') if mpg_file]
    mpg_file_list.sort(key=lambda x: int(pattern.findall(x)[0]))

    try:
        supported_merge(mpg_file_list, target_dir, output_file)
        if covered:
            subprocess_run(f"rm {target_dir}/*_covered.mp4")
    except Exception:
        print("使用前记得调整一下文件名: 空格、括号等")


def main():
    if len(sys.argv) == 1:
        sys.exit("请传入待合并视频文件夹📁目录")
    else:
        target_dir = sys.argv[1]
    target_dirs = [target_dir]
    for item in target_dirs:
        merge(item)


if __name__ == "__main__":
    main()

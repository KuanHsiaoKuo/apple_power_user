"""
给视频文件添加章节书签
"""

import re
import os
import sys
import subprocess
from subprocess import CalledProcessError

def times_chapters(time_path: str, save_path: str):
    """
    1. save_path: 保存在视频文件目录中。
    :param time_path:
    :param save_path:
    :return:
    """
    chapters = list()

    with open(time_path, 'r') as f:
        line_pattern = re.compile(r"(\d):(\d{2}):(\d{2}) (.*)")
        for line in f:
            if line.strip():
                hrs, mins, secs, title = line_pattern.findall(line.strip())[0]
                hrs, mins, secs = int(hrs), int(mins), int(secs)
                minutes = (hrs * 60) + mins
                seconds = secs + (minutes * 60)
                timestamp = (seconds * 1000)
                chap = {
                    "title": title,
                    "startTime": timestamp
                }
                chapters.append(chap)

    text = """;FFMETADATA1
major_brand=isom
minor_version=512
compatible_brands=isomiso2avc1mp41
encoder=Lavf59.16.100

    """

    for index, chap in enumerate(chapters):
        title = chap['title']
        start = chap['startTime']
        if index + 1 < len(chapters):
            end = chapters[index + 1]['startTime'] - 1
        else:
            end = start + 10000
        """
        [CHAPTER]
        TIMEBASE=1/1000
        START={start}
        END={end}
        title={title}
        
        """
        chapter = ["[CHAPTER]", "TIMEBASE=1/1000", f"START={start}", f"END={end}", f"title={title}", "\n"]
        text += '\n'.join(chapter)
    file_name = re.findall(r'(\d.*?\.mp4)', time_path)[0]
    file_name = file_name.split('/')[-1]
    chapters_path = f"{save_path}/{file_name}.txt"
    if os.path.exists(chapters_path):
        with open(chapters_path, 'r') as f:
            raw_text = f.read()
    else:
        raw_text = ''
    if text != raw_text:
        with open(chapters_path, "w") as f:
            f.write(text)
        return chapters_path
    else:
        return None


def gen_timetable(screenshots_path: str):
    """
    配合IINA的截图格式：
    screenshot-template: %{filename}-%p-
    0:23:20 Start
    0:40:30 First Performance
    0:40:56 Break
    1:04:44 Second Performance
    1:24:45 Crowd Shots
    1:27:45 Credits
    :param screenshots_path:
    :return:
    """
    info_pattern = re.compile(r'(\d.*?\.mp4)-(\d+:\d{2}:\d{2})-(.*?).png')
    ls_png_cmd = f"ls {screenshots_path}/*.png"
    try:
        png_cmd_res = subprocess.run(ls_png_cmd, shell=True, check=True, capture_output=True)
    except CalledProcessError as e:
        png_cmd_res = e
    if png_cmd_res.returncode == 0:
        png_list = png_cmd_res.stdout.decode().split('\n')
        png_infos = {}
        for png in png_list:
            png_info = info_pattern.findall(png)
            if png_info:
                video, timestamp, title = png_info[0]
                # 去掉截图归类目录
                # 例如：130-139.tokio-runtime/130-139.tokio-runtime.mp4-00:00:13-第一节-概要介绍.png
                video = video.split('/')[-1]
                if not title:
                    title = '未命名章节'
                if not png_infos.get(video):
                    png_infos[video] = []
                png_infos[video].append([timestamp, title])
        # 按照第二个时间点元素排序
        files = []
        for video, chapters in png_infos.items():
            file_path = f"{screenshots_path}/{video}.txt"
            chapters.sort(key=lambda item: item[0].split(':'))
            with open(file_path, 'w') as f:
                for timestamp, chapter_name in chapters:
                    f.writelines(f"{timestamp} {chapter_name}\n ")
            files.append(file_path)
        return files
    else:
        sys.exit(f"执行指令{ls_png_cmd}出错：{png_cmd_res.stderr.decode()}")


def categorized_screenshots(root_screen_directory):
    info_pattern = re.compile(r'(\d.*?)\.mp4-(\d+:\d{2}:\d{2})-(.*?).png')
    ls_png_cmd = f"ls {root_screen_directory}/*.png"
    try:
        png_cmd_res = subprocess.run(ls_png_cmd, shell=True, check=True, capture_output=True)
    except CalledProcessError as e:
        png_cmd_res = e
    if png_cmd_res.returncode == 0:
        png_list = png_cmd_res.stdout.decode().split('\n')
        file_titles = []
        for png in png_list:
            png_info = info_pattern.findall(png)
            if png_info:
                video_title, timestamp, title = png_info[0]
                if video_title and video_title not in file_titles:
                    file_titles.append(video_title)
        # 新建文件夹并整合截图
        for title in file_titles:
            dir_path = f"{root_screen_directory}/{title}"
            if not os.path.exists(dir_path):
                os.popen(f"mkdir {dir_path}")

            os.popen(f"mv {root_screen_directory}/{title}.*.png {dir_path}/")
    dir_res = os.popen(f"ls -d {root_screen_directory}/*/")
    dirs = dir_res.read().split('\n')
    return [item[:-1] for item in dirs]


def main(s_dir):
    timetables = gen_timetable(s_dir)
    chapter_files = []
    for timetable in timetables:
        chapter_path = times_chapters(timetable, video_path)
        if chapter_path:
            chapter_files.append(chapter_path)

    for chapter_file in chapter_files:
        video_name = re.findall(r'(\d.*?)\.mp4', chapter_file)[0]
        edit_video_path = f"{video_path}/{video_name}.mp4"
        inserted_video_path = f"{video_path}/{video_name}-chapters.mp4"
        """
        -y: 默认覆盖, 但是这里载入章节文件不可以in-place修改。
        -i: input
        -codec: 编解码
        -map_metadata 1: 只匹配头部内容，只能在第一次添加时生效
        -map_chapters 1: 匹配章节，在后续修改章节时需要加上
        """
        merge_command = f"ffmpeg -y -i {edit_video_path} -i {chapter_file} -map_metadata 1 -map_chapters 1 -codec copy {inserted_video_path}"
        delete_command = f"rm {edit_video_path}"
        mv_command = f"mv {inserted_video_path} {edit_video_path}"
        os.system(merge_command)
        os.system(delete_command)
        os.system(mv_command)


if __name__ == "__main__":
    timefile = ''
    chapter_file = ''
    if len(sys.argv) != 3:
        sys.exit('请按顺序加入截图文件夹路径和视频文件路径')
    else:
        ss_path, video_path = sys.argv[1], sys.argv[2]
    # times_chapters(timefile, chapter_file)
    screenshot_dirs = categorized_screenshots(ss_path)
    for screenshot_dir in screenshot_dirs:
        if screenshot_dir:
            main(screenshot_dir)

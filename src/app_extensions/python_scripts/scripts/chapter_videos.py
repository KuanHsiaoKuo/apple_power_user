"""
给视频文件添加书签
[How to Add Chapters to MP4s with FFmpeg - Kyle Howells](https://ikyle.me/blog/2020/add-mp4-chapters-ffmpeg)
[mpv.io#screenshot](https://mpv.io/manual/stable/#screenshot)
ffmpeg -i part1.mp4 -f ffmetadata part1.txt
ffmpeg -i part1.mp4 -i part1.txt -map_metadata 1 -codec copy part1_insert.mp4
"""

import re


def times_chapters(time_path: str, chapter_path: str):
    chapters = list()

    with open(time_path, 'r') as f:
        for line in f:
            x = re.match(r"(\d):(\d{2}):(\d{2}) (.*)", line)
            hrs = int(x.group(1))
            mins = int(x.group(2))
            secs = int(x.group(3))
            title = x.group(4)

            minutes = (hrs * 60) + mins
            seconds = secs + (minutes * 60)
            timestamp = (seconds * 1000)
            chap = {
                "title": title,
                "startTime": timestamp
            }
            chapters.append(chap)

    text = """
            ;FFMETADATA1
            major_brand=isom
            minor_version=512
            compatible_brands=isomiso2avc1mp41
            encoder=Lavf59.16.100
            
    """

    for i in range(len(chapters) - 1):
        chap = chapters[i]
        title = chap['title']
        start = chap['startTime']
        end = chapters[i + 1]['startTime'] - 1
        text += f"""
                    [CHAPTER]
                    TIMEBASE=1/1000
                    START={start}
                    END={end}
                    title={title}
                """
        chapter = ["[CHAPTER]", "TIMEBASE=1/1000", f"START={start}", f"END={end}", f"title={title}"]
        text += '\n'.join(chapter)

    with open(chapter_path, "w") as myfile:
        myfile.write(text)


if __name__ == "__main__":
    timefile = ''
    chapter_file = ''
    times_chapters(timefile, chapter_file)
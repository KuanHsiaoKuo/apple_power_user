"""
给视频文件添加书签
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
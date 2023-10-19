import os
import glob

PATH = "/media/sf_Porn"
VIDEO_TYPE = ['mp4', 'ts', 'mkv']

res = {
    "JP":{video: len(glob.glob(f"{PATH}/JP/**/*.{video}", recursive=True)) for video in VIDEO_TYPE},
    "JP_Series":{video: len(glob.glob(f"{PATH}/JP_Series/**/*.{video}", recursive=True)) for video in VIDEO_TYPE},
    "EN":{video: len(glob.glob(f"{PATH}/EN/**/*.{video}", recursive=True)) for video in VIDEO_TYPE},
    "EN_Series":{video: len(glob.glob(f"{PATH}/EN_Series/**/*.{video}", recursive=True)) for video in VIDEO_TYPE},
}

print(res)
print('Total: ', {video:sum([i[video] for i in res.values()]) for video in VIDEO_TYPE})
print('Sum: ', sum({video:sum([i[video] for i in res.values()]) for video in VIDEO_TYPE}.values()))

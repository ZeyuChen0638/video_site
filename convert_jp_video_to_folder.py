import os
import glob
import re
import shutil

PATH = "/media/sf_Porn/JP/松下紗栄子"

# for video in os.listdir(PATH):
#     if video.endswith('mp4') or video.endswith('ts') or video.endswith('avi'):
#         pattern = '(^[a-zA-Z]*-[0-9]*)'
#         match = re.search(pattern, video)
#         if match:
#             new_video_folder = os.path.join(PATH, match.group())
#             video_path = os.path.join(PATH, video)
#             print(video_path, new_video_folder)
#             os.mkdir(new_video_folder)
#             shutil.move(video_path, new_video_folder)



for video in os.listdir(PATH):
    for file in os.path.join(PATH, video):
        count = 0
        if file.endswith('.jpg') and file != 'ss.jpg':
            count += 1
    if count > 1:
        print(video)
        break
from django.http import HttpResponse
import json
import subprocess
import os
from backend.constant import *
from backend.common.img_base64 import encode_base64
# Create your views here.

def recommand(request):
    # demo 松下沙荣子
    res = {}
    for actor in os.listdir(os.path.join(PORN_DIRS, 'JP')):
        for video in os.listdir(os.path.join(PORN_DIRS, 'JP', actor)):
            for file in os.listdir(os.path.join(PORN_DIRS, 'JP', actor, video)):
                print(file)
                if file.endswith('jpg'):
                    img_b64 = encode_base64(os.path.join(PORN_DIRS, 'JP', actor, video, file))
                    res[video] = img_b64
    return HttpResponse(json.dumps(res))
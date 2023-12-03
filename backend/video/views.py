from django.http import HttpResponse, FileResponse
import json
import subprocess
import os
from backend.constant import *
from backend.common.img_base64 import encode_base64
from .models import *
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
# Create your views here.

def recommand(request):
    # demo 松下沙荣子
    res = {}
    for actor in os.listdir(os.path.join(PORN_DIRS, 'JP')):
        if actor == '松下紗栄子':
            for video in os.listdir(os.path.join(PORN_DIRS, 'JP', actor)):
                if os.path.isdir(os.path.join(PORN_DIRS, 'JP', actor, video)):
                    print(os.path.join(PORN_DIRS, 'JP', actor, f"'{video}'"))
                    for file in os.listdir(os.path.join(PORN_DIRS, 'JP', actor, video)):
                        print(file)
                        # if file.endswith('jpg') and file != "ss.jpg":
                        if file == f'{video}.jpg':
                            img_b64 = encode_base64(os.path.join(PORN_DIRS, 'JP', actor, video, file))
                            res[video] = img_b64
    return HttpResponse(json.dumps(res))


class FirstPageAPIVIew(APIView):
    def get(self, request):
        res = {}
        for actor in os.listdir(os.path.join(PORN_DIRS, 'JP')):
            if actor == '松下紗栄子':
                for video in os.listdir(os.path.join(PORN_DIRS, 'JP', actor)):
                    if os.path.isdir(os.path.join(PORN_DIRS, 'JP', actor, video)):
                        print(os.path.join(PORN_DIRS, 'JP', actor, f"'{video}'"))
                        for file in os.listdir(os.path.join(PORN_DIRS, 'JP', actor, video)):
                            print(file)
                            # if file.endswith('jpg') and file != "ss.jpg":
                            if file == f'{video}.jpg':
                                img_b64 = encode_base64(os.path.join(PORN_DIRS, 'JP', actor, video, file))
                                res[video] = img_b64
        return HttpResponse(json.dumps(res))

class AvatarAPIView(APIView):
    def get(self ,request):
        img_b64 = encode_base64('/media/sf_Porn/JP/松下紗栄子/actor.png')
        return HttpResponse(img_b64)
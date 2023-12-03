from django.http import HttpResponse
import os
import json
# Create your views here.

def listdir(request):
    print(request.GET['path'])
    dirs = os.listdir(request.GET['path'])
    print(dirs)
    return HttpResponse(json.dumps(dirs))

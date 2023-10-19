from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import json
import subprocess
import os

# Create your views here.

def statistic(request):
    return HttpResponse("Hello, you are getting statistic info")

def hostinfo(request):    
    def full_cpuinfo():
        with open('/proc/cpuinfo', 'r') as fr:
            cpuinfo_content = fr.read()
        cpu_cores = cpuinfo_content.replace('\t', '').split("\n\n")[:-1]
        last_cpu = {i.split(":")[0]:i.split(":")[1] for i in cpu_cores[-1].split('\n')}
        cpu_info = {
            'cores': len(cpu_cores),
            'model_name': last_cpu['model name'].strip(),
            'vendor': last_cpu['vendor_id'],
            'MHz': last_cpu['cpu MHz'],
            'cache_size': str(int(int(last_cpu['cache size'].strip().split(' ')[0]) / 1024)) + ' MB'
        }
        return cpu_info
        # [print(i,"\n#######################################") for i in cpu_cores]

    def get_memoryinfo():
        memory = subprocess.run("free", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
        [i.strip() for i in memory.stdout.split("\n")][1].split()
        mem_list = [i.strip() for i in memory.stdout.split("\n")][1].split()
        swap_list = [i.strip() for i in memory.stdout.split("\n")][2].split()
        memory_info = {
            'total_memory': "{:.2f}".format(int(mem_list[1]) / 1024 / 1024) + ' GB',
            'used_memory': "{:.2f}".format(int(mem_list[2]) / 1024 / 1024) + ' GB',
            'free_memory': "{:.2f}".format(int(mem_list[3]) / 1024 / 1024) + ' GB',
            'total_swap': "{:.2f}".format(int(swap_list[1]) / 1024 / 1024) + ' GB',
            'used_swap': "{:.2f}".format(int(swap_list[2]) / 1024 / 1024) + ' GB',
            'free_swap': "{:.2f}".format(int(swap_list[3]) / 1024 / 1024) + ' GB',
        }
        return memory_info
    
    def get_diskinfo():
        PORN_DIRS = '/media/sf_Porn/'
        PORN_FOLDERS = ['EN', 'EN_Series', 'JP', 'JP_Series']
        disk = subprocess.run(f"du -h {PORN_DIRS} --max-depth=1", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
        disk_list = {i.split('\t')[1]:i.split('\t')[0] for i in disk.stdout.split("\n")[:-1]}

        disk_info = {}
        for folder in PORN_FOLDERS:
            disk_info[folder] = disk_list[os.path.join(PORN_DIRS, folder)]
        return disk_info


    res = HttpResponse(json.dumps({
            "cpu": full_cpuinfo(),
            "memory": get_memoryinfo(),
            "disk": get_diskinfo()
        }))
    res['Access-Control-Allow-Origin']='*'
    res['Access-Control-Allow-Credentials']=True
    return res








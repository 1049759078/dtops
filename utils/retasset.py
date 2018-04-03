#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Eric

import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dtops.settings")# project_name 项目名称
django.setup()
from utils.Saltapi import SaltAPI
from  asset.models import Asset
salt = SaltAPI(url="https://118.25.39.84:8000", user="saltapi", password="saltapi123")
def getkeyall():
    minions,minions_pre = salt.list_all_key()
    # print(minions,minions_pre)
    # return minions,minions_pre
def disks(tgt,fun):
    dis = salt.remote_noarg_execution_sigle(tgt,fun)
    # print(dis)
    disk = {}
    for partition in dis.values():
        # print(partition)
        for i in partition.values():
            # print(i)
            fs = i['filesystem']
            if fs.startswith("/dev"):
                total = '%.2f' % (float(i['1K-blocks']) / 1024 / 1024) + 'G'
                avail = '%.2f' % (float(i['available']) / 1024 / 1024)
                capacity = i['capacity']
                used = '%.2f' % (float(i['used']) / 1024 / 1024)
                disk[fs] = { 'total': total, 'avail': avail,'used':used,'capacity':capacity}
            else:
                continue
        print(disk)

        return disk



def auto_asset(node):
    ret = salt.remote_grains_execution_sigle(node)
    asset_info = {}
    asset_info['os']= ret[node]['oscodename']
    asset_info['kernelrelease']= ret[node]['kernelrelease']
    asset_info['cpu_model']= ret[node]['cpu_model']
    asset_info['dns']= ''.join(ret[node]['dns']['ip4_nameservers'])
    asset_info['serialnumber'] =  ret[node]['serialnumber']
    asset_info['virtual'] =  ret[node]['virtual']
    asset_info['localhost'] = ret[node]['localhost']
    asset_info['mem_total'] =  ret[node]['mem_total']
    asset_info['num_cpus'] =  ret[node]['num_cpus']
    asset_info['ip4_interfaces'] = " ".join(ret[node]['ip4_interfaces']['eth0'])
    asset_info['hwaddr_interfaces'] = ret[node]['hwaddr_interfaces']['eth0']
    asset_info['disks'] = disks(node,'disk.usage')

    # selinux = ret[node]['enabled']
    return  asset_info
# ass = Asset.objects.all()
# for ii in ass:
#     asset_info=auto_asset(ii.inner_ip)
#     asset = Asset.objects.get(inner_ip=ii.inner_ip)
#     asset.osfinger = asset_info['os']
#     asset.hostname = asset_info['localhost']
#     asset.cpu_model = asset_info['cpu_model']
#     asset.mac_addr = asset_info['hwaddr_interfaces']
#     asset.mem_total = asset_info['mem_total']
#     asset.num_cpus = asset_info['num_cpus']
#     asset.virtual = asset_info['virtual']
#     asset.serialnumber = asset_info['serialnumber']
#     asset.dns = asset_info['dns']
#     asset.kernelrelease = asset_info['kernelrelease']
#     asset.inner_ip = asset_info['ip4_interfaces']
#     for de,di in asset_info['disks'].items():
#         #{'avail': '40.05', 'total': '49.09G', 'capacity': '15%', 'used': '6.54'}
#         asset.disk_total = ''.join(de + di['total'])
#     asset.save()


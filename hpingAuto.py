#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess

#IPリストのファイルを指定
IP_List = "/Users/yuhei/tools/Python-ping/IP.txt"

# ping対象をファイルから読み込む
with open(IP_List, "r") as f:
    IP_List = [v.rstrip() for v in f.readlines()]

# ping実行、保存
for i,IP in enumerate(IP_List):
    # /root/work/ICMP/ のディレクトリを作成する必要がある
    cmd_str = "script -a -t -c 'echo -e \"\\r\\n# hping2 -V -c 3 -1 --icmptype 8 " + IP + "\"; hping2 -V -I eth0 -c 3 -1 --icmptype 8 " + IP + "; echo -e \"\\r\\n# hping2 -V -c 3 -1 --icmptype 13 " + IP + "\"; hping2 -V -I eth0 -c 3 -1 --icmptype 13 " + IP + "; echo -e \"\\r\\n# hping2 -V -c 3 -1 --icmptype 17 " + IP + "\"; hping2 -V -I eth0 -c 3 -1 --icmptype 17 " + IP + "' /root/work/ICMP/icmp_" + IP + ".txt 2>/dev/null"
    subprocess.call(cmd_str, shell=True)

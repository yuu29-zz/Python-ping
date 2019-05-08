#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

#URLリストのファイルを選択
#SamlePass:/Users/yuhei/Desktop/test
IP_List = input("Please Enter IP_List_File FullPass: ")

# ping対象をファイルから読み込む
with open(IP_List, "r") as f:
    IP_List = [v.rstrip() for v in f.readlines()]

# ping実行、保存
for i,site in enumerate(IP_List):
    IP_List_w = '/root/work/ICMP/' + IP_List + '.txt'
    with open(IP_List_w , mode='a') as IP_List_save:
        os.system("echo # hping2 -V -c 3 -1 --icmptype 8 " + site + " ; hping2 -V -I eth0 -c 3 -1 --icmptype 8 " + site + "; echo # hping2 -V -c 3 -1 --icmptype 13 " + site + "; hping2 -V -I eth0 -c 3 -1 --icmptype 13 " + site + "; echo # hping2 -V -c 3 -1 --icmptype 17 " + site + "; hping2 -V -I eth0 -c 3 -1 --icmptype 17 " + site)

        
        cmd_str = "script -a -t -c 'echo -e \"\\r\\n# hping2 -V -c 3 -1 --icmptype 8 " + IP + "\"; hping2 -V -I eth0 -c 3 -1 --icmptype 8 " + IP + "; echo -e \"\\r\\n# hping2 -V -c 3 -1 --icmptype 13 " + IP + "\"; hping2 -V -I eth0 -c 3 -1 --icmptype 13 " + IP + "; echo -e \"\\r\\n# hping2 -V -c 3 -1 --icmptype 17 " + IP + "\"; hping2 -V -I eth0 -c 3 -1 --icmptype 17 " + IP + "' /root/work/" + YEARDAY + "/" + IP + "/icmp_" + IP + ".txt 2>/dev/null"
subprocess.call(cmd_str, shell=True)

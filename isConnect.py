#-*- coding: utf-8 -*-
import os
import sys
import IPy

def getIpStatus(ip):
    backinfo = os.system('ping -n 1 -w 1 %s' %ip)
    print(backinfo)
    if not backinfo:
        return str(ip.net())

def getIPs(ns):
    ips = IPy.IP(ns)
    retIps = []
    for ip in ips:
        backinfo = getIpStatus(ip)
        if backinfo != None:
            retIps.append(backinfo)
    return retIps

if __name__ == "__main__":
    print("argvs：" + sys.argv[1])
    print(getIPs(sys.argv[1]))
    print('finish!')

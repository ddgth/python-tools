#-*- coding: utf-8 -*-
from dns import resolver
import dns
import sys

def isDnsServer():
	#读取文件
	list = []
	with open('./DNS.txt','r') as fr:
		for line in fr:
			try:
				dns_query = dns.message.make_query("www.baidu.com", "A")
				response = dns.query.udp(dns_query, line.strip(), port = 53, timeout = 5)
				if type(response) == dns.message.Message:
					list.append(line.strip())
			except Exception as e:
				continue
	return list

if __name__ == '__main__':
	print(isDnsServer())
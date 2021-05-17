#!/usr/bin/python
from http import client

HOSTS_EXTERNAL_URL = [
	['raw.githubusercontent.com', '/jerryn70/GoodbyeAds/master/Hosts/GoodbyeAds.txt'],
	['raw.githubusercontent.com', '/StevenBlack/hosts/master/alternates/fakenews-gambling-porn/hosts'],
	['raw.githubusercontent.com', 'AdAway/adaway.github.io/master/hosts.txt'],
	['raw.githubusercontent.com','/r-a-y/mobile-hosts/master/AdguardDNS.txt'],
	['o0.pages.dev', '/Pro/hosts.txt'],
	['block.energized.pro', '/unified/formats/hosts.txt']
]

def bytes2utf (bytelist: list[bytes]) -> list[str]:
	return [line.decode('utf-8') for line in bytelist]

defaults = open('defaults.txt', 'r')
defaults_lines = defaults.readlines()
defaults.close()

whitelist = open('whitelist.txt', 'r')
whitelist_lines = whitelist.readlines()
whitelist.close()

custom_host = open('dalisoft.txt', 'r')
custom_host_lines = custom_host.readlines()
custom_host.close()

# Utils
def request(url: str, path: str) -> list[str]:
	conn = client.HTTPSConnection(url)
	conn.request('GET', path)
	bytelist = conn.getresponse().readlines()
	res = bytes2utf(bytelist)
	res = set(res)
	res = list(res)
	conn.close()
	return res

# Checks
def checkWhitelist (line: str) -> bool:
	if line in whitelist_lines:
		return True

	return False

def checkComments (line: str) -> bool:
	if '#' in line:
		return True

	return False


# All list
output_list: list[str] = []

print('Generating hosts... 0%')

# Blocks
for line in custom_host_lines:
	if checkWhitelist(line) is False and checkComments(line) is False:
		output_list.append(line)

index = 1
len = len(HOSTS_EXTERNAL_URL) + 1
for host, path in (HOSTS_EXTERNAL_URL):
	host_list = request(host, path)

	for line in host_list:
		if checkWhitelist(line) is False and checkComments(line) is False:
			output_list.append(line)

	print('Generating hosts... {}%'.format(int((index / len) * 100 )))
	index += 1

## IP Generation block
ip_list = request('block.energized.pro', '/extensions/ips/formats/list.txt')
for line in ip_list:
	if checkWhitelist(line) is False and checkComments(line) is False:
		output_list.append('0.0.0.0 {}'.format(line))

print('Generating hosts... 100%')

# Save hosts
print('Building blocks...')

hosts_file = open('hosts', 'w')
hosts_file.writelines(defaults_lines)
hosts_file.writelines(output_list)
hosts_file.close()

print('Done...')

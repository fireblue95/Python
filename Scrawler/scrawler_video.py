import os
import json
import random
import requests
from time import sleep
from lxml import etree
from tqdm import trange


def get_now_page(now_url):
	sleep(random.random())
	res = requests.get(now_url, headers=headers)
	html = etree.HTML(res.content)

	title_name = html.xpath('//*[@id="htitle"]//text()')
	video_name = f'{title_name[0].split()[0]}{title_name[-1].strip()}'
	now_number = title_name[0].split()[-1]

	xpath_ = '/html/body/div[3]/div[2]/div[9]/script[1]/text()'
	target = html.xpath(xpath_)[0].replace('\\', '')

	target_data = json.loads(target.split('=')[-1])
	next_html_url = f'https://www.qdrama.cc{target_data["link_next"]}'
	this_m3u8_url = target_data['url']
	now_ts_prekey_url = os.path.dirname(this_m3u8_url)
	return video_name, now_number, this_m3u8_url, now_ts_prekey_url, next_html_url


def read_m3u8(file_path):
	with open(file_path, 'rb') as f:
		data = f.readlines()

	number_ts = list()
	for i in data:
		temp = i.decode('utf-8').strip()
		if '.ts' in temp:
			number_ts.append(temp)
	return number_ts


def write_b(save_full_path, content_):
	with open(save_full_path, 'wb') as ff:
		ff.write(content_)


def start_get_video(this_url_):
	while True:
		video_name, now_number, this_m3u8_url, this_ts_prekey_url, next_html_url = get_now_page(this_url_)
		print(f'Video Name: {video_name} --> {now_number}')

		save_dir = os.path.join(os.path.abspath(os.getcwd()), video_name, f'{now_number}_ts')
		print(f'Save to: {os.path.dirname(save_dir)}')

		if not os.path.exists(save_dir):
			os.makedirs(save_dir)

		m3u8_abs_path = os.path.join(save_dir, os.path.basename(this_m3u8_url))
		sleep(random.random())
		res = requests.get(this_m3u8_url, headers=headers_ts)
		write_b(m3u8_abs_path, res.content)

		ts_filenames = read_m3u8(m3u8_abs_path)
		for i in trange(len(ts_filenames)):
			url = f'{this_ts_prekey_url}/{ts_filenames[i]}'
			filename = os.path.basename(url)

			sleep(random.random())
			res = requests.get(url, headers=headers_ts)
			write_b(os.path.join(save_dir, filename), res.content)
		if not next_html_url:
			break
		else:
			this_url_ = next_html_url

	start_merge_video(save_dir)


def start_merge_video(save_dir_):
	ts_full_files = list()
	output_dir_name = 'CompleteWorks'
	target_path = os.path.join(save_dir_, output_dir_name)
	if not os.path.exists(target_path):
		os.mkdir(target_path)
	
	print('Start merged.')
	all_dirs = os.listdir(save_dir_)

	if output_dir_name in all_dirs:
		del all_dirs[all_dirs.index(output_dir_name)]

	for main_path_ in all_dirs:
		video_path = os.path.join(save_dir_, main_path_)
		for i in os.listdir(video_path):
			if '.ts' in i:
				ts_full_files.append(os.path.normcase(os.path.join(video_path, i)))
		k = 0
		with open(os.path.join(target_path, os.path.basename(video_path).replace('_', '.')), 'wb') as ff:
			for i in trange(len(ts_full_files)):
				now_nn = int(os.path.basename(ts_full_files[i])[3:-3])
				if now_nn != k:
					print(f'File missing: edf{k:06d}.ts')
					exit()
				with open(ts_full_files[i], 'rb') as ts_f:
					ts_data = ts_f.readlines()
				for zz in ts_data:
					ff.write(zz)
				k += 1


headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

headers_ts = {
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
	'origin':'https://www.qdrama.cc',
	'accept-encoding':'gzip, deflate, br',
	'accept-language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
	'referer':'https://www.qdrama.cc/',
	'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
	'sec-ch-ua-mobile':'?0',
	'sec-fetch-dest':'empty',
	'sec-fetch-mode':'cors',
	'sec-fetch-site':'cross-site'
}

this_url = 'https://www.qdrama.cc/vod/play/id/23098/sid/8/nid/3.html'

start_get_video(this_url)


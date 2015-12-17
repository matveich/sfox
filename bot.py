import io
import time
import telepot
import pywapi
from pprint import pprint


def _weather(location='Novosibirsk'):
	weather = pywapi.get_weather_from_yahoo(list(pywapi.get_location_ids(location).keys())[1], units='metric')
	d = [
		{'Date': weather['condition']['date']}, 
		{'Current condition': weather['condition']['text']},
		{'Temperature': weather['condition']['temp']},
		{'Forecast for today': weather['forecasts'][0]['text']},
		{'High': weather['forecasts'][0]['high']},
		{'Low': weather['forecasts'][0]['low']}
	]
	s = ''
	for i in d:
		s += list(i.keys())[0] + ': ' + i[list(i.keys())[0]] + '\n'
	return s

def _help():
	return io.open('help.txt').read()

def _parse_command(s):
	if s.find(' ') != -1:
		return s[s.find('/')+1:s.find(' ')]
	else:
		return s[s.find('/')+1:]

commands = {'weather': _weather, 'help': _help}

def _launch_command(s):
	try:
		return commands[s]()
	except:
		return commands['help']()

token = '168197682:AAFszqo37rZ2RGnUxaKQ_sLe0Iw6gt0If6w'
bot = telepot.Bot(token)
pprint(bot.getMe())

def handler(msg):
	pprint(msg)
	com = _parse_command(msg['text'].encode('utf-8'))
	text = _launch_command(com)
	bot.sendMessage(msg['from']['id'], text)
	while 1:
		time.sleep(3)
		count = 0
		f = io.open('anya_go_sleep.txt', 'r')
		import random
	   	a = []
	   	print('gh')
		while f:
			a.append(f.readline())
		f.close()
		bot.sendMessage(122358697, a[random.randint(0, len(a)-1)])
		count+=1
		if count == 11:
			return


bot.notifyOnMessage(handler)
print('Listening...')

while 1:
	time.sleep(3)
import io, re
import time
import telepot
import pywapi
from pprint import pprint


def _weather(args, location='Novosibirsk'):
	l = ''
	if args:
		for a in args[0]:
			l = re.match('\D+', a).group(0)
		if l:
			location = l
	weather = pywapi.get_weather_from_yahoo(list(pywapi.get_location_ids(location).keys())[1], units='metric')
	s = 'date: %s\ncurrent condition: %s\ntemperature: %s\n\nforecast for today: %s\n\thigh: %s\n\tlow: %s' % (
		weather['condition']['date'], 
		weather['condition']['text'], 
		weather['condition']['temp'], 
		weather['forecasts'][0]['text'],
		weather['forecasts'][0]['high'],
		weather['forecasts'][0]['low']
	)
	return s

def _help():
	return io.open('help.txt').read()


def _parse_command(s):
	c = []
	if ' ' in s:
		c.append(s[s.find('/')+1:s.find(' ')])
	else:
		c.append(s[s.find('/')+1:])
		return c
	if '|' in s:
		c.append(s[s.find(' ') + 1: s.find('|')].split(' '))
	else:
		c.append(s[s.find(' ')+ 1:].split(' '))
		return c
	c.append(s[s.find('|')+1:].split(' '))
	return c

def _parse_global_params(params):
	res = {}
	for p in params:
		t = re.match('[0-2][0-9]:[0-5][0-9]', p)
		if t:
			res['time'] = t
	return res

def _set_timer(time):
	pass

commands = {'help': _help, 'weather': _weather}
global_params = {'time': _set_timer}

def _launch_command(s):
	try:
		return commands[s[0]](s[1:])
	except:
		return "Unknown command. /help"

token = '133385334:AAHabB1GdkdSjQr34gztlpOEK0tctS913xM'
bot = telepot.Bot(token)
pprint(bot.getMe())

def handler(msg):
	pprint(msg)	
	com = _parse_command(msg['text'].encode('utf-8'))
	print(com)
	text = _launch_command(com)
	"""gl = _parse_global_params(com[2])
	print(gl)
	for i in range(len(gl)):
		try:
			global_params[list(gl.keys())[i]](gl[i])
		except:
			pass"""
	bot.sendMessage(msg['from']['id'], text)


bot.notifyOnMessage(handler)
print('Listening...')

while 1:
	time.sleep(3)
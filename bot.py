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

def _start():
	return """Hi! I'm just another telgram bot. I was made for help my creator. 
		However, you can always ask me do something that i can. 
		You can create an issue or join to project in github.com/matveich/sfox.git"""

def _parse_command(s):
	if s.find(' ') != -1:
		return s[s.find('/')+1:s.find(' ')]
	else:
		return s[s.find('/')+1:]

commands = {'start': _start, 'help': _help, 'weather': _weather}

def _launch_command(s):
	try:
		return commands[s]()
	except:
		return "Unknown command. /help"

token = '133385334:AAHabB1GdkdSjQr34gztlpOEK0tctS913xM'
bot = telepot.Bot(token)
pprint(bot.getMe())

def handler(msg):
	pprint(msg)
	com = _parse_command(msg['text'].encode('utf-8'))
	text = _launch_command(com)
	bot.sendMessage(msg['from']['id'], text)


bot.notifyOnMessage(handler)
print('Listening...')

while 1:
	time.sleep(3)
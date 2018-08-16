import requests
import telepot
from scrapper import scrapper
bot = telepot.Bot('531532180:AAFwFjxhyEO-hEGgXGgmLwQC0U25mysDwNQ')
messages = bot.getUpdates()
print(messages)
users = []
zodiacs=['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
for msg in messages:
    user = msg['message']['from']['id']
    if user not in users:
        users.append(user)
        
dict ={}  
dict = scrapper()
for msg in messages[-1:]:
    user = msg['message']['from']['id']
    horo= msg['message']['text']
    if horo in zodiacs:
        bot.sendMessage(user,(dict[horo]))
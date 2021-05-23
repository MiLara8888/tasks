
import requests
n=input()
urll=f'http://numbersapi.com/{n}/math?json'
res=requests.get(urll)
res=res.json()
if res['found']==False:
    print('Boring')
else:
    print('Interesting')
    print(res['text'])


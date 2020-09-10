from win32com.client import Dispatch
import time
import requests
import json
def speaker(str):
    speak= Dispatch('SAPI.SpVoice')
    speak.Speak(str)

if __name__ == "__main__":
     speaker("News for today in India are")
     url="paste here your api link"
     json_news= requests.get(url).text
     json_news=json.loads(json_news)
     for i in range(0,10):
         speaker(json_news['articles'][i]['title'])
         time.sleep(1)
         speaker("Now next news headline is ")

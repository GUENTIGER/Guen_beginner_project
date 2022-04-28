
from bs4 import BeautifulSoup 
import requests 
import datetime
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

#get funtion weather
#get the weather from google

def weather(city): 
    city=city.replace(" ","+") #replace the space with +
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    print("Dang tim kiem......\n")
    soup = BeautifulSoup(res.text,'html.parser') #parse the html
    location = soup.select('#wob_loc')[0].getText().strip() 
    time = soup.select('#wob_dts')[0].getText().strip() #wob_dts is the id of the time  
    info = soup.select('#wob_dc')[0].getText().strip()  #wob_dc is the id of the info
    weather = soup.select('#wob_tm')[0].getText().strip() #wob_tm is the id of the weather
    print(location)
    print(time)
    print(info)
    print(weather+"°C") 

city=input("Tim bat ky thanh pho nao: ") 
city=city+" weather" 
weather(city)
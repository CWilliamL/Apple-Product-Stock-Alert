import requests
from datetime import date, datetime
import time
import random
from bs4 import BeautifulSoup
import concurrent.futures
import concurrent.futures.thread
from threading import Thread
import telegram
import iphone

iphone13url = "https://www.apple.com/hk/shop/fulfillment-messages?pl=true&parts.0=MGC73ZA/A&location=Central"
chat_id = "Your chat id"


def configure_telegram():
    """
    Configures the bot with a Telegram Token.
    Returns a bot instance.
    """

    TELEGRAM_TOKEN = 'Your Telegram Token'
    if not TELEGRAM_TOKEN:
        logger.error('The TELEGRAM_TOKEN must be set')
        raise NotImplementedError

    return telegram.Bot(TELEGRAM_TOKEN)

def urlgen():
    url = "https://www.apple.com/hk/shop/fulfillment-messages?pl=true"
    for i,d in enumerate(iphonemodel):
        url = url+"&parts."+str(i)+"="+d
    url = url+"&location=Central"
    print(url)
    return url
bot = configure_telegram()
applestore = {
    "R428": "IFC",
    "R499": "TST",
    "R409": "CWB",
    "R485": "FW",
    "R673": "APM",
    "R610": "ST"
}

iphonemodel = {
    "MLT83ZA/A":"細藍128",
    "MLTE3ZA/A":"細藍256",
    "MLTJ3ZA/A":"細藍512",
    "MLTN3ZA/A":"細藍1TB",
    "MLT63ZA/A":"細銀128",
    #"MLTC3ZA/A":"細銀256",
    "MLTG3ZA/A":"細銀512",
    "MLTL3ZA/A":"細銀1TB",
    #"MLT73ZA/A":"細金128",
    #"MLTD3ZA/A":"細金256",
    "MLTH3ZA/A":"細金512",
    "MLTM3ZA/A":"細金1TB",
    #"MLT53ZA/A":"細黑128",
    #"MLT93ZA/A":"細黑256",
    "MLTF3ZA/A":"細黑512",
    "MLTK3ZA/A":"細黑1TB",

    "MLH73ZA/A":"大藍128",
    "MLHC3ZA/A":"大藍256",
    "MLHG3ZA/A":"大藍512",
    "MLHL3ZA/A":"大藍1TB",
    "MLH53ZA/A":"大銀128",
    #"MLH93ZA/A":"大銀256",
    "MLHE3ZA/A":"大銀512",
    "MLHJ3ZA/A":"大銀1TB",
    #"MLH63ZA/A":"大金128",
    #"MLHA3ZA/A":"大金256",
    #"MLHF3ZA/A":"大金512",
    #"MLHK3ZA/A":"大金1TB",
    #"MLH43ZA/A":"大黑128",
    "MLH83ZA/A":"大黑256",
    "MLHD3ZA/A":"大黑512",
    "MLHH3ZA/A":"大黑1TB",
    "MK2L3ZP/A":"ipad銀64",
    "MK2K3ZP/A":"ipad黑64",
    #"MLWL3ZP/A":"mini粉64",
    "MK8K3ZP/A":"mini紫256 5g",
    "MK8F3ZP/A":"mini黑256 5g",
    "MLX93ZP/A":"mini粉256 5g",
    "MK8H3ZP/A":"mini白256 5g"
    #"MLDW3ZA/A":"粉128",
    #"MLDY3ZA/A":"藍128",
    #"MLDU3ZA/A":"黑128",
    #"MLDY3ZA/A":"藍128"
    #"MLE23ZA/A":"粉256"
}

stocks = {
    "細藍128":[],
    "細藍256":[],
    "細藍512":[],
    "細藍1TB":[],
    "細銀128":[],
    "細銀256":[],
    "細銀512":[],
    "細銀1TB":[],
    #"細金128":[],
    "細金256":[],
    "細金512":[],
    "細金1TB":[],
    #"細黑128":[],
    "細黑256":[],
    "細黑512":[],
    "細黑1TB":[],
    "大藍128":[],
    "大藍256":[],
    "大藍512":[],
    "大藍1TB":[],
    #"大銀128":[],
    "大銀256":[],
    "大銀512":[],
    "大銀1TB":[],
    #"大金128":[],
    #"大金256":[],
    #"大金512":[],
    #"大金1TB":[],
    #"大黑128":[],
    "大黑256":[],
    "大黑512":[],
    "大黑1TB":[],
    "ipad銀64":[],
    "ipad黑64":[],
    #"mini粉64":[],
    "mini紫256 5g":[],
    "mini黑256 5g":[],
    "mini粉256 5g":[],
    "mini白256 5g":[]
    #"粉128": [],
    #"黑128": [],
    #"白128": [],
    #"藍128": []
    #"粉256": []
}

#iphone13urlgen = urlgen()
#proxylist = Proxies()
#proxylist.start()
time.sleep(1)
previous_message=""
previous_request_time = time.time()
count=0


#get the list of free proxies
def getProxies():
    r = requests.get('https://free-proxy-list.net/')
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('tbody')
    proxies = []
    for row in table:
        if row.find_all('td')[4].text =='elite proxy':
            proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
            proxies.append(proxy)
        else:
            pass
    return proxies

def extract(proxy):
    #this was for when we took a list into the function, without conc futures.
    #proxy = random.choice(proxylist)
    global iphone13urlgen
    iphone13prourl = iphone13urlgen
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    try:
        #change the url to https://httpbin.org/ip that doesnt block anything
        r = requests.get(iphone13prourl, headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=10)
        #print(r.status_code)
        return r
    except:
        
        #delete_url = "http://localhost:5010/delete?proxy="+proxy
        #requests.get(delete_url)
        print("fail and deleted")
        return 404

def publish():
    message = ""
    for key,values in stocks.items():
        if values != []:
            message= message+key+": "
            for value in values:
                message= message+value+", " 
            message=message[:-2]
            message+="\n"

    if message !="":
        finalmessage=message+str(datetime.now())[:-3]
    else:
        finalmessage="冇哂貨\n(%s)\n"%(str(datetime.now())[:-3])
    bot.sendMessage(chat_id=chat_id,text=finalmessage)

def monitoring(model_id):
    global count, previous_request_time, stocks
    request_time = time.time()
    try:
        response = ""
        stock_list = []
        proxies=[]
        proxiesjson = requests.get("http://127.0.0.1:5010/all/?type=https").json()
        for proxyip in proxiesjson:
            proxies.append(proxyip["proxy"])
        proxies = random.sample(proxies,len(proxies))
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_url = {executor.submit(iphone.getstock,model_id,proxy): proxy for proxy in proxies[:5]}
            for future in concurrent.futures.as_completed(future_to_url):
                response = future.result()
                #print(response)
                if response == 404:
                    
                    #print("proxy deleted")
                    print("failed")
                    

                elif response != "":
                    try:
                        #response.json()
        
                        executor.shutdown(wait=False)
                        for f in future_to_url:
                            if not f.done():
                                f.cancel()
                        break
                    except:
                        pass
        #print(response)

        # if response == 404 or response.status_code == 301 or response.status_code == 503:
        #     return
        # if request_time <= previous_request_time:
        #     return
        # else:
        #     previous_request_time = request_time
        if not isinstance(response,int):
            partNumber = response['partNumber']
            print(partNumber)
            previous_stocks = stocks[iphonemodel[partNumber]]
            for content in response['quoteDetails']['quotes']:
                if content['availabilityStatus'] == 'AVAILABLE_TODAY':
                    stock_list.append(applestore[content['storeNumber']])
            if previous_stocks != stock_list:
                stocks[iphonemodel[partNumber]] = stock_list
                publish()
        count+=1
        if count ==10000:
            bot.sendMessage(chat_id="Your chat id",text="Still Running")
            count=0


    except Exception as ex:
        template = "An exception of type (0) occured. Arguments:\n{1!r}"
        errormessage = template.format(type(ex).__name__,ex.args)
        try:
            bot.sendMessage(chat_id="Your chat id",text=errormessage)
        except:
            pass
    return


while True:
    for model_id in iphonemodel:
        Thread(target=monitoring,args=[model_id]).start()
    time.sleep(0.2)



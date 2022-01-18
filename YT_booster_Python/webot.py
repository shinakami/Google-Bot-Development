from lib2to3.pgen2 import driver
from selenium import webdriver
from time import sleep
import random as rd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from fake_useragent import UserAgent
import os
import re
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import loguru
import pyquery
from tqdm import tqdm
import random
os.system('cls')

def SSLIPcatcher():
    response = requests.get("https://www.sslproxies.org/")
 
    proxy_ips = re.findall('\d+\.\d+\.\d+\.\d+:\d+', response.text)  #「\d+」代表數字一個位數以上
    
    valid_ips = []
    for ip in proxy_ips:
        try:
            result = requests.get('https://ip.seeip.org/jsonip?',
			       proxies={'http': ip, 'https': ip},
			       timeout=5)
            print(result.json())
            valid_ips.append(ip)
        except:
            print(f"{ip} invalid")
    return valid_ips
            




def getProxiesFromFreeProxyList():
    proxies = []
    url = 'https://free-proxy-list.net/'
    loguru.logger.debug(f'getProxiesFromFreeProxyList: {url}')
    loguru.logger.warning(f'getProxiesFromFreeProxyList: downloading...')
    response = requests.get(url)
    if response.status_code != 200:
        loguru.logger.debug(f'getProxiesFromFreeProxyList: status code is not 200')
        return
    loguru.logger.success(f'getProxiesFromFreeProxyList: downloaded.')
    d = pyquery.PyQuery(response.text)
    trs = list(d('list > tbody > tr').items())
    loguru.logger.warning(f'getProxiesFromFreeProxyList: scanning...')
    IPPool = []
    for tr in trs:
        # 取出所有資料格
        tds = list(tr('td').items())
        # 取出 IP 欄位值
        ip = tds[0].text().strip()
        # 取出 Port 欄位值
        port = tds[1].text().strip()
        # 取出匿名性
        anom = tds[4].text().strip()
        # 組合 IP 代理
        #if anom == 'level3':
        proxy = f'{anom}:{ip}:{port}'
        proxies.append(proxy)
        IPPool.append(pd.DataFrame([{'IP':ip, 'Port':port}]))
    IPPool = pd.concat(IPPool, ignore_index=True)
    loguru.logger.success(f'getProxiesFromFreeProxyList: scanned.')
    loguru.logger.debug(f'getProxiesFromFreeProxyList: {len(proxies)} level3 proxies is found.')
    return IPPool



def IPcheater():

    ActIps = IPmoder()
    options = webdriver.ChromeOptions()
    proxy = 'http://'+ActIps['IP'][0]+':'+ActIps['Port'][0]
    options.add_argument(('–proxy-server='+proxy))
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    os.system('cls')
    print('–proxy-server='+proxy)
    IPPool = []
    for i in range(1,6):
        # 用迴圈逐一打開分頁
        url = 'http://free-proxy.cz/zh/proxylist/country/all/https/ping/level1'.format(i)
        print('Dealing with {}'.format(url))
        driver.get(url)
        soup = BeautifulSoup(driver.page_source)
        for j in soup.select('tbody > tr'):
            if re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', str(j)):
                IP = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', str(j))
                Port = re.findall('class="fport" style="">(.*?)</span>', str(j))
                IPPool.append(pd.DataFrame([{'IP':IP, 'Port':Port}]))
        print('There are {} IPs in Pool'.format(len(IPPool)))
    IPPool = pd.concat(IPPool, ignore_index=True)
    #print(IPPool)

    ActIps = []
    for IP, Port in zip(IPPool['IP'],IPPool['Port']):
        if len(IP) >= 1 and len(Port) >= 1:
            proxy = {'http':'http://'+ IP[0] + ':' + Port[0],
                    'https':'https://'+ IP[0] + ':' + Port[0]} 
            print(proxy)
            try:
                # 隨機找的一篇新聞即可
                url = 'https://www.youtube.com/watch?v=tfHHtMm37BI'
                resp = requests.get(url, proxies=proxy, timeout=2)
                if str(resp.status_code) == '200':
                    ActIps.append(pd.DataFrame([{'IP':IP[0], 'Port':Port[0]}]))
                    print('Succed: {}:{}'.format(IP, Port), 'code: ', resp.status_code)
                else:
                    print('Failed: {}:{}'.format(IP, Port), 'code: ', resp.status_code)
            except:
                    ActIps.append(pd.DataFrame([{'IP':IP[0], 'Port':Port[0]}]))
                    print('Failed: {}:{}'.format(IP, Port), 'code: NULL')
    ActIps = pd.concat(ActIps, ignore_index=True)
    print(ActIps)
    return ActIps


def IPmoder():
    print("IPmoder start")
    IPPool = []
    for i in range(666):
        IP = str(rd.randint(0,255)) + '.' + str(rd.randint(0,255)) + '.' + str(rd.randint(0,255)) + '.' + str(rd.randint(0,255))
        Port = str(rd.randint(0, 100000))
        IPPool.append(pd.DataFrame([{'IP':IP, 'Port':Port}]))
    IPPool = pd.concat(IPPool, ignore_index=True)
    return IPPool

    #ActIps = []
    #for IP, Port in zip(IPPool['IP'],IPPool['Port']):
    #    if len(IP) >= 1 and len(Port) >= 1:
    #        proxy = {'http':'http://'+ IP + ':' + Port,
    #                'https':'https://'+ IP + ':' + Port} 
    #        try:
    #            # 隨機找的一篇新聞即可
    #            url = 'https://www.youtube.com/watch?v=tfHHtMm37BI'
    #            resp = requests.get(url, proxies=proxy, timeout=2)
    #            if str(resp.status_code) == '200':
    #                ActIps.append(pd.DataFrame([{'IP':IP, 'Port':Port}]))
    #                print('Succed: {}:{}'.format(IP, Port), 'code: ', resp.status_code)
    #            else:
    #                print('Failed: {}:{}'.format(IP, Port), 'code: ', resp.status_code)
    #        except:
    #                print('Failed: {}:{}'.format(IP, Port), 'code: NULL')
    #ActIps = pd.concat(ActIps, ignore_index=True)
    #print(ActIps)
    #return ActIps


#ActIps = IPmoder()
#ActIps = IPcheater()
#ActIps = getProxiesFromFreeProxyList() 
ops=[]
ip = []
ID = []
def IPDataManager():
    for i in range(5):
        ops.append('')
        ops[i] = webdriver.ChromeOptions()
        user = UserAgent()
        us_a = user.chrome
        ID.append('')
        ip.append('')
        ID[i] = us_a
        IP_noot = rd.randint(0, len(ActIps['IP'])-1)
        Port_noot = rd.randint(0, len(ActIps['Port'])-1)
        ip[i] = ActIps['IP'][IP_noot]+':'+ActIps['Port'][Port_noot]
        proxy = 'https://'+ActIps['IP'][IP_noot]+':'+ActIps['Port'][Port_noot]
        ops[i].add_argument('user-agent='+us_a)
        ops[i].add_argument(('–proxy-server='+proxy))
        ops[i].add_argument("--mute-audio")

def SLLIPDataManager(ActIps):
    for i in range(5):
        ops.append('')
        ops[i] = webdriver.ChromeOptions()
        user = UserAgent()
        us_a = user.chrome
        ID.append('')
        ip.append('')
        ID[i] = us_a
        IP_noot = rd.randint(0, len(ActIps)-1)
        
        ip[i] = ActIps[IP_noot]
        proxy = 'https://'+ActIps[IP_noot]
        ops[i].add_argument('user-agent='+us_a)
        ops[i].add_argument(('–proxy-server='+proxy))
        ops[i].add_argument("--mute-audio")


ActIps = SSLIPcatcher()
SLLIPDataManager(ActIps)
driver_root = []

for op in ops:
    driver_f = webdriver.Chrome(executable_path='chromedriver', chrome_options=op)
    driver_root.append(driver_f)

net_root1 = ['https://www.youtube.com/watch?v=VwWgU6JHuvQ', 'https://www.youtube.com/watch?v=BC2Ulz7896Y'
            ,'https://www.youtube.com/watch?v=aNo-jPjH5V8', 'https://www.youtube.com/watch?v=v-hKahoiBV0'
            ,'https://www.youtube.com/watch?v=Ha5g9H4nu6I', 'https://www.youtube.com/watch?v=47xFYqCndLc'
            ,'https://www.youtube.com/watch?v=D2mMOMbrfQQ', 'https://www.youtube.com/watch?v=W-oZxYwTscM']


net = [net_root1]
time_sleep = 0

while True :
   
    os.system('cls')
    for i in range(5):    
        print(ID[i])
        print(ip[i])
        sleep(1)
    nt = 0
    time_sleep = time_sleep + 1
    time = 360
    net_root = net[nt]
   

    ChList = random.sample(range(0, len(net_root)-1), 5)
    ch_root = ChList
 
    print('delay_time:', time, 'time-step: ', time_sleep, 'net root num: ', nt)
    print('ch1: ', ch_root[0], 'ch2: ', ch_root[1], 'ch3: ', ch_root[2], 'ch4: ', ch_root[3], 'ch5: ', ch_root[4])

    i = 0
    with tqdm(total=5) as pbar: 
        for driver_boot in driver_root:
            driver_boot.get(net_root[ch_root[i]])
            pbar.update(1)
            i = i + 1
    with tqdm(total=time) as tbar:
        for i in range(time):
            sleep(1)
            tbar.update(1)
    
    for driver_boot in driver_root:
        driver_boot.delete_all_cookies()
        driver_boot.refresh()

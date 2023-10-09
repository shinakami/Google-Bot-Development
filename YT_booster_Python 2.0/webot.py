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
import gc

os.system('cls')


            


"""

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




#Basic ip Data Intialization



#----------------------------for Old DataForm----------------------------------------
#ActIps = IPmoder()
#ActIps = IPcheater()
#ActIps = getProxiesFromFreeProxyList() 

def IPDataManager(ActIps):
    
    for i in range(5):
        ops.append('')
        ops[i] = webdriver.ChromeOptions()
        ops[i].add_experimental_option("excludeSwitches", ["enable-automation"])
        ops[i].add_experimental_option('useAutomationExtension', False)
        ops[i].add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})
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

#----------------------------for Old DataForm----------------------------------------

"""
   
ops=[]
ip = []
ID = []

def SSLIPcatcher(minimum_ipcount):
    times = 0
    valid_ips = []
    while len(valid_ips) < minimum_ipcount:
        loguru.logger.debug("Collecting from https://www.sslproxies.org/")
        response = requests.get("https://www.sslproxies.org/")

        proxy_ips = re.findall('\d+\.\d+\.\d+\.\d+:\d+', response.text)#「\d+」代表數字一個位數以上
        #https://ip.seeip.org/jsonip?
        for ip in proxy_ips:
            try:
                result = requests.get('https://ip.seeip.org/jsonip?',
			        proxies={'http': ip, 'https': ip},
			        timeout=5)
                loguru.logger.success(result.json() +": " + str(result.status_code))
                valid_ips.append(ip)
            except:
                loguru.logger.warning(f"{ip} invalid")
        times += 1
    print("Searching times :" + str(times))
    loguru.logger.success("ValidIP Collecting Completed")
    return valid_ips

def SLLIPDataManager(ActIps):
   


    for i in range(len(ActIps)):
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
        ops[i].add_experimental_option("excludeSwitches", ["enable-automation"])
        ops[i].add_experimental_option('useAutomationExtension', False)
        ops[i].add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})


def Exacute(ActIps):

    while True :


        SLLIPDataManager(ActIps)
        driver_root = []

        

        for op in ops:
            driver_f = webdriver.Chrome(executable_path='chromedriver', chrome_options=op)
            driver_root.append(driver_f)
            

        net = ['https://www.youtube.com/watch?v=LvkK-I4KUKI', 'https://www.youtube.com/watch?v=A1DHC3ininw'
                    ,'https://www.youtube.com/watch?v=kOz-tItDBuU', 'https://www.youtube.com/watch?v=D2mMOMbrfQQ'
                    ,'https://www.youtube.com/watch?v=yTArRtqMkMA', 'https://www.youtube.com/watch?v=xTsTMMYx8XQ'
                    ,'https://www.youtube.com/watch?v=xE6wrmIRjz0', 'https://www.youtube.com/watch?v=VwWgU6JHuvQ']


        time_sleep = 0
        setting_timeSleep = 3
        
        while time_sleep < setting_timeSleep:
            for i in range(len(ActIps)):    
                print(ID[i])
                print(ip[i])
                sleep(1)

            time_sleep = time_sleep + 1
            time = 360

            net_root= net

            ChList = random.sample(range(0, len(net_root)-1), len(ActIps))
            ch_root = ChList
        
            print('delay_time:', time, 'time-step: ', time_sleep)
            

            i = 0
            with tqdm(total=len(ActIps)) as pbar: 
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
            gc.collect()
            break

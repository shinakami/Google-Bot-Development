from lib2to3.pgen2 import driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time
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



def SSLIPcatcher(minimum_ipcount):

    valid_ips = []
    set_ips = []
    loguru.logger.debug("Collecting from https://www.sslproxies.org/")
    response = requests.get("https://www.sslproxies.org/")

    proxy_ips = re.findall('\d+\.\d+\.\d+\.\d+:\d+', response.text)#「\d+」代表數字一個位數以上
       
    for ip in proxy_ips:
            
            
        ###
        valid_ips.append(ip) 
        ### 

    valid_ipsample = random.sample(range(0, len(valid_ips)), minimum_ipcount)        

    for el in valid_ipsample:
        set_ips.append(valid_ips[el])

    loguru.logger.success("ValidIP Collecting Completed")
    loguru.logger.debug("IP: " + str(set_ips))
    return set_ips


   

def Execute(minimum_ipcount, execute_time, execute_step):
    circle = 0
    while True :
        os.system("PYKAMIA的清除系統資料.bat")
        os.system("cls")
        ActIps = SSLIPcatcher(minimum_ipcount)
        ops = []
        ID = []

        print("Browser num: "+ str(len(ActIps)))

        print("start")


        time.sleep(3)
        
        circle = circle + 1

        for i in range(len(ActIps)):
            ops.append('')
            ops[i] = Options()
        
            user = UserAgent()
            us_a = user.chrome
            ID.append('')
            ID[i] = us_a
            
      
            proxy = 'https://'+ActIps[i]
            ops[i].add_argument('user-agent='+us_a)
            ops[i].add_argument(('–proxy-server='+proxy))
            ops[i].add_argument("--mute-audio")
            ops[i].add_experimental_option("excludeSwitches", ["enable-automation"])
            ops[i].add_experimental_option('useAutomationExtension', False)
            ops[i].add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})

        
        driver_root = []

        
        for op in ops:
            driver_f = webdriver.Chrome(service=Service('chromedriver.exe'), options=op)
            driver_root.append(driver_f)
          

        net = ['https://www.youtube.com/watch?v=d6sxJlNxZnw', 'https://www.youtube.com/watch?v=-XBGDNXN-_M'
                    ,'https://www.youtube.com/watch?v=Y-W7B_veFUk', 'https://www.youtube.com/watch?v=ZxxaFuDRy3c'
                    ,'https://www.youtube.com/watch?v=yTArRtqMkMA', 'https://www.youtube.com/watch?v=xTsTMMYx8XQ'
                    ,'https://www.youtube.com/watch?v=xE6wrmIRjz0', 'https://www.youtube.com/watch?v=1aE1yZl2-vc'
                    ,'https://www.youtube.com/watch?v=ikx2uLfhesg', 'https://www.youtube.com/watch?v=EklnZzW6gKw'
                    ,'https://www.youtube.com/watch?v=H1f4aAXAPFI', 'https://www.youtube.com/watch?v=KcNoBA1e3ss'
                    ,'https://www.youtube.com/watch?v=JDzOI0uVk0A', 'https://www.youtube.com/watch?v=vTtRo-uHfbU'
                    ,'https://www.youtube.com/watch?v=pdbMjxOZSco', 'https://www.youtube.com/watch?v=tY7ptP7ca8Q'
                    ,'https://www.youtube.com/watch?v=KN1tB6N5tFU', 'https://www.youtube.com/watch?v=NS1H69k6s3o']

        
        step = 0
        
        while True:    
            
            for i in range(len(ActIps)):
                loguru.logger.debug(ID[i] + '/' +ActIps[i])    
                print(ops[i])
                time.sleep(1)
                

            step = step + 1

            ChList = random.sample(range(0, len(net)-1), len(ActIps))
            
            random_execute_time = random.randint(execute_time-60, execute_time)

            print('execute_time:', random_execute_time, 'Step: ', step, '/', execute_step, 'Round: ', circle)
                

            
                
            with tqdm(total = len(ActIps)) as pbar: 
                i = 0
                for driver_boot in driver_root:
                    
                    
                    ###叫出視窗
                    driver_boot.get(net[ChList[i]])
                      

                    ###模擬使用者滑鼠點擊
                    action = ActionChains(driver_boot)
                    action.move_by_offset(10, 10)  # 移動到頁面的某個坐標（這裡是 (10, 10)）
                    action.click()
                    action.perform()

                    ###縮小視窗
                    if step == 1:
                        driver_boot.minimize_window() 

                    pbar.update(1)
                    i = i + 1
                

            with tqdm(total = random_execute_time) as tbar:
                for i in range(random_execute_time):
                    time.sleep(1)
                    tbar.update(1)


            for driver_boot in driver_root:
                
                driver_boot.refresh()
                
            if step == execute_step:
                for driver_boot in driver_root:
                    driver_boot.quit()
                del ops[:]
                del ID[:]
                break

            gc.collect()
            
            
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time
import random as rd
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import os
import re
import requests
import loguru
from tqdm import tqdm
import random
import gc
import sys
import SSLtest

   

def Execute(minimum_ipcount, execute_time, execute_step, address):
    circle = 0
    is_operating = True
    while is_operating :
        #os.system("PYKAMIA的清除系統資料.bat")
        os.system("cls")
        #ActIps = SSLIPcatcher(minimum_ipcount)
        ActIps = SSLtest.SSLIPcatcher(minimum_ipcount)
        ops = []
        ID = []

        print("Browser num: "+ str(len(ActIps)))

        print("start")


        
        circle = circle + 1

        for i in range(len(ActIps)):
            ops.append(Options())
            
        
            while len(ID) < len(ActIps):
                user = UserAgent()
                us_a = user.chrome
                if 'Windows' in us_a or 'Macintosh' in us_a:
                    print("Only Windows & Macintosh")
                    ID.append(us_a)
        
            
      
            proxy = 'https://'+ActIps[i]
            ops[i].add_argument('user-agent='+us_a)
            ops[i].add_argument(('–proxy-server='+proxy))
            ops[i].add_argument("--mute-audio")
            ops[i].add_experimental_option("excludeSwitches", ["enable-automation"])
            ops[i].add_experimental_option('useAutomationExtension', False)
            ops[i].add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})

        net = address
        if len(net) < minimum_ipcount:
            loguru.logger.warning("address array is too short")
            sys.exit("程序已被強制停止")
        
        driver_root = []

        
        for op in ops:
            driver_f = webdriver.Chrome(service=Service('chromedriver.exe'), options=op)
            driver_f.set_page_load_timeout(execute_time) # 設置頁面載入過期時間門檻
            driver_root.append(driver_f)


        
        step = 0
        try:
            while step != execute_step:    

                for i in range(len(ActIps)):
                    loguru.logger.debug(ID[i] + '/' +ActIps[i])    
                    print(ops[i])
                    time.sleep(1)
                    

                step = step + 1

                ChList = random.sample(range(len(net)), len(ActIps)) #根據IP的數目挑選不重複的頻道位置
                
                random_execute_time = random.randint(execute_time-60, execute_time) # 隨機設置WebDriver執行時間

                print('execute_time:', random_execute_time, 'Step: ', step, '/', execute_step, 'Round: ', circle)
                    

                
                    
                with tqdm(total = len(ActIps)) as pbar: 
                    i = 0
                    for driver_boot in driver_root:
                        

                        ### 叫出視窗
                        
                        driver_boot.get(net[ChList[i]])
                        

                        ###模擬使用者滑鼠點擊
                        action = ActionChains(driver_boot)
                        action.move_by_offset(1, 1)  # 移動到頁面的某個坐標（這裡是 (10, 10)）
                        action.click()
                        action.perform()
                        

                        
                        driver_boot.minimize_window() 

                        pbar.update(1)
                        i = i + 1
                    
                ###維持Google瀏覽器開啟的時間(random_execute_time)
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
                    del driver_root[:]
                    

                gc.collect()
            
        except KeyboardInterrupt:
            loguru.logger.warning("YT Viewer Monitoring stopped.")
            is_operating = False

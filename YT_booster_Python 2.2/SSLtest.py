import requests
import re
import random
import json
from loguru import logger
import os
import sys

def load_previous_ips(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_ips(filename, ips):
    with open(filename, 'w') as file:
        json.dump(ips, file)

def SSLIPcatcher(minimum_ipcount, previous_ips_file='previous_ips.json'):
    valid_ips = []
    set_ips = []
    previous_ips = load_previous_ips(previous_ips_file)
    
    logger.debug("Collecting from https://www.sslproxies.org/")
    response = requests.get("https://www.sslproxies.org/")
    
    # 解析出代理 IP 列表
    proxy_ips = re.findall(r'\d+\.\d+\.\d+\.\d+:\d+', response.text)
    
    for ip in proxy_ips:
        try:
           
                # 若成功則加入有效 IP 列表
            if ip not in previous_ips:  # 確保不重複
                valid_ips.append(ip)  
                logger.info(f"IP {ip} is valid and not previously used.")
            else:
                logger.warning(f"IP {ip} is already in the previous list, skipping.")
            
        except requests.RequestException:
            logger.error(f"IP {ip} is invalid or unreachable.")
            continue
    
    if len(valid_ips) < minimum_ipcount:
        logger.warning("可用 IP 數量不足，無法滿足需求。")
        sys.exit()

    # 隨機選取所需的有效 IP
    valid_ipsample = random.sample(valid_ips, minimum_ipcount)
    
    for el in valid_ipsample:
        set_ips.append(el)

    logger.success("ValidIP Collecting Completed")
    logger.debug("IP: " + str(set_ips))
    
    # 儲存當前的 set_ips 以便未來使用
    save_ips(previous_ips_file, set_ips)

    return set_ips


SSLIPcatcher(5)

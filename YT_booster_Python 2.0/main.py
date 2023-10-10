import webot

if __name__ == '__main__':
    print("Main program Start")
    minimum_ip = 3
    execute_time = 5
    max_step = 3
    listValidIP = webot.SSLIPcatcher(minimum_ipcount=minimum_ip)
    print(listValidIP)
    webot.Execute(listValidIP, execute_time, max_step)

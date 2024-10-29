import webot
import os
if __name__ == '__main__':
    os.system("cls")
    print("Main program Start")
    
    minimum_ip = 5
    execute_time = 120
    execute_step = 7


    address = ['https://www.youtube.com/watch?v=Ju5U3mZJYYc', 'https://www.youtube.com/watch?v=orXrSx5L0k4'
           ,'https://www.youtube.com/watch?v=sy95ABSMnPE', 'https://www.youtube.com/watch?v=8d9nIflqLUU'
           ,'https://www.youtube.com/watch?v=ddjEx5lhOGg', 'https://www.youtube.com/watch?v=AFvE3V6TBUo']

    webot.Execute(minimum_ip, execute_time, execute_step, address)
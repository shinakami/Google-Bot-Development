import webot
import os
if __name__ == '__main__':
    os.system("cls")
    print("Main program Start")
    
    minimum_ip = 7
    execute_time = 180
    execute_step = 5


    address = ['https://www.youtube.com/watch?v=muNCt2rkH3w', 'https://www.youtube.com/watch?v=vn-ze9UZX2c'
           ,'https://www.youtube.com/watch?v=13Y7JvsgplI', 'https://www.youtube.com/watch?v=iXbBTLAZ4jY'
           ,'https://www.youtube.com/watch?v=yc7Li_LLofk', 'https://www.youtube.com/watch?v=Qdt37PmrBdY'
           ,'https://www.youtube.com/watch?v=-2xVWMFF3dY', 'https://www.youtube.com/watch?v=jH9MRpaJIn8'
           ,'https://www.youtube.com/watch?v=q018elKqDws', 'https://www.youtube.com/watch?v=YmlyE94vYqU'
           ,'https://www.youtube.com/watch?v=orXrSx5L0k4', 'https://www.youtube.com/watch?v=sy95ABSMnPE'
           ,'https://www.youtube.com/watch?v=Ju5U3mZJYYc', 'https://www.youtube.com/watch?v=3TKABB3mUNA']

    webot.Execute(minimum_ip, execute_time, execute_step, address)

import time
from datetime import datetime as d

#hosts_path="/etc/hosts" #for Mac and Linux
hosts_path=r"C:\Windows\System32\drivers\etc\hosts" #for Windows
#r-passing raw string so python doesn't try to interpret \
#other solution is passing \\ in directory
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","poczta.o2.pl",\
"www.poczta.o2.pl","youtube.com","www.youtube.com","chess24.com",\
"www.chess24.com","chessarbiter.com","www.chessarbiter.com"] #blocked sites

while True: #starting infinte loop
    if d(d.now().year,d.now().month,d.now().day,8) < \
    d.now() < d(d.now().year,d.now().month,d.now().day,18): #blockade hours
        print("No surfing here - working hours!\nto break loop press ctrl C")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content: #checking if blocked already:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else: #removing blocade in blockadeless hours
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0) #return to file begining
            for line in content:
                if not any(website in line for website in website_list):
                    #rewriting just lanes with no blocade
                    file.write(line)
            file.truncate()
        print("free time ;)")
    time.sleep(60)#60 sec delay between checks

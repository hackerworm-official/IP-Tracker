import urllib.request as ur
import json
import webbrowser

print(f"""

 /$$$$$$ /$$$$$$$        /$$$$$$$$                           /$$                          
|_  $$_/| $$__  $$      |__  $$__/                          | $$                          
  | $$  | $$  \ $$         | $$  /$$$$$$  /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$ 
  | $$  | $$$$$$$/         | $$ /$$__  $$|____  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$
  | $$  | $$____/          | $$| $$  \__/ /$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/
  | $$  | $$               | $$| $$      /$$__  $$| $$      | $$_  $$ | $$_____/| $$      
 /$$$$$$| $$               | $$| $$     |  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$      
|______/|__/               |__/|__/      \_______/ \_______/|__/  \__/ \_______/|__/      
                                                                                                                           
                                Telegram Channel: @hackingworm                                              
                                                                                            """)

while True:
    ip=input("Which IP would you like to check ? : ")
    url= "http://ip-api.com/json/"
    response = ur.urlopen(url + ip)
    data = response.read()
    Values = json.loads(data)

    print(" IP: " + Values["query"])
    print(" Status: " + Values["status"])
    print(" country: " + Values["country"])
    print(" counterycode: " + Values["countryCode"])
    print(" Region: " + Values["region"])
    print(" Region name: " + Values["regionName"])
    print(" City: " + Values["city"])
    print(" ZIP: " + Values["zip"])
    print(" ISP: " + Values["isp"])
    print(" Time zone: " + Values["timezone"])
    print(" Longitude: " + str(Values["lon"]))
    print(" Lattitude: " + str(Values["lat"]))

    break

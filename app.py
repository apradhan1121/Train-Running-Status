import requests
import json
class IRCTC:
    def __init__(self):
        user_input=input("How would you like to proceed?"
              "1.Enter 1 to train schedule")
        if user_input=="1":
            self.trainschedule()
    def trainschedule(self):
        train_no=input("Enter the train no.")
        self.fetchdata(train_no)

    def fetchdata(self,train_no):
        url = "https://irctc1.p.rapidapi.com/api/v1/liveTrainStatus"

        querystring = {"trainNo": train_no, "startDay": int(input("provide start day"))}

        headers = {
            "X-RapidAPI-Key": "a1c743d23bmshb0243aa50cabc66p1e8b33jsne2725585980c",
            "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        x=(response.text)                           #Output is in String format
        y=json.loads(x)                             #converting string into dictionary using json
        print("The data is Successfully Generated")
        print(y)
        print(y['data'])
        print("Select the given data")
        for i in y['data']:
            print(i)
        o=y['data']                                      #it only works for the data which are connected dictonary format like : upcoming Stations previous stations delay etc.
        m=o[input("Select the given data  ")]                                   #upcoming_stations
        m=list(m)
        print(m)

        u = (m[0])
        print(u)
        print()
        print()


        for i in range(1,len(m)):
            u=(m[i])
            print(u)
            # print(u['station_name'])
        for i in u:
            print(i)

        z = (input("Select the Station Name"))                               #station_name
        for i in range(1,len(m)):
            u=(m[i])
            print(u[z],u['std'])



#upcoming_stations
#station_name
#stoppage_number



obh=IRCTC()
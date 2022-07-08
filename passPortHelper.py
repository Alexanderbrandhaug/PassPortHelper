import requests
import time



headers = requests.utils.default_headers()

def chooseOffice(politistasjon):
    url = "https://pass-og-id.politiet.no/qmaticwebbooking/rest/schedule/appointmentProfiles"
    response = requests.request("GET", url, headers=headers)
    response = response.json()
    for x in response:
        if politistasjon == x['branchName']:
            return x['branchPublicId']

    

def checkDate(fromDate, stopDate, politistasjon):
    fromDateOriginal = fromDate
    stopDateDay = stopDate.split("-")[2]
    stopDateDay = int(stopDateDay)
    politistasjon = chooseOffice(politistasjon)
    
    hit = True
    while hit:
        print("Checking for available appointments between: " + fromDate + " " + stopDate)
        time.sleep(30)
        fromDateDay = fromDate.split("-")[2]
        url = "https://pass-og-id.politiet.no/qmaticwebbooking/rest/schedule/branches/"+politistasjon+"/dates/"+fromDate+"/times;servicePublicId=8e859bd4c1752249665bf2363ea231e1678dbb7fc4decff862d9d41975a9a95a;customSlotLength=15"
        response = requests.request("GET", url, headers=headers)
        response = response.json()
        
        if int(fromDateDay) == stopDateDay:
            fromDate = fromDateOriginal
            continue
        
        if not response and (int(fromDateDay) is not stopDateDay):
            fromDateDay = int(fromDateDay) + 1
            fromDateDay = str(fromDateDay)
            fromDate = fromDate.split("-")
            fromDate[2] = fromDateDay
            if len(fromDateDay) == 1:
                fromDateDay = "0"+fromDateDay
                fromDate = str(fromDate[0]+ "-"+ fromDate[1]+"-"+fromDateDay)
            
            else:
                fromDate = str(fromDate[0]+ "-"+ fromDate[1]+"-"+fromDate[2])
                
        if response:
            print(response)
            hit = False


checkDate("2022-08-15", "2022-08-20","Heimdal politistasjon")

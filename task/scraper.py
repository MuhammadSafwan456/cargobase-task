import requests
from bs4 import BeautifulSoup

base_url = "https://www.flightstats.com/v2/flight-tracker"


def scrap_flight_details(airline_code, flight_number, date_):
    buffer = {"airline": {},
             "source": {},
             "destination": {}}
    year, month, date = date_.split("-")
    url = f'{base_url}/{airline_code}/{flight_number}?year={year}&month={month}&date={date}'
    rsp = requests.get(url)
    print("rsp.status_code",rsp.status_code)
    if rsp.status_code == 200:
        details = BeautifulSoup(rsp.content, "html.parser")
        flight_status = details.find("h2", class_="layout-row__Title-sc-1uoco8s-4 kaIMhA").text
        print("flight_status-------->",flight_status)
        if flight_status == "Flight Status":
            buffer["status"] = details.find("div", class_="ticket__StatusContainer-sc-1rrbl5o-17").text.replace("Scheduled", "")
            buffer["airline"]["name"] = details.find("div", class_="text-helper__TextHelper-sc-8bko4a-0 eOUwOd").text
            buffer["airline"]["code"] = airline_code
            buffer["airline"]["number"] = flight_number
            for i, info in enumerate(["source", "destination"]):
                buffer[info]["city"], buffer[info]["code"], buffer[info]["country"] = details.find_all("div", class_="text-helper__TextHelper-sc-8bko4a-0 efwouT")[i].text.split(",")
                buffer[info]["details"] = {}
                buffer[info]["details"]["airport"] = {}
                buffer[info]["details"]["airport"]["name"] = details.find_all("div", class_="text-helper__TextHelper-sc-8bko4a-0 cHdMkI")[i].text 
                buffer[info]["details"]["airport"]["code"] = details.find_all("a", class_="route-with-plane__AirportLink-sc-154xj1h-3 kCdJkI")[i].text 
                buffer[info]["details"]["scheduled"] = {}
                time_info = details.find_all("div", class_="text-helper__TextHelper-sc-8bko4a-0 kbHzdx")
                buffer[info]["details"]["scheduled"]["time"], buffer[info]["details"]["scheduled"]["timezone"] = time_info[i*2].text.split(" ")
                buffer[info]["details"]["estimated"] = {}
                buffer[info]["details"]["estimated"]["time"], buffer[info]["details"]["estimated"]["timezone"] = time_info[i*2+1].text.split(" ")
                buffer[info]["details"]["date"] = date_
                gate_info = details.find_all("div", class_="ticket__TGBValue-sc-1rrbl5o-16 hUgYLc text-helper__TextHelper-sc-8bko4a-0 kbHzdx")
                buffer[info]["details"]["terminal"] = gate_info[i*2].text
                buffer[info]["details"]["gate"] = gate_info[i*2+1].text
            return buffer
        else:
            return {
                "status": "Flight data not available"
            }
    return None




# info = get_flight_details("AA", f_n, "20-8-2022")
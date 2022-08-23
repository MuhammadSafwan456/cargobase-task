from celery import shared_task
from .scraper import scrap_flight_details
from .serializers import FlightInfoSerializer

@shared_task(name="scrapt-flight-info")
def scrap_flight_info(airline_code, flight_number, date_):
    info = scrap_flight_details(airline_code, flight_number, date_)
    data = {
        "airline": airline_code,
        "flight_number": flight_number,
        "date": date_,
        "info": info
    }
    serializer = FlightInfoSerializer(data=data)
    if not serializer.is_valid():
        print("serializer.errors", serializer.errors)
        return  
    print("saving data------------>")
    # serializer.save()

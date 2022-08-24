from celery import shared_task

from task.models import FlightInfo
from .scraper import scrap_flight_details
from .serializers import FlightInfoSerializer
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@shared_task(name="scrapt_flight_info")
def scrap_flight_info(airline_code, flight_number, date_):
    info = scrap_flight_details(airline_code, flight_number, date_)
    default = {"info": info}
    FlightInfo.objects.update_or_create(
        airline=airline_code, flight_number=flight_number, date=date_, defaults=default
    )
    logger.info("saving task")

# cargobase-task

# How to Run,
```sh
1- Clone the repo
2- pip install requirements.txt
3- python manage.py migrate
4- python manage.py runserver (to start the app)
5- celery -A cargobase worker -l INFO (to start the celery)
```

There are 3 Endpoints as mentions below:

# SCRAP DATA
```sh
- URL: http://127.0.0.1:8000/task/scrap/
- METHOD: GET
- Query Params: 
  - airline -> required
  - flight_number -> required
  - date -> required
- RETURN: task id of background Async Task
```
# GET STATUS
```sh
- URL: http://127.0.0.1:8000/task/<task_id>/status/
- METHOD: GET
- Path Params: 
  - task_id -> task-id return by previous API
- RETURN: status of background Async Task
```
# GET DATA
```sh
- URL: http://127.0.0.1:8000/task/info/
- METHOD: GET
- Query Params: 
  - airline -> optional
  - flight_number -> optional
  - date -> optional
- RETURN: flight info according to query params
```

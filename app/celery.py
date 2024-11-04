from celery import Celery

# Define Celery application
celery_app = Celery(
    "worker",
    backend="rpc://",
    broker="pyamqp://guest:guest@rabbitmq//"
)
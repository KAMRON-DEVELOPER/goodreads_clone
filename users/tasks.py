import os
from celery import Celery
from django.core.mail import send_mail

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def send_email():

    send_mail(
        subject='Welcome home!',
        message=f"Hi user Kamronbek",
        from_email='atajanovkamronbek2003@gmail.com',
        recipient_list=['atajanovkamronbek2003@gmail.com', 'dangersenator577@gmail.com'],
    )


    # send_mail(
    #     subject,
    #     message,
    #     "atajanovkamronbek2003@gmail.com",
    #     recipient_list
    # )








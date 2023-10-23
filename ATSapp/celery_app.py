from celery import Celery

app = Celery('app', broker='redis://redis:6379/0')


app.conf.update(
    result_backend='redis://redis:6379/0',
    # task_routes={
    #     'app.main.*': {'queue': 'ATSapp-queue'},
    # }
)


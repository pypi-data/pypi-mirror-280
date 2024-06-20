import asyncio
import datetime
import json
import threading

from celery.apps.beat import Beat
from celery.beat import PersistentScheduler
from celery.utils.imports import symbol_by_name
from django.utils import timezone

from django_celery_beat_endpoint import __version__


class AwareThread(threading.Thread):
    def __init__(self, beat, port, http_server_cls):
        self.beat = beat
        self.port = port
        self.http_server_cls = http_server_cls
        super(AwareThread, self).__init__(daemon=True)

    def run(self):
        asyncio.set_event_loop(asyncio.new_event_loop())

        print(
            self.beat.colored.green(
                f"Serving celery beat status v{__version__} on port {self.port} using {self.http_server_cls}."
            )
        )

        server = symbol_by_name(self.http_server_cls)(beat=self.beat, port=self.port)
        server.serve()


class AwareBeat(Beat):
    def run(self):
        port = self.app.conf.beat_port
        http_server_cls = self.app.conf.beat_http_server

        AwareThread(self, port, http_server_cls).start()
        super(AwareBeat, self).run()

    def ping(self):
        self.get_periodic_tasks()
        return True

    def get_periodic_tasks(self):
        if symbol_by_name(self.scheduler_cls) == PersistentScheduler:
            schedule = self.Service(
                app=self.app,
                max_interval=self.max_interval,
                scheduler_cls=self.scheduler_cls,
                schedule_filename=self.schedule,
            ).scheduler.get_schedule()
        else:
            from django_celery_beat.schedulers import DatabaseScheduler

            schedule = DatabaseScheduler(self.app).all_as_schedule()

        tasks = list()
        for key, entry in schedule.items():
            is_due, next_time_to_check = entry.is_due()

            tz = entry.schedule.tz
            last_run_at = entry.last_run_at.astimezone(tz)
            next_excecution = (
                timezone.now() + datetime.timedelta(seconds=next_time_to_check)
            ).astimezone(tz)

            tasks.append(
                {
                    "name": key,
                    "task": entry.task,
                    "args": "({})".format(
                        ",".join(
                            [json.dumps(arg, ensure_ascii=False) for arg in entry.args]
                        )
                    ),
                    "last_run_at": last_run_at.strftime("%Y-%m-%d %H:%M:%S"),
                    "schedule": str(entry.schedule),
                    "kwargs": json.dumps(entry.kwargs, ensure_ascii=False),
                    "is_due": is_due,
                    "next_excecution": next_excecution.strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
        return tasks

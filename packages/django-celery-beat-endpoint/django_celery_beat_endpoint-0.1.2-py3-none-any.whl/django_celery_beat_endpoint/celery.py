from functools import cached_property

from celery import Celery

from django_celery_beat_endpoint.defaults import DEFAULTS


class AwareCelery(Celery):
    @cached_property
    def Beat(self, **kwargs):
        return self.subclass_with_self("django_celery_beat_endpoint.beat:AwareBeat")

    def _load_config(self):
        conf = super()._load_config()
        self.add_defaults(DEFAULTS)
        return conf

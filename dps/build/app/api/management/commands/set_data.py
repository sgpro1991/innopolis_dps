from django.core.management.base import BaseCommand, CommandError
from api.models import *
import random
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Создать тестовые данные для проверки'

    def handle(self, *args, **options):
        a = random.random()
        for i in range(3000):
            longitude = random.uniform( -100, 100 )
            latitude = random.uniform( -100, 100 )
            insert = Station(longitude=longitude,latitude=latitude,timezone="MSK")
            insert.save()
            d1 = date(2018, 8, 15)
            d2 = date(2018, 9, 15)
            delta = d2 - d1
            for i in range(delta.days + 1):
                d = (d1 + timedelta(i))
                t_air = random.uniform( -30, 30 )
                insert_air = Air(station=Station.objects.get(id=insert.id), t_air=t_air, datetime=d)
                insert_air.save()
        self.stdout.write("ok")

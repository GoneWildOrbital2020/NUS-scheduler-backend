from datetime import datetime
from django.db import models
from calendars.models import Month, Day
from users.models import UserCustom


class EventGroup(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(
        UserCustom, on_delete=models.CASCADE, null=True, blank=True, related_name='event_group')

    def __str__(self):
        return self.name

    class meta():
        unique_together = ['name', 'user']


class RepeatedEvent(models.Model):
    name = models.TextField()
    group = models.ForeignKey(
        EventGroup, on_delete=models.CASCADE, null=True, blank=True, related_name='repeated')


class Event(models.Model):
    index = models.IntegerField()
    title = models.TextField()
    description = models.TextField()
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    location = models.TextField()
    color = models.TextField(default="#6B7F82")
    day = models.ForeignKey(
        Day, on_delete=models.CASCADE,  null=True, blank=True)
    group = models.ForeignKey(
        EventGroup, on_delete=models.CASCADE, null=True, blank=True,)
    repeated_event = models.ForeignKey(
        RepeatedEvent, on_delete=models.CASCADE, null=True, blank=True,)

    def __str__(self):
        return self.title

    @staticmethod
    def parse(data, user):
        splitted = data.split('\r\n')[:-1]
        data_dict = {}
        dates = []
        for item in splitted:
            [key, value] = item.split(':')
            if key == "EXDATE":
                dates.append(value[:8])
            else:
                data_dict[key] = value
        group, _ = user.event_group.get_or_create(
            name=data_dict["SUMMARY"].split(" ", 1)[0])
        repeated_event, _ = group.repeated.get_or_create(
            name=data_dict["SUMMARY"], group=group)
        year = data_dict["DTSTART"][:4]
        events_count = Event.objects.filter(
            day__month__year__index=year, day__month__year__user=user).count() + 1
        month = data_dict["DTSTART"][4:6]
        day = data_dict["DTSTART"][6:8]
        data_dict['DESCRIPTION'] = data_dict['DESCRIPTION'].replace("\\n", " ")
        if data_dict["SUMMARY"].split(" ")[1] == "Exam":
            year_obj, _ = user.year_set.get_or_create(index=year)
            month_obj, _ = year_obj.month_set.get_or_create(
                month_name=Month.get_month_code(int(month)-1))
            day_obj, _ = month_obj.day_set.get_or_create(index=int(day))
            Event.objects.create(index=events_count, title=data_dict["SUMMARY"], description=data_dict["DESCRIPTION"],
                                 start=datetime(year=2020, month=1, day=1, hour=int(data_dict["DTSTART"][9:11]), minute=int(data_dict["DTSTART"][11:13])), end=datetime(year=2020, month=1, day=1, hour=int(data_dict["DTEND"][9:11]), minute=int(data_dict["DTEND"][11:13])), location="Exam Hall", day=day_obj, group=group, repeated_event=repeated_event)
            return
        count = 0
        rules = data_dict["RRULE"].split(';')
        while(count < int(rules[1][6:])):
            year_obj, _ = user.year_set.get_or_create(index=year)
            month_obj, _ = year_obj.month_set.get_or_create(
                month_name=Month.get_month_code(int(month)-1))
            day_obj, _ = month_obj.day_set.get_or_create(index=int(day))
            if (year + month + day) not in dates:
                Event.objects.create(index=events_count, title=data_dict["SUMMARY"], description=data_dict["DESCRIPTION"],
                                     start=datetime(year=2020, month=1, day=1, hour=int(data_dict["DTSTART"][9:11]), minute=int(data_dict["DTSTART"][11:13])), end=datetime(year=2020, month=1, day=1, hour=int(data_dict["DTEND"][9:11]), minute=int(data_dict["DTEND"][11:13])), location=data_dict["LOCATION"], day=day_obj, group=group, repeated_event=repeated_event)
                events_count = events_count + 1

            next_week = month_obj.get_next_week(day)
            if len(next_week) == 1:
                next_week = "0" + next_week
            if day > next_week:
                month = str(int(month) + 1)
                if len(month) == 1:
                    month = "0" + month
            day = next_week
            count = count + 1
        return "success"

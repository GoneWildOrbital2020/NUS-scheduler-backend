from django.db import models
from calendars.models import Day
from users.models import UserCustom


class EventGroup(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(
        UserCustom, on_delete=models.CASCADE, null=True, blank=True, related_name='owner')

    def __str__(self):
        return self.name


class Event(models.Model):
    index = models.IntegerField()
    title = models.CharField(max_length=30)
    description = models.TextField()
    start = models.TextField()
    end = models.TextField()
    location = models.TextField()
    color = models.TextField(default="#FFFFFF")
    day = models.ForeignKey(Day, on_delete=models.CASCADE, default=1)
    group = models.ForeignKey(
        EventGroup, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    @staticmethod
    def parse(data):
        data.replace("\n", "")
        splitted = data.split('\n')
        data_dict = {}
        dates = []
        desc = False
        for item in splitted:
            if desc:
                if item == "END:VEVENT":
                    break
                data_dict["DESCRIPTION"] = data_dict["DESCRIPTION"] + "\n" + item
            else:
                [key, value] = item.split(':')
                if key == "EXDATE":
                    dates.append(value[:8])
                else:
                    data_dict[key] = value
                    if key == "DESCRIPTION":
                        desc = True
        count = 0
        rules = data_dict["RRULE"].split(';')
        year = data_dict["DTSTART"][:4]
        month = data_dict["DTSTART"][4:6]
        day = data_dict["DTSTART"][6:8]
        while(count < rules[1][6:]):
            count = count + 1
        return "success"

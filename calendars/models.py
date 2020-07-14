from django.db import models
from users.models import UserCustom


class Year(models.Model):
    index = models.IntegerField()
    user = models.ForeignKey(UserCustom, on_delete=models.CASCADE, default=1)
    is_leap = models.BooleanField(default=False)

    def __str__(self):
        return str(self.index)

    @staticmethod
    def check_leap(year):
        if year % 4 != 0:
            return False
        else:
            if year % 100 != 0:
                return True
            else:
                if year % 400 == 0:
                    return True
                else:
                    return False

    class Meta:
        unique_together = ['index', 'user']


class Month(models.Model):
    MONTH_CHOICES = (
        ('JAN', 'January'),
        ('FEB', 'February'),
        ('MAR', 'March'),
        ('APR', 'April'),
        ('MAY', 'May'),
        ('JUN', 'June'),
        ('JUL', 'July'),
        ('AUG', 'August'),
        ('SEP', 'September'),
        ('OCT', 'October'),
        ('NOV', 'November'),
        ('DEC', 'December'),
    )

    MONTH_LENGTH_LEAP = {
        'JAN': 31,
        'FEB': 29,
        'MAR': 31,
        'APR': 30,
        'MAY': 31,
        'JUN': 30,
        'JUL': 31,
        'AUG': 31,
        'SEP': 30,
        'OCT': 31,
        'NOV': 30,
        'DEC': 31,
    }

    MONTH_LENGTH = {
        'JAN': 31,
        'FEB': 28,
        'MAR': 31,
        'APR': 30,
        'MAY': 31,
        'JUN': 30,
        'JUL': 31,
        'AUG': 31,
        'SEP': 30,
        'OCT': 31,
        'NOV': 30,
        'DEC': 31,
    }

    month_name = models.CharField(max_length=3, choices=MONTH_CHOICES)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, default=1)

    def get_month_length(self):
        if self.year.is_leap:
            return self.MONTH_LENGTH_LEAP[self.month_name]
        else:
            return self.MONTH_LENGTH[self.month_name]

    def get_next_week(self, day):
        if self.year.is_leap:
            nex = (int(day) + 7) % self.MONTH_LENGTH_LEAP[self.month_name]
            if nex == 0:
                nex = self.MONTH_LENGTH_LEAP[self.month_name]
            return str(nex)
        else:
            nex = (int(day) + 7) % self.MONTH_LENGTH[self.month_name]
            if nex == 0:
                nex = self.MONTH_LENGTH[self.month_name]
            return str(nex)

    @ staticmethod
    def get_month_code(index):
        return Month.MONTH_CHOICES[index][0]

    def __str__(self):
        return self.month_name

    class Meta:
        unique_together = ['month_name', 'year']


class Day(models.Model):
    index = models.IntegerField()
    month = models.ForeignKey(Month, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.index)

    class Meta:
        unique_together = ['index', 'month']

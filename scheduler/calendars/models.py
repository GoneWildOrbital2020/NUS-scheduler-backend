from django.db import models


class Year(models.Model):
    index = models.IntegerField()

    def __str__(self):
        return str(self.index)


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

    MONTH_LENGTH = {
        'JAN': 31,
        'FEB': 29,  # kalo mo lebih bagus bisa detect kabisat ato ga, tp ya nanti deh
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
        return self.MONTH_LENGTH[self.month_name]

    @staticmethod
    def get_month_code(index):
        return Month.MONTH_CHOICES[index][0]

    def __str__(self):
        return self.month_name


class Day(models.Model):
    index = models.IntegerField()
    month = models.ForeignKey(Month, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.index)

from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    event_cost = models.CharField(max_length=4, default='0', help_text="Leave empty if zero.")
    event_reg_type = models.CharField(choices=[('1', 'SINGLE'), ('2', 'GROUP')], max_length=1)

    def __str__(self):
        return self.event_name

class MyUser(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    institute_type = models.CharField(choices=[('School', 'SCHOOL'), ('College', 'COLLEGE')], max_length=8)
    institute_name = models.CharField(max_length=110)
    email = models.EmailField(max_length=254, unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    date = models.DateField(auto_now_add=True, auto_now=False)
    registered_events = models.ManyToManyField(Event, related_name='u_events',)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class MyGroup(models.Model):
    title = models.CharField(max_length=60)
    leader_name = models.CharField(max_length=60)
    persons = models.CharField(max_length=200)
    institute_type = models.CharField(choices=[('School', 'SCHOOL'), ('College', 'COLLEGE')], max_length=8)
    institute_name = models.CharField(max_length=110)
    registered_events = models.ManyToManyField(Event, related_name='g_events',)
    email = email = models.EmailField(max_length=254, unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    date = models.DateField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    def members_as_list(self):
        return self.persons.split(';')



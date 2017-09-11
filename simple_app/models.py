from django.db import models


class Event(models.Model):
    external_id = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)

    # this fields better to use as related models lines, but not necessary for test example
    tags = models.CharField(max_length=100, blank=True, null=True)
    persons = models.CharField(max_length=200, blank=True, null=True)

    image_source = models.CharField(max_length=255, blank=True, null=True)
    resource_url = models.CharField(max_length=255, blank=True, null=True)
    duration = models.IntegerField(verbose_name='Event will be go on around', blank=True, null=True)
    legal_age = models.IntegerField(verbose_name='It is forbidden to visit before', blank=True, null=True)
    price_min = models.FloatField(blank=True, null=True)
    price_max = models.FloatField(blank=True, null=True)

    def __str__(self):
        return '{}-{}'.format(self.external_id or 'no-id', self.title)


class Place(models.Model):
    external_id = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=100, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    image_source = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '{}-{}'.format(self.external_id or 'no-id', self.name)


class Schedule(models.Model):
    external_id = models.CharField(max_length=50, blank=True, null=True)
    # may be more than one event at one time
    event = models.ForeignKey(Event)
    # as well as some events may be placed in different locations
    place = models.ForeignKey(Place)
    starts = models.DateTimeField()
    ends = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} in {} at {}/{}'.format(self.event, self.place, self.starts, self.ends)
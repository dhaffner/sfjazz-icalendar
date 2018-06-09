import json

from ics import Calendar, Event
c = Calendar()
# e = Event()
# e.name = "My cool event"
# e.begin = '20140101 00:00:00'
# c.events.add(e)
# print(c.events)
# print(c)

with open('src/data.json', 'r') as f:
    sfjazz_events = json.load(f)


def transform(sfjazz_event):
    e = Event()
    e.name = sfjazz_event['name']
    e.begin = sfjazz_event['eventDate']
    # TODO : map more fields
    return e


events = map(transform, sfjazz_events)
c.events.update(events)
print(c)
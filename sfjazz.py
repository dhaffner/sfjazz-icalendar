import json
import sys

from html.parser import HTMLParser

import arrow

from ics import Calendar, Event


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    if html:
        s = MLStripper()
        html = s.unescape(html)
        s.feed(html)
        return s.get_data()


def transform(e):
    return Event(
        uid=e['id'],
        name=e['name'],
        begin=(
            arrow.get(e['eventDate'])
                 .replace(tzinfo='US/Pacific')
        ),
        description=strip_tags(e.get('secondaryName')),
        location=e['venueName'],
        url=f'http://sfjazz.org{e["detailsLink"]}'
    )


if __name__ == '__main__':
    c = Calendar()
    c.events.update(map(transform, json.load(sys.stdin)))
    print(c)

# Kal/utils.py

from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formatuje dzień jako td
	# filtruj wydarzenia według dnia
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		for event in events_per_day:
			d += f'<li> {event.title} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formatuje tydzień jako tr 
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formatuje miesiąc jako tabelę
	# filtruj wydarzenia według roku i miesiąca
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

		kal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		kal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		kal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			kal += f'{self.formatweek(week, events)}\n'
		return kal
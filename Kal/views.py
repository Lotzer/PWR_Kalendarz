# cal/views.py

from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # dzisiejsza data do kalendarza 
        d = get_date(self.request.GET.get('day', None))

        # tworzymy instancje klasy Calendar z dzisiejsza data
        Kal = Calendar(d.year, d.month)

        # zwracamy kalendzarz jako tabele
        html_Kal = Kal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_Kal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


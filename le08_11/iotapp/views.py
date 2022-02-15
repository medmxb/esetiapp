from datetime import datetime, timedelta

import telepot
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView

from .models import don
import csv


def sendtele():
    token = '2112940431:AAFvEGA8V0ZXvn0Jao1GsFW5UqMIdZe-qlk'
    rece_id = 2115040562
    bot = telepot.Bot(token)
    bot.sendMessage(rece_id, 'la température depasse la normale')
    print(bot.sendMessage(rece_id, 'OK.'))


def data(request):
    tab1 = don.objects.all()
    s = {'tab1': tab1}
    return render(request, 'app/tables.html', s)


def home(request):
    return HttpResponse('bonjour à tous')


def exp_csv(request):
    obj = don.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=DHT.csv'
    writer = csv.writer(response)
    writer.writerow(['Air Temperature', 'Air humidity', 'Soil Humidity', 'LUX', 'Irrigation duration',
                     'Power Consumption', 'Flow Rate', 'Soil Temperature', 'Electrical Conductivity', 'Soil Salinity'
                     , 'Creation Date'])
    studs = obj.values_list('ta','ha', 'sm', 'lux','tmp', 'p', 'qua','tg', 'ecg', 'salg', 'dt')
    for std in studs:
        writer.writerow(std)
    return response


def dht11(request):
    tab = don.objects.order_by('id')
    tab1 = don.objects.values()
    list2 = (list(tab1))[-1]
    temp1 = list2['temp']
    hum1 = list2['hum']
    dt1 = list2['dt']
    list1=(list(tab1))[-3:]

    if temp1 > 40 :
        sendtele()
        send_mail(
            'température dépasse la normale,' + str(temp1),
            'anomalie dans la machine le,' + str(dt1),
            'yassine.ayat@ump.ac.ma',
            ['yassine1960ayat@gmail.com'],
            fail_silently=False,
        )

    s = {'tab': tab,"list1":list1,"list2":list2,"temp1":temp1,"hum1":hum1,"dt1":dt1}

    return render(request, 'app/app.html', s)


def chart(request):
    tab = don.objects.order_by('id')
    tab1 = don.objects.values()
    list2 = (list(tab1))[-1]
    temp1 = list2['temp']
    hum1 = list2['hum']
    dt1 = list2['dt']
    list1=(list(tab1))[-7:]

    if temp1 > 40 :
        send_mail(
            'température dépasse la normale,' + str(temp1),
            'anomalie dans la machine le,' + str(dt1),
            'yassine.ayat@ump.ac.ma',
            ['yassine1960ayat@gmail.com'],
            fail_silently=False,
        )

    s1 = {'tab': tab,"list1":list1,"list2":list2,"temp1":temp1,"hum1":hum1,"dt1":dt1}

    return render(request, 'app/charts.html', s1)


class EditorChartView(TemplateView):
    template_name = 'app/charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tab"] = don.objects.all()
        return context


class ChartView1(TemplateView):
    template_name = 'app/charts1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tab"] = don.objects.all()
        return context


class ChartView2(TemplateView):
    template_name = 'app/charts2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tab"] = don.objects.all()
        return context


class ChartView3(TemplateView):
    template_name = 'app/charts3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tab"] = don.objects.all()
        return context


class ChartView4(TemplateView):
    template_name = 'app/charts4.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tab"] = don.objects.all()
        return context


class ChartView5(TemplateView):
    template_name = 'app/charts5.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tab"] = don.objects.all()
        return context


class ChartView6(TemplateView):
    template_name = 'app/charts6.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tab"] = don.objects.all()
        return context


class ChartView7(TemplateView):
    template_name = 'app/charts7.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tab"] = don.objects.all()
        return context


class ChartView8(TemplateView):
    template_name = 'app/charts8.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tab"] = don.objects.all()
        return context


class ChartView9(TemplateView):
    template_name = 'app/charts9.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tab"] = don.objects.all()
        return context


class ChartView10(TemplateView):
    template_name = 'app/charts10.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tab"] = don.objects.all()
        return context


class EditorChartView1(TemplateView):
    template_name = 'app/app.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tab"] = don.objects.all()
        context["tab1"] = don.objects.last()
        context['now'] = datetime.now()
        context['t'] = (context['now']-context["tab1"].dt)
        print(don.objects.all())
        return context

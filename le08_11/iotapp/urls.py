
from django.urls import path

from iotapp import views
from iotapp import api

urlpatterns = [

    path('data/', views.data, name = 'Data'),
    path('home/', views.home, name = 'Home'),
    path('csv/', views.exp_csv, name = 'exp-csv'),
    path('', views.EditorChartView1.as_view(), name = 'DB'),
    path('charts/1', views.ChartView1.as_view(), name = 'CH'),
    path('charts/2', views.ChartView2.as_view(), name = 'CH2'),
    path('charts/3', views.ChartView3.as_view(), name = 'CH3'),
    path('charts/4', views.ChartView4.as_view(), name = 'CH4'),
    path('charts/5', views.ChartView5.as_view(), name = 'CH5'),
    path('charts/6', views.ChartView6.as_view(), name = 'CH6'),
    path('charts/7', views.ChartView7.as_view(), name = 'CH7'),
    path('charts/8', views.ChartView8.as_view(), name = 'CH8'),
    path('charts/9', views.ChartView9.as_view(), name = 'CH9'),
    path('charts/10', views.ChartView10.as_view(), name = 'CH10'),
    ##api
    path('api/list', api.Dlist, name='DHT11List'),

    # genericViews
    path('api/post', api.Dhtviews.as_view(), name='DHT_post'),
]
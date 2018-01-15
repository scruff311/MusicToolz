from django.conf.urls import url
from django.views.generic import TemplateView
# from . import views

app_name = 'setlist_builder'
urlpatterns = [
    url(r'^', TemplateView.as_view(template_name='index.html')),
    # url(r'^$', '../frontend/build/index.html'),
    # url(r'^$', views.index, name='index'),
    # url(r'^filter_out_starters/$', views.filter_out_starters, name='filter_out_starters'),
    # url(r'^results/(?P<result>[^/]+)/$', views.results, name='results'),
    # url(r'^results/$', views.results, name='results'),
    # url(r'^generate/$', views.generate, name='generate'),
]
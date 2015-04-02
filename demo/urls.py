from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from letter_counter import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^counter$', TemplateView.as_view(template_name= 'input_word.html')),
    url(r'^count-letters$', views.letter_counter)
)

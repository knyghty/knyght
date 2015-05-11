from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

import debug_toolbar


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^__debug__/', include(debug_toolbar.urls)),
]

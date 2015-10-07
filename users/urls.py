from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns(
    '',
    # the view to register our user with a third party token
    # the backend is the python social auth backend e.g. facebook
    url(r'^register-by-token/(?P<backend>[^/]+)/$',
        views.register_by_access_token),
    url(r'^$',views.index, name='index'),
    url(r'^availability/$', views.CheckAvailabilityApiView.as_view(), name='my_rest_view'),
    url(r'^profile/$',views.profileApiView.as_view(), name='profileView'),
)
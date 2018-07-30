from django.conf.urls import url, include
from django.http import Http404
from wedsite.views import (
    StaticView, StaticViewNoAuth, RSVPCSVView, RSVPView, CreateAccountView
)
from django.contrib.auth.views import (
    LoginView, PasswordResetView, PasswordChangeView, PasswordChangeDoneView,
    LogoutView)
from wedsite.conf import settings

from . import views

def get_url(uri, name):
    """
    Given a URI and a name will create the url object for the
    urlpatterns list
    """
    template = "{}.html".format(name)

    if settings.WEDSITE_JSON["access"][name] == "all":
        view = StaticViewNoAuth.as_view(template=template)
    elif settings.WEDSITE_JSON["access"][name] == "login":
        view = StaticView.as_view(template=template)
    else:
        # TODO actual styled 404 page
        view = StaticViewNoAuth.as_view(template="404.html")

    return url(r'^{}$'.format(uri), view, name=name)

urlpatterns = [

    # Top-level URL serves the main index view
    get_url('', 'index'),
    get_url('contact', 'contact'),
    get_url('story', 'story'),
    get_url('wedding', 'wedding'),
    get_url('events', 'events'),
    get_url('travel', 'travel'),
    get_url('explore', 'explore'),
    get_url('gifts', 'gifts'),
    get_url('team', 'team'),
    get_url('traditions', 'traditions'),
    url(r'^rsvp$', RSVPView.as_view(), name='rsvp'),
    url(r'^create-account$', CreateAccountView.as_view(), name='create-account'),
    url(r'^guestlist.csv$', RSVPCSVView.as_view(), name='guestlist.csv'),
]

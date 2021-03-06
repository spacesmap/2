from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [

    url(r'^list-space/$', view=views.PlaceAdd.as_view(), name='list-space'),
    url(r'^list-space/place_add_description$', view=views.PlaceAddDescriptionView.as_view(), name='place_add_description'),
    url(r'^list-space/place_add_contact_details$', view=views.PlaceAddContactDetailsView.as_view(), name='place_add_contact_details'),
    url(r'^list-space/place_add_amenities', view=views.PlaceAddAmenitiesView.as_view(), name='place_add_amenities'),
    url(r'^list-space/place_add_location', view=views.PlaceAddLocationView.as_view(), name='place_add_location'),
    url(r'^list-space/place_add_meeting_rooms', view=views.PlaceAddMeetingRoomsView.as_view(), name='place_add_meeting_rooms'),
    url(r'^list-space/success', view=views.PlaceAddContinue.as_view(), name='list-space-success'),


    url(r'^list-space/dropzone', view=views.PhotoDropzone.as_view(), name='list-space-dropzone'),
    url(r'^list-space/header', view=views.PhotoDropzone.as_view(), name='header'),
    url(r'^list-space/header-edit', view=views.PhotoDropzone.as_view(), name='header-edit'),
    # url(r'^list-space/$', view=views.PlaceAdd.as_view(), name='list-space'),


    url(r'^(?P<country>[\w-]+)/$', view=views.PlaceView.as_view(), name='country'),
    url(r'^(?P<country>[\w-]+)/(?P<city>[\w-]+)/$', view=views.PlaceView.as_view(), name='city'),
    url(r'^(?P<country>[\w-]+)/(?P<city>[\w-]+)/(?P<place>[\w-]+)/$', view=views.PlaceView.as_view(), name='place'),
    # url(r'^(?P<city>[\w-]+)/(?P<place>.*)/$', view=views.Place.as_view(), name='place'),



]

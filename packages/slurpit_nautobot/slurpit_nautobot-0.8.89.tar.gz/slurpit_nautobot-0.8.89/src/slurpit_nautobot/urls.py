from django.urls import include, path
from . import views
from . import models
from nautobot.dcim.models import Device

urlpatterns = (    
    ## setting ##
    path("settings/",           views.SettingsView.as_view(), name="settings"),
    
    ## onboard device ##
    path('devices/',            views.SlurpitImportedDeviceListView.as_view(), name='importeddevice_list'),
    path('devices/onboard',     views.SlurpitImportedDeviceOnboardView.as_view(), name='onboard'),
    path('devices/import',      views.ImportDevices.as_view(), name='import'),

    ## data mapping ##
    path('data_mapping/',       views.DataMappingView.as_view(), name='data_mapping_list'),

    ## reconcile ##
    path('reconcile/',          views.ReconcileView.as_view(), name='reconcile_list'),
    path('reconcile/<uuid:pk>/<str:reconcile_type>', views.ReconcileDetailView.as_view(), name='reconcile_detail'),
    ## logging ##
    path('slurpitlog/',         views.LoggingListView.as_view(), name='slurpitlog_list'),

    path(
        "devices/<uuid:pk>/slurpit_planning/", 
        views.SlurpitPlanningning.as_view(), 
        name="slurpit_planning",
    ),

    ## Planning ##
    path("slurpitplannings/",   views.SlurpitPlanningListView.as_view(), name="slurpitplanning_list"),
    
)

from django.urls import path, include
from applications.v1.views import service as service_views
from applications.v1.views import package as package_views
from applications.v1.views import deliverable as deliverable_views

service_urls = [
    path(
        '',
        service_views.ServiceResume.as_view(),
        name='service_resume'),
    path(
        'servicelist/',
        service_views.ServiceList.as_view(),
        name='service_list'),
    path(
        '<int:id>/',
        service_views.ServiceResume.as_view(),
        name='service_detail')
]

package_urls = [
    path(
        '',
        package_views.PackageResume.as_view(),
        name='service_resume'),
    path(
        'packagelist/',
        package_views.PackageList.as_view(),
        name='package_list'),
    path(
        '<int:id>/',
        package_views.PackageResume.as_view(),
        name='package_detail')
]

deliverable_urls = [
    path(
        '',
        deliverable_views.DeliverableResume.as_view(),
        name='deliverable_resume'),
    path(
        'deliverablelist/',
        deliverable_views.DeliverableList.as_view(),
        name='serviceList'),
    path(
        '<int:id>/',
        deliverable_views.DeliverableResume.as_view(),
        name='deliverable_detail')
]

urlpatterns = [
    path('deliverable/', include(deliverable_urls, namespace=None)),
    path('package/', include(package_urls, namespace=None)),
    path('service/', include(service_urls, namespace=None)),   
]

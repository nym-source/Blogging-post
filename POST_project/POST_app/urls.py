from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views

urlpatterns = [
    path('',views.listVIEW, name='list'),
    path('mypost',views.mypostSVIEW, name='mypost'),
    path('draft/',views.draftVIEW, name='draft'),
    path('post/',views.postVIEW, name='post'),
    path('details/<int:id>',views.detailsVIEW, name='details'),
    path('publish/<int:pk>', views.updateVIEW.as_view(), name='publish'),
    path('signup/',views.signup, name='signup'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
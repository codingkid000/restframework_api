from django.urls import path
from myapp.views import *

urlpatterns = [
    path('detail/', DetailTable.as_view(),name='detail'),
    path('update/<int:id>',DetailsUpdate.as_view(),name='DetailsUpdate'),
    path("delete/<int:id>",DetailsDelete.as_view(),name="delete"),
]

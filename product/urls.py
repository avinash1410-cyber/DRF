from django.urls import path
from .views import RetrieveProductView,CreateProductView,CreateListProductView,alt_view

urlpatterns = [
    # path('create/', CreateProductView.as_view(),name="CreateProductView"),
    # path('list/', CreateListProductView.as_view(),name="CreateListProductView"),
    # path('<int:pk>/', RetrieveProductView.as_view(),name="RetrieveProductView")

    path('', alt_view,name="RetrieveProductView"),
    path('<int:pk>/', alt_view,name="RetrieveProductView")
    ]

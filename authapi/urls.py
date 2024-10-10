from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from accounts.views import auth_router

api = NinjaAPI()

api.add_router("/auth/", auth_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]


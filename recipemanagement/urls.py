"""
URL configuration for recipemanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from recipe import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as rviews



router = DefaultRouter()
router.register('user', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('recipe.urls')),

    path('', include(router.urls)),

    path('api-token-auth/',rviews.obtain_auth_token),         # for login view url using token auth (this is a builtin url path and has a builtin view code ,add this pathname in browser)

    # path('user_logout',views.user_logout.as_view()),

]

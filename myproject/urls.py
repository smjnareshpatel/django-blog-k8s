"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.http import JsonResponse, HttpResponse  # ✅ FIXED
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def health_check(request):
    return JsonResponse({"status": "ok"})

def root_view(request):
    return HttpResponse("CI/CD working! New version deployed...")  # ✅ This now works

urlpatterns = [
    path('', root_view),
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
    path('health/', health_check),
]

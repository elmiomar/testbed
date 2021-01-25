from TestBed.urls import *
from django.views.generic import TemplateView

from APIRest.views import *

router = routers.DefaultRouter()
router.register(r'unit', UnitViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', TemplateView.as_view(template_name="index.html")),
]
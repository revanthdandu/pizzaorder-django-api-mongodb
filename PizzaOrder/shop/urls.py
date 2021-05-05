from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('pizza', views.PizzaViewSet, basename='pizza')
router.register('topping', views.ToppingViewSet, basename='topping')

urlpatterns = router.urls
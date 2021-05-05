from rest_framework.viewsets import ModelViewSet
from .serializers import PizzaSerializer, ToppingSerializer
from .models import Pizza, Topping
from django.db.models import Q
# Create your views here.

class ToppingViewSet(ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer

class PizzaViewSet(ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def get_queryset(self):
        query_set = self.queryset

        if self.request.GET.get("q", None):
            query = self.request.GET['q']
            q1 = Q(pizza_size=query)
            q2 = Q(pizza_type=query)
            return query_set.filter(q1 | q2)
        else:
            return query_set


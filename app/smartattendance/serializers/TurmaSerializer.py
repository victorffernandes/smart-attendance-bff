from rest_framework.serializers import ModelSerializer

from ..models import Turma

class Serializer(ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'
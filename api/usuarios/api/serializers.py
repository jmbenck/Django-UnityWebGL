from rest_framework import serializers
from usuarios.models import Cidade, Escola, Usuario


class CidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cidade
        fields = ('url', 'id', 'cidade')


class EscolaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Escola
        fields = ('url', 'id', 'escola')


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    cidade = CidadeSerializer()
    escola = EscolaSerializer()

    class Meta:
        model = Usuario
        fields = (
            'url', 'id', 'username', 'password', 'nome', 'idade', 'sexo', 'serie', 'escola', 'cidade', 'pontuacao')

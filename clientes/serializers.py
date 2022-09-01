from ast import Return

from rest_framework import serializers

from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError(
                {'cpf': "O número de CPF é inválido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError(
                {'nome': "Inserir nome válido! Incluir somente letras"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError(
                {'rg': "O RG deve ter 9 dígitos."})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError(
                {'celular': "O celular deve ter 11 dígitos."})
        return data


''' def validate_nome(self, nome):
        if nome.isspace() and not nome.isalpha():
            raise serializers.ValidationError("Inserir nome válido! Incluir somente letras")
        return nome
    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError("O RG deve ter 9 dígitos.")
        return rg
    def validate_celular(self, celular):
        if len(celular) < 11:
            raise serializers.ValidationError("O celular deve ter 11 dígitos.")
        return celular'''

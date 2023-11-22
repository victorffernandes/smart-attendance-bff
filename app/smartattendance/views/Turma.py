from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime, timezone

from ..models import Turma, Aluno_Turma, Chamada, Presenca, Usuario
from ..serializers import ChamadaSerializer, TurmaSerializer, UsuarioSerializer, PresencaSerializer
        

class ViewSet(GenericViewSet):
    
    serializer_class = ChamadaSerializer.Serializer
    queryset = Chamada.objects.all()
    
    @action(detail=False, methods=['GET'])
    def listar_chamada(self, request):
        usuario_id = request.query_params['user']
        turma_id = request.query_params['turma']

        turma = Turma.objects.get(id=turma_id)
        turmaSerialized = TurmaSerializer.Serializer(turma).data
        usuario = Usuario.objects.get(id=usuario_id)
        usuarioSerialized = UsuarioSerializer.Serializer(usuario).data
        resp = {}

        chamadas = Chamada.objects.filter(turma_id=turma)
        chamadasSerialized = ChamadaSerializer.Serializer(chamadas, many = True).data

        for chamada in chamadasSerialized:
            chamada['Aberta'] = False
            if datetime.fromisoformat(chamada['data_inicio'][:-1])  < datetime.now() and datetime.fromisoformat(chamada['data_fim'][:-1]) > datetime.now():
                chamada['Aberta'] = True
                
        if usuarioSerialized['usuario_tipo'] == 'A':
            presencas = Presenca.objects.filter(chamada_id__in=chamadas).filter(aluno_id=usuario)
            presencasSerialized = PresencaSerializer.Serializer(presencas, many = True).data

            #Melhorar esse algoritmo talvez
            for chamada in chamadasSerialized:
                for presenca in presencasSerialized:
                    if presenca['chamada_id'] == chamada['id']:
                        chamada['presenca'] = presenca['status']

        resp['chamadas'] = chamadasSerialized
        return Response(resp)

        


    @action(detail=False,methods=['PUT'])
    def iniciar_chamada(self, request):
        turma_id = request.data.get('turma_id')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        data_fim = request.data.get('data_fim')
        raio = request.data.get('raio')

        
        turma = Turma.objects.get(id=turma_id)
        # Cria uma nova chamada
        chamada = Chamada.objects.create(
            turma_id=turma,
            data_inicio=datetime.now(),
            data_fim=data_fim,
            latitude=latitude,
            longitude=longitude,
            raio=raio
        )
        
        chamada_serializer = ChamadaSerializer.Serializer(chamada).data
        # Filtra os alunos da turma
        alunos = Aluno_Turma.objects.filter(turma_id=turma_id)
        
        # Atualizar status de todos os alunos para "FALTA"
        for aluno in alunos:
            Presenca.objects.create(
                aluno_id = aluno.aluno_id,
                chamada_id = chamada,
                tempo_entrada = None,
                tempo_saida = None,
                status = "F",
                ultima_atualizacao = None,
            )

        return Response(chamada_serializer)
        
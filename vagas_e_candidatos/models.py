from django.db import models

AREA_CHOICES = [
    ('adm', 'Administração'),
    ('eng', 'Engenharia'),
    ('tec', 'Tecnologia da Informação'),
    ('edu', 'Educação'),
    ('jur', 'Direito'),
    ('med', 'Medicina'),
    ('enf', 'Enfermagem'),
    ('fin', 'Finanças'),
    ('mkt', 'Marketing'),
    ('com', 'Comércio'),
    ('arq', 'Arquitetura'),
    ('des', 'Design'),
    ('coms', 'Comunicação Social'),
    ('log', 'Logística'),
    ('rec', 'Recursos Humanos'),
    ('tur', 'Turismo'),
    ('agr', 'Agronomia'),
    ('vet', 'Medicina Veterinária'),
    ('art', 'Artes'),
    ('out', 'Outros'),
]

TIPO_CONTRATO_CHOICES = [
    ('clt', 'CLT (Efetivo)'),
    ('pj', 'Pessoa Jurídica (PJ)'),
    ('est', 'Estágio'),
    ('tra', 'Temporário'),
    ('fre', 'Freelancer'),
    ('apr', 'Aprendiz'),
    ('aut', 'Autônomo'),
    ('vol', 'Voluntário'),
    ('int', 'Intermitente'),
    ('out', 'Outros'),
]

class Vaga(models.Model):
    titulo = models.CharField(max_length=200)
    area = models.CharField(max_length=50, choices=AREA_CHOICES)
    tipo_contrato = models.CharField(max_length=50, choices=TIPO_CONTRATO_CHOICES)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

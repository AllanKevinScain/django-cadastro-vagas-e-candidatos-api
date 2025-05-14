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

GENERO_CHOICES = [
    ('mas', 'Masculino'),
    ('fem', 'Feminino'),
    ('ninf', 'Prefere não informar'),
]

ESCOLARIDADE_CHOICES = [
    ('nin', 'Nenhuma'),
    ('funi', 'Fundamental Incompleto'),
    ('fuc', 'Fundamental Completo'),
    ('mei', 'Médio Incompleto'),
    ('med', 'Médio Completo'),
    ('sui', 'Superior Incompleto'),
    ('sup', 'Superior Completo'),
    ('pos', 'Pós-graduação'),
    ('mes', 'Mestrado'),
    ('dou', 'Doutorado'),
]


class Vaga(models.Model):
    titulo = models.CharField(max_length=200)
    area = models.CharField(max_length=50, choices=AREA_CHOICES)
    tipo_contrato = models.CharField(
        max_length=50, choices=TIPO_CONTRATO_CHOICES)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo


class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=15)
    escolaridade = models.CharField(
        max_length=30, choices=ESCOLARIDADE_CHOICES)
    vaga = models.ForeignKey(
        Vaga, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome

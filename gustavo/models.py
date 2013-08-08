# SIGNALS
from django.db.models import signals
from utils.signals_comuns import slug_pre_save

signals.pre_save.connect(slug_pre_save, sender=Artigo)

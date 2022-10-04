from django.db import models


class Categorias(models.Model):
    decreto = models.CharField(db_column='Decreto', max_length=30, primary_key=True)  # Field name made lowercase.
    fecha_vig = models.DateTimeField(db_column='Fecha Vig')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    categoria = models.CharField(db_column='Categoria', max_length=3)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=6)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=200, blank=True, null=True)
 # Field name made lowercase.
    secuencia = models.DecimalField(db_column='Secuencia', max_digits=18, decimal_places=2)  # Field name made lowercase.
    jerarquia_relacionada = models.CharField(db_column='Jerarquia Relacionada', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ubicacion = models.DecimalField(db_column='Ubicacion', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    importe1 = models.DecimalField(db_column='Importe1', max_digits=18, decimal_places=2)  # Field name made lowercase.
    importe2 = models.DecimalField(db_column='Importe2', max_digits=18, decimal_places=2)  # Field name made lowercase.
    importe3 = models.DecimalField(db_column='Importe3', max_digits=18, decimal_places=2)  # Field name made lowercase.
    importe4 = models.DecimalField(db_column='Importe4', max_digits=18, decimal_places=2)  # Field name made lowercase.
    importe5 = models.DecimalField(db_column='Importe5', max_digits=18, decimal_places=2)  # Field name made lowercase.
    importe6 = models.DecimalField(db_column='Importe6', max_digits=18, decimal_places=2)  # Field name made lowercase.
    importe7 = models.DecimalField(db_column='Importe7', max_digits=18, decimal_places=2)  # Field name made lowercase.
    importe8 = models.DecimalField(db_column='Importe8', max_digits=18, decimal_places=2)  # Field name made lowercase.
    importe9 = models.DecimalField(db_column='Importe9', max_digits=18, decimal_places=2)  # Field name made lowercase.
    importe10 = models.DecimalField(db_column='Importe10', max_digits=18, decimal_places=2)  # Field name made lowercase.
    porc_asistencia = models.DecimalField(db_column='Porc. Asistencia', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escalanro = models.IntegerField(db_column='EscalaNro', blank=True, null=True)  # Field name made lowercase.
    horas = models.DecimalField(db_column='Horas', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    horasdetalle = models.CharField(db_column='HorasDetalle', max_length=60, blank=True, null=True)  
    #Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categorias'
# Create your models here.

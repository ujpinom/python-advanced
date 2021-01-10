class Time:

    def __init__(self,horas=0,minutos=0,segundos=0):
        self.hora=horas
        self.minutos=minutos
        self.segundos=segundos


    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self,hora):
        if( 0<= hora <24):
            self._hora=hora
        else:
            raise ValueError('La hora está por fuera del formato especificado')

    @property
    def minutos(self):
        return self._minutos

    @minutos.setter
    def minutos(self,minutos):
        if not (0<= minutos <60):
            raise ValueError('El valor para los minutos no es correcto.')
        self._minutos=minutos

    @property
    def segundos(self):
        return self._segundos

    @segundos.setter
    def segundos(self,segundos):
        if not(0<= segundos <60):
            raise ValueError('El valor para los segundos no es correcto')

        self._segundos=segundos


    def set_time(self,horas=0,minutos=0,segundos=0):
        self.hora=horas;self.minutos=minutos;self.segundos=segundos

    def __repr__(self):
        return (f'Time(Hora={self.hora},Minutos={self.minutos},Segundos={self.minutos})')

    def __str__(self):

        if self.hora in (0,12):
            hora=12
        else:
            hora=self.hora%12
        if self.hora>=12:
            estado='PM'
        else:
            estado='AM'

        return (f'{hora:0>2}:{self.minutos:0>2}:{self.segundos:0>2}  {estado}')
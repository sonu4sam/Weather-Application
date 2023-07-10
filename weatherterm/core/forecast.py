from datetime import date

from .forecast_type import ForecastType

class Forecast:
    def __init__(self,
                 current_temp, 
                 humidity, 
                 wind, 
                 high_temp,
                 low_temp,
                 description='',
                 forecast_date=None,
                 forecast_type=ForecastType.TODAY):
        self._current_temp = current_temp
        self._high_temp = high_temp
        self._low_temp = low_temp
        self._humidity = humidity
        self._wind = wind
        self._description = description
        self._forecast_type = forecast_type
        
        if forecast_date is None:
            self.forecast_date = date.today()
        else:
            self._forecast_date = forecast_date
            
    @property
    def forecast_date(self):
        return self._forecast_date
    
    @forecast_date.setter
    def forecast_date(self, forecast_date):
        self._forecast_date = forecast_date.strftime('%a %b %d')
        
    @property
    def current_temp(self):
        return self._current_temp
    
    @property
    def humidity(self):
        return self._humidity
    
    @property
    def wind(self):
        return self._wind
    
    @property
    def description(self):
        return self._description
    
    def __str__(self) -> str:
        tempature = None
        offset = ' ' * 4
        
        if self._forecast_type == ForecastType.TODAY:
            tempature = (f'{offset}{self.current_temp}\xb0\n'
                         f'{offset}High {self._high_temp}\xb0 / '
                         f'Low {self._low_temp}\xb0 ')
            
        else:
            tempature = (f'{offset}High {self._high_temp}\xb0 / '
                            f'Low {self._low_temp}\xb0 ')
            
        return (f'>> {self.forecast_date}\n'
                f'{tempature}'
                f'({self._description})\n'
                f'{offset}Wind: '
                f'{self._wind} / Humidity: {self._humidity}\n')
    
        
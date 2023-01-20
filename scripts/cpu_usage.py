#!/bin/python

# from requests import get
import psutil

print(''+'{:>3.0f}%'.format(psutil.cpu_percent(interval=1)))


## Code below to use it with Glances

# cpu = get('http://localhost:61208/api/3/cpu').json()['total']
# cpu_temp = get('http://localhost:61208/api/3/sensors').json()[6]['value']
# cpu = '{:>3.0f}'.format(cpu)
# cpu_temp = '{:>4.0f}'.format(cpu_temp)

# print('' + str(cpu) + '%  ' + ' ' + str(cpu_temp) + '°C')

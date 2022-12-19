#!/bin/python

# from requests import get
import psutil

ram_used = '{:>2.2f}'.format(psutil.virtual_memory().used/1073741824)
ram_total = '{:>2.2f}'.format(psutil.virtual_memory().total/1073741824)
ram_percent = '{:>.0f}'.format(psutil.virtual_memory().percent)

print('力 ' + ram_used + ' / ' + ram_total + ' GB (' + ram_percent + '%)')


## Code below to use it with Glances

# ram = get('http://localhost:61208/api/3/mem').json()
# ram_used = '{:>5.2f}'.format(ram['used']/1073741824)
# ram_total = '{:>5.2f}'.format(ram['total']/1073741824)
# ram_percent = '{:>.0f}'.format(ram['percent'])
# # print(ram_used, ram_total, ram_percent)

# print('力 ' + ram_used + ' / ' + ram_total + ' GB (' + ram_percent + '%)')

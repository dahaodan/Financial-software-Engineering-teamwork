vol = '1a'
if not vol.isdigit():
    print('1')
else:
   vol = int(vol)
   if vol % 100 != 0:
       print('2')
    
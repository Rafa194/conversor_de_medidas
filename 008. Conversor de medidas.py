metros = float(input('Digite uma distancia em metros:'))
km = metros * (10 ** -3)
hm = metros * (10 ** -2)
dam = metros / 10
dm = metros * 10
cm = metros * (10 ** -2)
mm = metros * (10 ** -3)

print('A medida de {}m corresponde a:'.format(metros) )
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))

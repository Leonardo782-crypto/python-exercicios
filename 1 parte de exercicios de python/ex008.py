medida=float(input('uma distancia em metros: '))
mm=medida *1000
cm=medida *100
dm=medida *10
dam=medida /10
hm=medida /100
km=medida /1000
print('a medida em {} corresponde a {}cm e {}mm e {}dm'.format(medida,cm,mm,dm))
print('a medida em {} corresponde a {}dam e {}hm e {}km'.format(medida,dam,hm,km))

largura=float(input('Largura da parede : '))
alt=float(input('Altura da parede: '))
área= largura * alt
print('Sua parede tem a dimensao de {}x{} e sua área é de {}m.'.format(largura,alt,área))
tinta=área / 2
print('Para pintar essa parede,você precisa de {} litros de tinta '.format(tinta))
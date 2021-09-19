#===================== [1] CREACION DE LOS DATOS ======================
# data
lanzamientos = [5, 2, 3, 4, 3, 6, 6, 2, 2, 4, 5, 1, 1, 2, 6, 4, 1, 6]

# diccionario donde registrar los datos (tabla de frecuencia)
mapa_lanzamientos = {}

#====================== [2] ESTADISTICA DE LOS DATOS ======================
# contabilizacion de los datos
for lanzamiento in lanzamientos:
	if lanzamiento in mapa_lanzamientos:
		mapa_lanzamientos[lanzamiento] += 1
	else:
		mapa_lanzamientos[lanzamiento] = 1

mapa_lanzamientos_sorted = sorted(mapa_lanzamientos)
grupos             = len(mapa_lanzamientos_sorted);

# salida por consola de los resultados
if True :
    for key in mapa_lanzamientos_sorted:
        print(f'{key}: {mapa_lanzamientos[key]}')


#====================== [3] CREACION DEL HISTOGRAMA ======================
# libreria para crear histogramas
import matplotlib.pyplot as plot
# libreria para guardar una imagen
from matplotlib import pyplot

plot.title('histograma')
#plt.hist(mos, bins=60, alpha=1, edgecolor = 'black',  linewidth=1)
plot.hist(x=lanzamientos, bins=grupos, color='#65A9DA',
 rwidth=1, edgecolor = 'black', linewidth=1)
plot.grid(True)
# guardar gráfico como imágen PNG.
pyplot.savefig("histograma.png")
# mostrar grafico
plot.show()


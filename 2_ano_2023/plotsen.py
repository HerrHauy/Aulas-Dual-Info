import numpy as np
import matplotlib.pyplot as plt

def plota_sen_lan(x0,xf,n):
    
    xpoints = np.linspace(x0,xf,n)
    ypoints = []
    
    for i in xpoints:
        ypoints.append(np.sin(i))
        
    plt.plot(xpoints,ypoints)
    plt.show()
    
    
x0 = float(input('Valor inicial do plot:'))
xf = float(input('Valor final do plot:'))
n = int(input('Número de pontos do plot:'))
plota_sen_lan(x0,xf,n)
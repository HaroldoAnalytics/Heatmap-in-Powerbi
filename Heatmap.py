import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

portao_1 = [251.7, 552.4]
portao_2 = [314.0, 579.0]
portao_3 = [381.1, 626.2]
portao_11 = [502.1, 187.2]
portao_12 = [3927, 2520]
coordenadas_portoes = np.array([portao_1, portao_2, portao_3, portao_11])
quantidade_pessoas = np.array([14000, 9000, 10760, 9000])

imagem_path = r'C:\Users\glauc\Downloads\Planta aeroporto.jpeg'
imagem = img.imread(imagem_path)

fig, ax = plt.subplots(figsize=(10, 10))

y, x = np.meshgrid(np.linspace(0, imagem.shape[1], 600), np.linspace(0, imagem.shape[0], 600))

z = np.zeros_like(x)
for i in range(len(coordenadas_portoes)):
    z += quantidade_pessoas[i] * np.exp(-((x - coordenadas_portoes[i][1]) ** 2 + (y - coordenadas_portoes[i][0]) ** 2) / 1400)

img_plot = ax.imshow(imagem, extent=[0, imagem.shape[1], 0, imagem.shape[0]])
heat = ax.imshow(z, extent=[0, imagem.shape[1], 0, imagem.shape[0]], alpha=0.4, cmap="hot_r")
cbar = plt.colorbar(heat, ax=ax, label='Quantidade de Pessoas')

plt.title('Mapa de Calor do Fluxo de Pessoas nos Portões do Aeroporto')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

def on_scroll(event):

    if event.button == 'up':
        ax.set_xlim(ax.get_xlim()[0] * 0.9, ax.get_xlim()[1] * 0.9)
        ax.set_ylim(ax.get_ylim()[0] * 0.9, ax.get_ylim()[1] * 0.9)

    elif event.button == 'down':
        ax.set_xlim(ax.get_xlim()[0] * 1.1, ax.get_xlim()[1] * 1.1)
        ax.set_ylim(ax.get_ylim()[0] * 1.1, ax.get_ylim()[1] * 1.1)
    plt.draw()

fig.canvas.mpl_connect('scroll_event', on_scroll)
plt.show()

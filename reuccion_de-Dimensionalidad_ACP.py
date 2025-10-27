# ----------------------------------------------------
# 1. IMPORTACIÓN DE LIBRERÍAS
# ----------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

# ----------------------------------------------------
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# ----------------------------------------------------
# Generamos datos sintéticos en 3D que tengan una clara dirección principal
# para que PCA pueda ser ilustrado de forma efectiva.
np.random.seed(42)  # Para reproducibilidad
mean = [0, 0, 0]
# Matriz de covarianza que define la forma alargada de la nube de puntos
cov = [[13, 12, -2], 
       [12, 13, -2], 
       [-2, -2, 2]]
X = np.random.multivariate_normal(mean, cov, 200)

# Aplicamos PCA para obtener los componentes
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X)

# ----------------------------------------------------
# CLASE AUXILIAR PARA FLECHAS 3D (Mejora Estética)
# ----------------------------------------------------
# Matplotlib por defecto no dibuja flechas 3D de alta calidad.
# Esta clase nos permite crear flechas vectoriales limpias.
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)

# ----------------------------------------------------
# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
# ----------------------------------------------------
def generar_grafico_pca():
    """
    Genera y configura la visualización del proceso de PCA.
    """
    # --- Configuración Estética Global ---
    plt.style.use('seaborn-v0_8-whitegrid') # Estilo base limpio
    plt.rcParams.update({
        'font.family': 'sans-serif',
        'font.sans-serif': 'Arial', # Fuente clara y profesional
        'axes.labelcolor': '#333333',
        'xtick.color': '#333333',
        'ytick.color': '#333333',
        'axes.titleweight': 'bold',
        'axes.titlesize': 14,
        'axes.labelsize': 12,
        'legend.fontsize': 11,
    })
    
    # Paleta de colores amigable con daltonismo (Azul, Naranja, Verde)
    color_principal = '#0072B2'
    color_secundario = '#D55E00'
    color_terciario = '#009E73'
    color_puntos = '#56B4E9'

    # --- Creación de la Figura y los Subplots (Axes) ---
    # Aspecto 16:9 ideal para presentaciones
    fig = plt.figure(figsize=(16, 9))
    gs = fig.add_gridspec(2, 3, height_ratios=[0.1, 0.9])

    # Título general de la figura
    fig.suptitle(
        'Proceso de Reducción de Dimensión con PCA', 
        fontsize=20, 
        fontweight='bold', 
        y=0.98
    )

    # --- Panel 1: Datos Originales en 3D y Componentes Principales ---
    ax1 = fig.add_subplot(gs[1, 0], projection='3d')
    ax1.set_title('1. Datos Originales y Componentes Principales')
    
    # Dibujar puntos de datos
    ax1.scatter(X[:, 0], X[:, 1], X[:, 2], c=color_puntos, alpha=0.7, s=30, label='Datos Originales')
    
    # Dibujar los componentes principales como flechas
    arrow_prop_dict = dict(mutation_scale=20, arrowstyle='-|>', color='k', shrinkA=0, shrinkB=0, linewidth=1.5)
    for i, (comp, var) in enumerate(zip(pca.components_, pca.explained_variance_)):
        # Multiplicamos por la raíz de la varianza para escalar la flecha
        v = comp * np.sqrt(var) * 3 
        arrow = Arrow3D(
            [pca.mean_[0], pca.mean_[0] + v[0]],
            [pca.mean_[1], pca.mean_[1] + v[1]],
            [pca.mean_[2], pca.mean_[2] + v[2]],
            **arrow_prop_dict
        )
        ax1.add_artist(arrow)
        ax1.text(pca.mean_[0] + v[0]*1.2, pca.mean_[1] + v[1]*1.2, pca.mean_[2] + v[2]*1.2, f'PC{i+1}', fontsize=11, fontweight='bold')

    ax1.set_xlabel('Variable 1'); ax1.set_ylabel('Variable 2'); ax1.set_zlabel('Variable 3')
    ax1.view_init(elev=20, azim=-50) # Ajustar ángulo de vista

    # --- Panel 2: Scree Plot (Varianza Explicada) ---
    ax2 = fig.add_subplot(gs[1, 1])
    ax2.set_title('2. Varianza Capturada por Componente')
    
    explained_variance_ratio = pca.explained_variance_ratio_
    component_labels = ['PC1', 'PC2', 'PC3']
    colors = [color_principal, color_secundario, color_terciario]
    
    bars = ax2.bar(component_labels, explained_variance_ratio, color=colors, alpha=0.9)
    ax2.set_ylabel('Porcentaje de Varianza Explicada')
    ax2.set_ylim(0, 1)
    
    # Añadir etiquetas de porcentaje sobre las barras
    for bar in bars:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 0.02, f'{yval:.1%}', ha='center', va='bottom')

    # Línea de corte para la reducción
    ax2.axhline(y=explained_variance_ratio[2], color='r', linestyle='--', linewidth=1.5, xmin=0.05, xmax=0.95)
    ax2.text(1.5, explained_variance_ratio[2] + 0.05, 'Componentes descartados (ruido)', color='r', ha='center')

    # --- Panel 3: Datos Proyectados en 2D ---
    ax3 = fig.add_subplot(gs[1, 2])
    ax3.set_title('3. Datos Proyectados en Subespacio 2D')
    
    ax3.scatter(X_pca[:, 0], X_pca[:, 1], c=color_puntos, alpha=0.7, s=30)
    ax3.set_xlabel('Componente Principal 1')
    ax3.set_ylabel('Componente Principal 2')
    ax3.set_aspect('equal', adjustable='box') # Asegura que los ejes tengan la misma escala

    # --- Ajustes Finales de Layout ---
    plt.tight_layout(rect=[0, 0.05, 1, 0.95]) # Ajustar para dar espacio al título y copyright

    return fig

# ----------------------------------------------------
# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
# ----------------------------------------------------
def agregar_copyright(fig):
    """
    Añade una marca de agua/copyright a la figura.
    """
    fig.text(
        0.99, 0.01, # Posición (esquina inferior derecha)
        '© Alejandro Quintero Ruiz. Generado con Python.',
        ha='right', 
        va='bottom', 
        fontsize=10,
        color='gray',
        alpha=0.8
    )

# ----------------------------------------------------
# 5. BLOQUE PRINCIPAL Y EXPORTACIÓN DEL ARCHIVO
# ----------------------------------------------------
if __name__ == '__main__':
    # Generar el gráfico
    figura_pca = generar_grafico_pca()

    # Añadir el copyright
    agregar_copyright(figura_pca)

    # Guardar la imagen en formatos de alta calidad
    # SVG es un formato vectorial, ideal para escalar sin perder calidad.
    # PDF también es vectorial y excelente para publicaciones.
    # PNG con alto DPI es una buena alternativa de raster.
    nombre_archivo_base = "visualizacion_pca"
    figura_pca.savefig(f'{nombre_archivo_base}.svg', format='svg', bbox_inches='tight')
    figura_pca.savefig(f'{nombre_archivo_base}.pdf', format='pdf', bbox_inches='tight')
    figura_pca.savefig(f'{nombre_archivo_base}.png', format='png', dpi=300, bbox_inches='tight')

    print(f"Gráficos guardados como '{nombre_archivo_base}.svg', '{nombre_archivo_base}.pdf' y '{nombre_archivo_base}.png'")
    
    # Opcional: mostrar el gráfico en pantalla
    plt.show()

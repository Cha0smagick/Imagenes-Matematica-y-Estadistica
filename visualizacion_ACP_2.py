# ----------------------------------------------------------------------------
# 1. IMPORTACIÓN DE LIBRERÍAS
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# ----------------------------------------------------------------------------
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# ----------------------------------------------------------------------------
# Semilla para reproducibilidad de los datos aleatorios
np.random.seed(42)

# Parámetros para generar datos 2D correlacionados
# Media de los datos (centro de la nube de puntos)
mean = [0, 0]
# Matriz de covarianza para crear una correlación positiva
# La covarianza de 0.8 entre x e y creará una elipse inclinada
cov = [[1, 0.8], 
       [0.8, 1]]
# Número de puntos de datos a generar
n_samples = 300

# Generación de los datos usando una distribución normal multivariada
X = np.random.multivariate_normal(mean, cov, n_samples)

# Aplicación del Análisis de Componentes Principales (PCA)
# n_components=2 para obtener los dos componentes principales de nuestros datos 2D
pca = PCA(n_components=2)
pca.fit(X)

# ----------------------------------------------------------------------------
# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
# ----------------------------------------------------------------------------
def generar_grafico_pca(X, pca_model):
    """
    Genera y personaliza un gráfico de alta calidad para visualizar PCA.
    
    Args:
        X (np.ndarray): Datos originales.
        pca_model (PCA): Modelo PCA ajustado a los datos.
    """
    # --- Configuración Estética Inicial ---
    # Usamos el estilo de seaborn para una base profesional y limpia
    sns.set_style("whitegrid")
    # Paleta de colores amigable con el daltonismo
    palette = sns.color_palette("colorblind", n_colors=3)
    
    # Creación de la figura y los ejes con una relación de aspecto 16:9
    fig, ax = plt.subplots(figsize=(12, 6.75))

    # --- Dibujo de los Datos y Componentes ---
    # Dibujar la nube de puntos de los datos originales
    ax.scatter(X[:, 0], X[:, 1], alpha=0.6, color=palette[0], label='Datos Originales (Correlacionados)')

    # Dibujar los componentes principales como vectores
    # Los componentes son vectores que indican la dirección de máxima varianza
    for i, (comp, var) in enumerate(zip(pca_model.components_, pca_model.explained_variance_)):
        # Multiplicamos el componente por la raíz de la varianza para escalar su longitud
        # de forma visualmente representativa
        v = comp * np.sqrt(var) * 3  # El factor 3 es para una mejor visualización
        
        # Dibujar el vector del componente principal
        ax.arrow(pca_model.mean_[0], pca_model.mean_[1], v[0], v[1],
                 head_width=0.1, head_length=0.2, width=0.02,
                 color=palette[i+1], ec='black', length_includes_head=True)
        
        # Anotación de texto para cada componente
        ax.text(pca_model.mean_[0] + v[0] * 1.2, pca_model.mean_[1] + v[1] * 1.2,
                f'PC{i+1}\n({var:.2f} varianza)',
                color=palette[i+1], fontsize=12, fontweight='bold', ha='center', va='center')

    # --- Ajustes Estéticos Finales ---
    # Título y etiquetas con tipografía profesional (sans-serif)
    ax.set_title('Visualización del Análisis de Componentes Principales (PCA)', fontsize=18, fontweight='bold', pad=20)
    ax.set_xlabel('Variable Original 1', fontsize=14)
    ax.set_ylabel('Variable Original 2', fontsize=14)
    
    # Ajustar límites y aspecto para centrar la vista
    ax.axis('equal')
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    
    # Leyenda
    ax.legend(loc='upper left', fontsize=12)
    
    # Mejorar la legibilidad de los ticks
    ax.tick_params(axis='both', which='major', labelsize=12)

    return fig, ax

# Llamada a la función para generar el gráfico
fig, ax = generar_grafico_pca(X, pca)

# ----------------------------------------------------------------------------
# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
# ----------------------------------------------------------------------------
# Añadir la marca de agua/copyright en la parte inferior derecha
fig.text(0.95, 0.01, '© Alejandro Quintero Ruiz. Generado con Python.', 
         ha='right', va='bottom', fontsize=10, color='gray', style='italic')

# Ajustar el layout para que el copyright no se solape con otros elementos
fig.tight_layout(rect=[0, 0.03, 1, 0.97])

# ----------------------------------------------------------------------------
# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
# ----------------------------------------------------------------------------
# Guardar la imagen en formato vectorial (SVG) y raster (PNG) de alta resolución
output_filename_svg = "visualizacion_pca.svg"
output_filename_pdf = "visualizacion_pca.pdf"
output_filename_png = "visualizacion_pca.png"

fig.savefig(output_filename_svg, format='svg', bbox_inches='tight')
fig.savefig(output_filename_pdf, format='pdf', bbox_inches='tight')
fig.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')

# Mostrar el gráfico (opcional, útil en entornos interactivos como Jupyter)
plt.show()

print(f"Gráfico guardado exitosamente en los siguientes formatos:")
print(f"- {output_filename_svg} (Vectorial, recomendado para PowerPoint)")
print(f"- {output_filename_pdf} (Vectorial)")
print(f"- {output_filename_png} (Alta resolución, 300 DPI)")

# ==============================================================================
# 1. IMPORTACIÓN DE LIBRERÍAS
# ==============================================================================
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from sklearn.datasets import make_swiss_roll
from sklearn.manifold import LocallyLinearEmbedding, TSNE
from sklearn.decomposition import PCA
from umap import UMAP # Requiere instalar 'umap-learn'

# ==============================================================================
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# ==============================================================================
# Generamos el conjunto de datos "Swiss Roll"
# n_samples: Número de puntos en el conjunto de datos.
# noise: Cantidad de ruido gaussiano añadido a los datos.
# random_state: Semilla para reproducibilidad.
X, color = make_swiss_roll(n_samples=1500, noise=0.1, random_state=42)

# Parámetros para los algoritmos de reducción de dimensionalidad
# Estos parámetros son cruciales para el resultado y se eligen comúnmente.
N_NEIGHBORS = 12  # Número de vecinos para LLE y UMAP
N_COMPONENTS = 2   # Dimensión de destino (2D)

# =============================================================================
# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
# ==============================================================================
def generar_grafico_comparativo():
    """
    Genera y estiliza una visualización comparativa de métodos de reducción
    de dimensionalidad.
    """
    # --- Configuración del Estilo y Figura ---
    plt.style.use('seaborn-v0_8-whitegrid') # Estilo profesional y limpio
    fig = plt.figure(figsize=(16, 9), constrained_layout=True)
    
    # Paleta de colores 'viridis': es perceptualmente uniforme y amigable
    # para personas con daltonismo.
    cmap = plt.cm.viridis

    # Título principal de la figura
    fig.suptitle(
        "Comparación de Métodos de Reducción de Dimensionalidad",
        fontsize=22,
        fontweight='bold',
        fontfamily='sans-serif'
    )

    # --- Creación de la cuadrícula para los subplots ---
    # Usamos GridSpec para un control más fino del layout.
    gs = gridspec.GridSpec(2, 3, figure=fig)
    ax0 = fig.add_subplot(gs[0, 0], projection='3d') # Gráfico 3D original
    ax1 = fig.add_subplot(gs[0, 1]) # PCA
    ax2 = fig.add_subplot(gs[1, 0]) # LLE
    ax3 = fig.add_subplot(gs[1, 1]) # t-SNE
    ax4 = fig.add_subplot(gs[1, 2]) # UMAP
    
    axes = [ax1, ax2, ax3, ax4]

    # --- Gráfico 1: Datos Originales en 3D ---
    ax0.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=cmap, s=20, alpha=0.8)
    ax0.set_title("1. Datos Originales (Rollo Suizo 3D)", fontsize=14, pad=10)
    ax0.set_xlabel("Eje X")
    ax0.set_ylabel("Eje Y")
    ax0.set_zlabel("Eje Z")
    ax0.view_init(elev=10, azim=-75) # Ajuste de la vista 3D para mejor perspectiva

    # --- Aplicación y visualización de los algoritmos ---
    
    # Método 1: PCA (Principal Component Analysis) - Lineal
    pca = PCA(n_components=N_COMPONENTS, random_state=42)
    X_pca = pca.fit_transform(X)
    ax1.scatter(X_pca[:, 0], X_pca[:, 1], c=color, cmap=cmap, s=20, alpha=0.8)
    ax1.set_title("2. PCA (Lineal)", fontsize=14)

    # Método 2: LLE (Locally Linear Embedding) - No Lineal
    lle = LocallyLinearEmbedding(n_neighbors=N_NEIGHBORS, n_components=N_COMPONENTS, method='modified', random_state=42)
    X_lle = lle.fit_transform(X)
    ax2.scatter(X_lle[:, 0], X_lle[:, 1], c=color, cmap=cmap, s=20, alpha=0.8)
    ax2.set_title("3. LLE (No Lineal)", fontsize=14)

    # Método 3: t-SNE (t-distributed Stochastic Neighbor Embedding) - No Lineal
    tsne = TSNE(n_components=N_COMPONENTS, perplexity=30, random_state=42, init='pca', learning_rate='auto')
    X_tsne = tsne.fit_transform(X)
    ax3.scatter(X_tsne[:, 0], X_tsne[:, 1], c=color, cmap=cmap, s=20, alpha=0.8)
    ax3.set_title("4. t-SNE (No Lineal)", fontsize=14)

    # Método 4: UMAP (Uniform Manifold Approximation and Projection) - No Lineal
    reducer_umap = UMAP(n_neighbors=N_NEIGHBORS, n_components=N_COMPONENTS, random_state=42)
    X_umap = reducer_umap.fit_transform(X)
    ax4.scatter(X_umap[:, 0], X_umap[:, 1], c=color, cmap=cmap, s=20, alpha=0.8)
    ax4.set_title("5. UMAP (No Lineal)", fontsize=14)

    # --- Ajustes Estéticos Finales para los subplots 2D ---
    for ax in axes:
        ax.set_xlabel("Componente 1")
        ax.set_ylabel("Componente 2")
        ax.set_xticks([]) # Ocultamos los ejes para centrar la atención en la forma
        ax.set_yticks([])
        ax.spines['top'].set_visible(False) # Limpiamos los bordes del gráfico
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(True)
        ax.spines['left'].set_visible(True)
        ax.set_aspect('equal', 'box') # Asegura que la escala sea la misma en ambos ejes

    return fig

# ==============================================================================
# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
# ==============================================================================
def agregar_copyright(fig):
    """
    Añade una marca de agua de copyright a la figura.
    """
    fig.text(
        0.99, 0.01, # Posición (esquina inferior derecha)
        "© Alejandro Quintero Ruiz. Generado con Python.",
        ha='right', # Alineación horizontal
        va='bottom', # Alineación vertical
        fontsize=10,
        color='gray',
        fontstyle='italic'
    )

# ==============================================================================
# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
# ==============================================================================
def guardar_grafico(fig, nombre_archivo="comparacion_reduccion_dimensionalidad"):
    """
    Guarda la figura en formatos de alta calidad.
    """
    # Guardar en formato SVG (Vectorial, ideal para escalabilidad y edición)
    ruta_svg = f"{nombre_archivo}.svg"
    fig.savefig(ruta_svg, format='svg', dpi=300, bbox_inches='tight')
    print(f"Gráfico guardado como: {ruta_svg}")

    # Guardar en formato PDF (Vectorial, excelente para publicaciones)
    ruta_pdf = f"{nombre_archivo}.pdf"
    fig.savefig(ruta_pdf, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Gráfico guardado como: {ruta_pdf}")
    
    # Guardar en formato PNG (Ráster de alta resolución, para compatibilidad)
    ruta_png = f"{nombre_archivo}.png"
    fig.savefig(ruta_png, format='png', dpi=300, bbox_inches='tight')
    print(f"Gráfico guardado como: {ruta_png}")


# --- Ejecución Principal ---
if __name__ == "__main__":
    # Generamos la figura base
    figura_generada = generar_grafico_comparativo()
    
    # Añadimos el copyright
    agregar_copyright(figura_generada)
    
    # Mostramos el gráfico (opcional, útil para desarrollo)
    plt.show()
    
    # Guardamos el gráfico en los formatos deseados
    guardar_grafico(figura_generada)

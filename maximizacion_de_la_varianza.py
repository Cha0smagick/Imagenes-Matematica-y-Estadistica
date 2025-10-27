# ----------------------------------------------------
# 1. IMPORTACIÓN DE LIBRERÍAS
# ----------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import MaxNLocator

# ----------------------------------------------------
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# ----------------------------------------------------
# Semilla para reproducibilidad de los datos
np.random.seed(42)

# Parámetros de la distribución de datos original
mean = [0, 0]
# Matriz de covarianza (S) que define la forma y orientación de los datos
# Una alta covarianza (0.9) creará una elipse alargada, ideal para PCA.
cov_matrix = [[1, 0.9], 
              [0.9, 1]]

# Generación de 200 puntos de datos en 2D siguiendo una distribución normal multivariada
X = np.random.multivariate_normal(mean, cov_matrix, 200)

# --- Cálculo de Componentes Principales ---
# 1. Centrar los datos (aunque ya están centrados por la media [0,0])
X_centered = X - np.mean(X, axis=0)

# 2. Calcular la matriz de covarianza empírica (debería ser cercana a la original)
S = np.cov(X_centered, rowvar=False)

# 3. Calcular autovalores y autovectores de la matriz de covarianza
# Los autovectores son los componentes principales.
# Los autovalores indican la varianza capturada por cada componente.
eigenvalues, eigenvectors = np.linalg.eig(S)

# Ordenar los componentes por su autovalor (de mayor a menor)
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
eigenvectors = eigenvectors[:, order]

# El primer componente principal (PC1) es el vector que maximiza la varianza
pc1 = eigenvectors[:, 0]
# El segundo componente principal (PC2)
pc2 = eigenvectors[:, 1]

# ----------------------------------------------------
# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
# ----------------------------------------------------
def create_pca_visualization():
    """
    Genera y estiliza el gráfico que visualiza el concepto de maximización
    de la varianza en PCA.
    """
    # --- Configuración del Estilo y Figura ---
    # Usar un estilo limpio y profesional
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # Crear figura con una proporción 16:9, ideal para PowerPoint
    fig, ax = plt.subplots(figsize=(12, 6.75))

    # Paleta de colores armónica y amigable con daltonismo
    color_data = '#4c72b0'      # Azul suave
    color_pc1 = '#dd8452'       # Naranja
    color_pc2 = '#55a868'       # Verde
    color_proj = '#c44e52'      # Rojo suave
    color_text = '#333333'      # Gris oscuro para texto

    # --- Dibujo de los Elementos del Gráfico ---
    # Scatter plot de los datos originales
    ax.scatter(X[:, 0], X[:, 1], alpha=0.6, color=color_data, label='Datos Originales (X)')

    # Dibujar los Componentes Principales como vectores desde la media
    # Se escalan por el autovalor para que su longitud represente la varianza
    scale_factor = 3
    arrow_pc1 = ax.arrow(0, 0, pc1[0] * scale_factor * np.sqrt(eigenvalues[0]), pc1[1] * scale_factor * np.sqrt(eigenvalues[0]),
                         head_width=0.2, head_length=0.3, fc=color_pc1, ec=color_pc1, lw=2.5,
                         label=f'PC1 (Varianza Máxima: {eigenvalues[0]:.2f})')
    
    arrow_pc2 = ax.arrow(0, 0, pc2[0] * scale_factor * np.sqrt(eigenvalues[1]), pc2[1] * scale_factor * np.sqrt(eigenvalues[1]),
                         head_width=0.2, head_length=0.3, fc=color_pc2, ec=color_pc2, lw=2.5,
                         label=f'PC2 (Varianza Mínima: {eigenvalues[1]:.2f})')

    # Proyección de los datos sobre los componentes principales
    # Esto crea las "sombras" o distribuciones 1D a lo largo de los ejes
    proj_on_pc1 = X_centered.dot(pc1).reshape(-1, 1) * pc1.reshape(1, -1)
    proj_on_pc2 = X_centered.dot(pc2).reshape(-1, 1) * pc2.reshape(1, -1)
    
    ax.scatter(proj_on_pc1[:, 0], proj_on_pc1[:, 1], alpha=0.2, color=color_pc1, s=50)
    ax.scatter(proj_on_pc2[:, 0], proj_on_pc2[:, 1], alpha=0.2, color=color_pc2, s=50)

    # --- Ajustes Estéticos y Etiquetas ---
    # Título y subtítulo para dar contexto
    fig.suptitle('La Base Matemática de PCA: Maximización de la Varianza', 
                 fontsize=18, fontweight='bold', ha='center', color=color_text, y=0.96)
    ax.set_title('El vector $w$ (PC1) se elige para maximizar la varianza de los datos proyectados ($w^T S w$)',
                 fontsize=12, color=color_text, pad=10)

    # Configuración de los ejes
    ax.set_xlabel('Variable 1', fontsize=12, color=color_text)
    ax.set_ylabel('Variable 2', fontsize=12, color=color_text)
    ax.set_aspect('equal', adjustable='box') # Ejes isométricos para una correcta visualización de ángulos
    
    # Limitar el número de ticks para un look más limpio
    ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=6))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=6))
    
    # Tipografía y color de los ticks
    ax.tick_params(axis='both', which='major', labelsize=10, colors=color_text)

    # Leyenda
    # Crear una leyenda personalizada para un mejor control
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', label='Datos Originales (X)',
                   markerfacecolor=color_data, markersize=8),
        arrow_pc1,
        arrow_pc2
    ]
    ax.legend(handles=legend_elements, loc='upper left', frameon=True, facecolor='white', framealpha=0.8, edgecolor='lightgray')

    # Eliminar spines innecesarios
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('lightgray')
    ax.spines['bottom'].set_color('lightgray')

    return fig, ax

# ----------------------------------------------------
# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
# ----------------------------------------------------
def add_copyright(fig):
    """Añade una marca de agua de copyright a la figura."""
    fig.text(0.98, 0.02, '© Alejandro Quintero Ruiz. Generado con Python.',
             fontsize=8, color='gray',
             ha='right', va='bottom', alpha=0.7)

# ----------------------------------------------------
# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
# ----------------------------------------------------
if __name__ == '__main__':
    # Generar el gráfico
    main_fig, main_ax = create_pca_visualization()

    # Añadir el copyright
    add_copyright(main_fig)

    # Ajustar el layout para evitar que los elementos se solapen
    main_fig.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajustar para dar espacio al título y copyright

    # Guardar la imagen en formatos de alta calidad
    # SVG es un formato vectorial ideal para escalabilidad y edición
    output_filename_svg = 'pca_maximization_of_variance.svg'
    main_fig.savefig(output_filename_svg, format='svg', bbox_inches='tight')

    # PDF es otra excelente opción vectorial para publicaciones
    output_filename_pdf = 'pca_maximization_of_variance.pdf'
    main_fig.savefig(output_filename_pdf, format='pdf', bbox_inches='tight')

    # PNG con alta resolución (DPI) como alternativa rasterizada
    output_filename_png = 'pca_maximization_of_variance.png'
    main_fig.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')

    print(f"Gráfico guardado en los siguientes formatos:\n- {output_filename_svg}\n- {output_filename_pdf}\n- {output_filename_png}")

    # Mostrar el gráfico (opcional)
    plt.show()


# 1. IMPORTACIÓN DE LIBRERÍAS
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# Escalar los datos antes de aplicar PCA
# PCA es sensible a la escala de las variables, por lo que estandarizamos
# para que cada característica tenga media 0 y desviación estándar 1.
X_scaled = StandardScaler().fit_transform(X)

# Aplicar PCA para reducir de 4 a 2 dimensiones
pca = PCA(n_components=2)
principal_components = pca.fit_transform(X_scaled)

# Crear un DataFrame de pandas con los componentes principales y las especies
# para facilitar la visualización con seaborn.
principal_df = pd.DataFrame(
    data=principal_components,
    columns=['Componente Principal 1', 'Componente Principal 2']
)
# Mapear los targets numéricos (0, 1, 2) a los nombres de las especies
species_labels = pd.Series(y).map({0: target_names[0], 1: target_names[1], 2: target_names[2]})
principal_df['Especie'] = species_labels

# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO

def generar_grafico_pca(df, pca_instance):
    """
    Genera y personaliza un gráfico de dispersión de los componentes principales.

    Args:
        df (pd.DataFrame): DataFrame con los componentes principales y las especies.
        pca_instance (PCA): Instancia de PCA ajustada para obtener la varianza explicada.
    """
    # --- Configuración de Estilo Profesional ---
    # Usamos un estilo limpio y profesional de seaborn
    sns.set_theme(style="whitegrid", context="talk")
    
    # Paleta de colores amigable con el daltonismo
    color_palette = sns.color_palette("colorblind", n_colors=3)

    # Crear la figura y los ejes con una proporción 16:9 para PowerPoint
    fig, ax = plt.subplots(figsize=(12, 6.75))

    # --- Creación del Gráfico Principal (Scatterplot) ---
    sns.scatterplot(
        x='Componente Principal 1',
        y='Componente Principal 2',
        hue='Especie',
        data=df,
        palette=color_palette,
        s=100,  # Tamaño de los puntos
        alpha=0.8, # Transparencia
        edgecolor='k', # Borde negro para los puntos
        linewidth=0.5,
        ax=ax
    )

    # --- Ajustes Estéticos, Etiquetas y Títulos ---
    # Obtener la varianza explicada por cada componente
    explained_variance = pca_instance.explained_variance_ratio_

    # Título y etiquetas de los ejes claros y descriptivos
    ax.set_title('Análisis de Componentes Principales (PCA) del Dataset Iris', fontsize=20, weight='bold', pad=20)
    ax.set_xlabel(f'Componente Principal 1 ({explained_variance[0]:.1%} de varianza)', fontsize=14)
    ax.set_ylabel(f'Componente Principal 2 ({explained_variance[1]:.1%} de varianza)', fontsize=14)

    # Personalizar la leyenda
    legend = ax.legend(title='Especie', frameon=True, facecolor='white', framealpha=0.8)
    legend.get_title().set_fontweight('bold')

    # Ajustar los ticks para mayor legibilidad
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    
    # Añadir una cuadrícula sutil
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # Eliminar los bordes superiores y derechos del gráfico para un look más limpio
    sns.despine(ax=ax, top=True, right=True)

    # 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
    # Añadir marca de agua/copyright de forma discreta
    fig.text(0.98, 0.02, '© Alejandro Quintero Ruiz. Generado con Python.',
             ha='right', va='bottom', fontsize=10, color='gray', style='italic')

    return fig, ax

# Generar el gráfico llamando a la función
fig, ax = generar_grafico_pca(principal_df, pca)

# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
# Guardar la imagen en formatos de alta calidad
# SVG: Formato vectorial, ideal para escalabilidad infinita
plt.savefig('pca_iris_visualization.svg', format='svg', bbox_inches='tight')
# PNG: Formato de raster, con alta resolución (DPI) para compatibilidad
plt.savefig('pca_iris_visualization.png', format='png', dpi=300, bbox_inches='tight')

# Mostrar el gráfico (opcional, útil en entornos interactivos como Jupyter)
plt.show()

print("Gráficos 'pca_iris_visualization.svg' y 'pca_iris_visualization.png' generados exitosamente.")


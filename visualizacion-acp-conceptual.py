# =============================================================================
# 1. IMPORTACIÓN DE LIBRERÍAS
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =============================================================================
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# =============================================================================
# Configuración para la reproducibilidad de los datos
np.random.seed(42)

# Parámetros de la distribución de datos 2D
# El centro de la nube de puntos
centro_datos = [0, 0]
# Matriz de covarianza que define la forma y orientación de la nube de puntos.
# La covarianza positiva (0.8) crea una correlación positiva,
# haciendo que la dirección del primer componente principal sea evidente.
matriz_covarianza = [[1.0, 0.8], 
                     [0.8, 1.0]]

# Generación de 300 puntos de datos siguiendo una distribución normal multivariada
datos = np.random.multivariate_normal(centro_datos, matriz_covarianza, 300)

# --- Cálculo de Componentes Principales ---
# a) Centrar los datos (restar la media)
datos_centrados = datos - np.mean(datos, axis=0)

# b) Calcular la matriz de covarianza empírica de los datos centrados
#    (S en la definición)
S = np.cov(datos_centrados, rowvar=False)

# c) Calcular los autovalores (lambda) y autovectores de la matriz de covarianza S
#    Los autovalores representan la varianza explicada por cada componente.
#    Los autovectores representan la dirección de los componentes.
autovalores, autovectores = np.linalg.eigh(S)

# d) Ordenar los autovalores y autovectores de mayor a menor
#    El primer componente principal corresponde al autovalor más grande.
orden = np.argsort(autovalores)[::-1]
autovalores_ordenados = autovalores[orden]
autovectores_ordenados = autovectores[:, orden]

# =============================================================================
# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
# =============================================================================
def generar_grafico_pca(datos, media, autovalores, autovectores):
    """
    Genera y personaliza un gráfico que visualiza los Componentes Principales.
    
    Args:
        datos (np.array): Nube de puntos de datos.
        media (np.array): El punto central de los datos.
        autovalores (np.array): Autovalores ordenados de la matriz de covarianza.
        autovectores (np.array): Autovectores ordenados correspondientes.
    """
    # --- Configuración Estética Inicial ---
    # Estilo profesional y limpio de seaborn
    sns.set_theme(style="whitegrid")
    
    # Paleta de colores armónica y amigable con el daltonismo
    # Azul para los datos, Naranja y Verde para los componentes
    color_datos = "#2A6EBB"
    color_cp1 = "#E67E22"
    color_cp2 = "#2ECC71"

    # Creación de la figura y los ejes con una proporción 16:9 para presentaciones
    fig, ax = plt.subplots(figsize=(12, 6.75))

    # --- Dibujo de los Elementos del Gráfico ---
    # a) Gráfico de dispersión de los datos
    ax.scatter(datos[:, 0], datos[:, 1], alpha=0.6, c=color_datos, label="Datos Originales")

    # b) Dibujo de los componentes principales como flechas (vectores)
    #    La longitud de la flecha se escala por la raíz cuadrada del autovalor
    #    (que es la desviación estándar) para una mejor visualización.
    for i in range(len(autovalores)):
        autovector = autovectores[:, i]
        autovalor = autovalores[i]
        
        # Escala para la flecha (multiplicador para visibilidad)
        escala_flecha = np.sqrt(autovalor) * 3
        
        color_flecha = color_cp1 if i == 0 else color_cp2
        
        # Anotación con flecha para representar el vector
        ax.annotate(
            '', xy=media + escala_flecha * autovector, xytext=media,
            arrowprops=dict(facecolor=color_flecha, shrink=0.05, width=2, headwidth=10, edgecolor='black', linewidth=0.5)
        )

    # --- Anotaciones y Etiquetas ---
    # Anotación para el Primer Componente Principal (CP1)
    ax.text(media[0] + autovectores[0, 0] * 4.5, 
            media[1] + autovectores[1, 0] * 4.5, 
            "CP1 (Dirección de máxima varianza)\nVector propio del mayor autovalor (\u03BB\u2081)",
            fontsize=12, color=color_cp1, weight='bold', ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=color_cp1, lw=1, alpha=0.9))

    # Anotación para el Segundo Componente Principal (CP2)
    ax.text(media[0] + autovectores[0, 1] * 2.5, 
            media[1] + autovectores[1, 1] * 2.5, 
            "CP2",
            fontsize=12, color=color_cp2, weight='bold', ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=color_cp2, lw=1, alpha=0.9))

    # --- Ajustes Finales de Estilo ---
    ax.set_title("Visualización Conceptual de Componentes Principales (PCA)", fontsize=18, weight='bold', pad=20)
    ax.set_xlabel("Variable 1", fontsize=14)
    ax.set_ylabel("Variable 2", fontsize=14)
    
    # Asegurar que la escala de los ejes sea la misma para no distorsionar la perpendicularidad
    ax.set_aspect('equal', adjustable='box')
    
    # Mejorar la legibilidad de las marcas de los ejes
    ax.tick_params(axis='both', which='major', labelsize=12)
    
    # Eliminar el borde superior y derecho para un look más limpio
    sns.despine()
    
    # Ajustar el layout para que no se corten los elementos
    plt.tight_layout(rect=[0, 0.05, 1, 1]) # Dejar espacio en la parte inferior para el copyright
    
    return fig, ax

# Llamada a la función para crear el gráfico
fig, ax = generar_grafico_pca(
    datos=datos,
    media=np.mean(datos, axis=0),
    autovalores=autovalores_ordenados,
    autovectores=autovectores_ordenados
)

# =============================================================================
# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
# =============================================================================
# Añadir la marca de agua/copyright en la parte inferior derecha de la figura
fig.text(0.98, 0.02, "© Alejandro Quintero Ruiz. Generado con Python.", 
         ha='right', va='bottom', fontsize=10, color='gray', style='italic')

# =============================================================================
# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
# =============================================================================
# Guardar la imagen en formato SVG (vectorial, ideal para PowerPoint y publicaciones)
# y en PNG de alta resolución como alternativa.
nombre_archivo_svg = "visualizacion_pca_conceptual.svg"
nombre_archivo_png = "visualizacion_pca_conceptual.png"

plt.savefig(nombre_archivo_svg, format='svg', bbox_inches='tight')
plt.savefig(nombre_archivo_png, format='png', dpi=300, bbox_inches='tight')

# Mostrar el gráfico en la consola/notebook (opcional)
plt.show()

print(f"Gráfico guardado exitosamente como '{nombre_archivo_svg}' y '{nombre_archivo_png}'.")

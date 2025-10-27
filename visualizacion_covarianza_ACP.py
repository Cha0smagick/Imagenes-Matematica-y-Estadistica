# 1. IMPORTACIÓN DE LIBRERÍAS
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS

# Generar datos sintéticos con una correlación específica
# Usaremos una distribución normal multivariada para tener control total.
np.random.seed(42)  # Para reproducibilidad
media = [0, 0]
# Matriz de covarianza:
# [[Var(X), Cov(X,Y)],
#  [Cov(Y,X), Var(Y)]]
# Alta covarianza positiva para que la relación sea visible.
matriz_cov_original = [[1.0, 0.8], 
                       [0.8, 1.0]]
# Generamos 200 puntos de datos de 2 dimensiones
X = np.random.multivariate_normal(media, matriz_cov_original, 200)

# Centrar los datos (un paso crucial en PCA)
X_centrado = X - np.mean(X, axis=0)

# Calcular la matriz de covarianza a partir de los datos (S o Σ)
# S = (X^T * X) / (n-1)
S = np.cov(X_centrado, rowvar=False)

# Calcular autovalores y autovectores (la esencia de PCA)
autovalores, autovectores = np.linalg.eig(S)

# Ordenar los autovectores por sus autovalores en orden descendente
orden = np.argsort(autovalores)[::-1]
autovalores_ordenados = autovalores[orden]
autovectores_ordenados = autovectores[:, orden]

# El primer autovector es el Componente Principal 1 (PC1)
# El segundo autovector es el Componente Principal 2 (PC2)
pc1 = autovectores_ordenados[:, 0]
pc2 = autovectores_ordenados[:, 1]


# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO

# --- Configuración del Estilo Profesional ---
plt.style.use('seaborn-v0_8-whitegrid') # Estilo limpio y profesional
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': 'Arial', # Fuente clara y aceptada
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'axes.titlesize': 16,
    'axes.titleweight': 'bold',
    'legend.fontsize': 11,
    'figure.dpi': 300 # Alta resolución por defecto
})

# --- Creación de la Figura y los Ejes ---
# Proporción 16:9 ideal para PowerPoint
fig, ax = plt.subplots(figsize=(12, 6.75))

# --- Dibujar los Datos ---
# Usamos un color suave y semitransparente para los puntos
ax.scatter(X_centrado[:, 0], X_centrado[:, 1], alpha=0.6, c='#3498db', label='Datos Centrados (X)')

# --- Dibujar los Componentes Principales (Autovectores) ---
# La longitud de la flecha se escala por la raíz del autovalor (desviación estándar)
# Esto muestra visualmente la magnitud de la varianza capturada por cada componente.
# El factor 2.5 es para una mejor visibilidad.
origen = np.mean(X_centrado, axis=0)

# Componente Principal 1
ax.quiver(*origen, *(pc1 * np.sqrt(autovalores_ordenados[0]) * 2.5),
          color='#e74c3c', scale=1, scale_units='xy', angles='xy',
          width=0.01, label=f'PC1 (Varianza: {autovalores_ordenados[0]:.2f})')

# Componente Principal 2
ax.quiver(*origen, *(pc2 * np.sqrt(autovalores_ordenados[1]) * 2.5),
          color='#f1c40f', scale=1, scale_units='xy', angles='xy',
          width=0.01, label=f'PC2 (Varianza: {autovalores_ordenados[1]:.2f})')

# --- Anotaciones y Etiquetas ---
ax.set_title('Visualización de PCA y la Matriz de Covarianza')
ax.set_xlabel('Variable 1')
ax.set_ylabel('Variable 2')
ax.legend(loc='upper left', frameon=True, shadow=True)

# Asegurar que los ejes tengan la misma escala para una correcta visualización de los vectores
ax.set_aspect('equal', adjustable='box')

# --- Anotación de la Matriz de Covarianza ---
# Crear un cuadro de texto para mostrar la matriz de forma clara
# La diagonal contiene las varianzas; los otros elementos, la covarianza.
texto_matriz = (
    f"Matriz de Covarianza (S):\n"
    f"[[ Var(V1) , Cov(V1,V2) ]]\n"
    f"[[ Cov(V2,V1),  Var(V2)  ]]\n\n"
    f"S = [[{S[0,0]:.2f}, {S[0,1]:.2f}],\n"
    f"     [{S[1,0]:.2f}, {S[1,1]:.2f}]]"
)

# Propiedades de la caja de texto
props = dict(boxstyle='round,pad=0.5', facecolor='aliceblue', alpha=0.9)

# Colocar la caja de texto en una posición estratégica
ax.text(0.95, 0.05, texto_matriz, transform=ax.transAxes, fontsize=10,
        verticalalignment='bottom', horizontalalignment='right', bbox=props,
        fontname='monospace') # Monospace para alinear los números

# Ajustar el layout para que no se corten los elementos
plt.tight_layout(rect=[0, 0.05, 1, 1]) # Dejar espacio en la parte inferior para el copyright

# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
copyright_text = "© Alejandro Quintero Ruiz. Generado con Python."
fig.text(0.5, 0.01, copyright_text, ha='center', va='bottom', fontsize=8, color='gray')


# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
# Guardamos en formato SVG (vectorial, escalable) y PNG (alta resolución)
nombre_archivo_base = "pca_covariance_visualization"
plt.savefig(f'{nombre_archivo_base}.svg', format='svg', bbox_inches='tight')
plt.savefig(f'{nombre_archivo_base}.pdf', format='pdf', bbox_inches='tight')
plt.savefig(f'{nombre_archivo_base}.png', format='png', dpi=300, bbox_inches='tight')

print(f"Gráficos guardados como '{nombre_archivo_base}.svg', '{nombre_archivo_base}.pdf' y '{nombre_archivo_base}.png'")

# Mostrar el gráfico (opcional, útil en entornos interactivos)
plt.show()

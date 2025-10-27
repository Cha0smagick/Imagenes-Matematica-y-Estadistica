import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def generate_pca_visualization(output_filename_svg="pca_visualization.svg", 
                               output_filename_png="pca_visualization.png", 
                               dpi=300):
    """
    Genera una visualización de alta calidad del Análisis de Componentes Principales (PCA)
    con datos sintéticos, optimizada para presentaciones y publicaciones científicas.

    Parámetros:
    - output_filename_svg (str): Nombre del archivo para guardar la imagen en formato SVG.
    - output_filename_png (str): Nombre del archivo para guardar la imagen en formato PNG.
    - dpi (int): Resolución en DPI para la imagen PNG.
    """

    # --- 1. Definición de Datos/Parámetros Matemáticos ---
    # Generar datos sintéticos 2D con una correlación clara
    np.random.seed(42) # Para reproducibilidad
    mean = [0, 0]
    cov = [[10, 8], [8, 10]] # Matriz de covarianza para crear una correlación
    X = np.random.multivariate_normal(mean, cov, 200)

    # Escalar los datos para que la PCA sea más robusta (aunque en este caso 
    # con datos centrados en 0 no es estrictamente necesario para la dirección,
    # es una buena práctica general).
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Aplicar PCA
    pca = PCA(n_components=2) # Calculamos 2 componentes para visualizarlos
    pca.fit(X_scaled)

    # Obtener los componentes principales (eigenvectores) y la varianza explicada (eigenvalores)
    components = pca.components_
    explained_variance = pca.explained_variance_

    # Proyectar los datos sobre el primer componente principal
    X_pca_projected = pca.transform(X_scaled)[:, 0] # Solo la primera componente
    # Para visualizar la proyección en el espacio original, necesitamos "deshacer" la proyección
    # Esto es, proyectar los datos de 1D de vuelta al espacio 2D a lo largo del PC1
    X_reconstructed = pca.inverse_transform(pca.transform(X_scaled))


    # --- 2. Configuración Estética y Generación del Gráfico ---
    # Configuración global de Matplotlib para un estilo profesional
    plt.style.use('seaborn-v0_8-whitegrid') # Un estilo limpio con rejilla
    sns.set_palette("viridis") # Paleta de colores amigable con el daltonismo

    # Configuración de fuentes (ej. 'DejaVu Sans' es común y sans-serif)
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['legend.fontsize'] = 10
    plt.rcParams['figure.titleweight'] = 'bold' # Título en negrita

    # Crear la figura y los ejes con un tamaño adecuado para PowerPoint (16:9)
    fig, ax = plt.subplots(figsize=(12, 6.75)) # 16:9 aspect ratio (e.g., 12x6.75, 16x9)

    # Título del gráfico
    ax.set_title('Análisis de Componentes Principales (PCA): Reducción de Dimensionalidad', pad=20)

    # Plotear los datos originales escalados
    ax.scatter(X_scaled[:, 0], X_scaled[:, 1], alpha=0.6, s=50, label='Datos Originales (Escalados)', zorder=2)

    # Plotear el centro de los datos
    ax.scatter(0, 0, color='red', marker='X', s=150, label='Centro de los Datos', zorder=3)

    # Plotear los componentes principales como vectores
    # Escalar los vectores para que sean visibles y representativos de la varianza
    for i, (component, variance) in enumerate(zip(components, explained_variance)):
        # Multiplicar por la raíz cuadrada de la varianza explicada para mostrar la "fuerza" del componente
        # O simplemente por un factor fijo para visualización clara
        scale_factor = 3 * np.sqrt(variance) # Ajustar este factor según sea necesario
        
        # Dibujar el vector desde el origen (centro de los datos escalados)
        ax.quiver(0, 0, component[0] * scale_factor, component[1] * scale_factor, 
                  angles='xy', scale_units='xy', scale=1, color=sns.color_palette("viridis")[i+2], 
                  width=0.008, headwidth=5, headlength=8, headaxislength=7, 
                  label=f'Componente Principal {i+1} (Var. Explicada: {variance:.2f})', zorder=4)
        
        # Añadir anotación para el componente principal
        ax.text(component[0] * scale_factor * 1.1, component[1] * scale_factor * 1.1, 
                f'PC{i+1}', color=sns.color_palette("viridis")[i+2], 
                fontsize=11, fontweight='bold', ha='center', va='center')

    # Plotear la proyección de los datos sobre el primer componente principal
    # Esto se visualiza como puntos en la línea del PC1
    ax.scatter(X_reconstructed[:, 0], X_reconstructed[:, 1], 
               color='orange', alpha=0.7, s=30, label='Datos Proyectados en PC1', zorder=3)
    
    # Dibujar la línea del primer componente principal
    # Usamos los límites del gráfico para extender la línea
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    
    # Calcular puntos en la línea del PC1 para dibujarla
    # La línea pasa por el origen (0,0) y tiene la dirección del PC1
    line_x = np.array([x_min, x_max])
    line_y = (components[0][1] / components[0][0]) * line_x if components[0][0] != 0 else np.zeros_like(line_x)
    
    # Asegurarse de que la línea se extienda a través de los datos
    ax.plot(line_x, line_y, color=sns.color_palette("viridis")[2], linestyle='--', linewidth=1.5, 
            label='Línea del Primer Componente Principal', zorder=1)


    # Etiquetas de los ejes
    ax.set_xlabel('Característica 1 (Escalada)')
    ax.set_ylabel('Característica 2 (Escalada)')

    # Añadir una leyenda
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0.) # Fuera del gráfico para no obstruir

    # Ajustar límites para asegurar que todo sea visible
    ax.set_xlim(X_scaled[:, 0].min() - 1, X_scaled[:, 0].max() + 1)
    ax.set_ylim(X_scaled[:, 1].min() - 1, X_scaled[:, 1].max() + 1)
    ax.set_aspect('equal', adjustable='box') # Mantener la proporción para una visualización correcta de los vectores

    # Añadir anotaciones explicativas
    ax.text(0.02, 0.98, 
            "PCA reduce la dimensionalidad proyectando los datos\n"
            "en un subespacio de menor dimensión (ej. PC1).", 
            transform=ax.transAxes, fontsize=10, verticalalignment='top', 
            bbox=dict(boxstyle="round,pad=0.5", fc="white", ec="lightgray", lw=0.5, alpha=0.8))

    # --- 3. Bloque de Adición del Copyright ---
    fig.text(0.99, 0.01, '© Alejandro Quintero Ruiz. Generado con Python.', 
             ha='right', va='bottom', fontsize=8, color='gray', alpha=0.7)

    # Ajustar el layout para que la leyenda no se superponga
    plt.tight_layout(rect=[0, 0.03, 0.85, 0.95]) # Ajusta el área de trazado para dejar espacio a la leyenda y copyright

    # --- 4. Bloque de Guardado/Exportación del Archivo ---
    # Guardar como SVG (vectorial)
    plt.savefig(output_filename_svg, format='svg', bbox_inches='tight')
    print(f"Gráfico guardado como {output_filename_svg}")

    # Guardar como PNG de alta resolución
    plt.savefig(output_filename_png, format='png', dpi=dpi, bbox_inches='tight')
    print(f"Gráfico guardado como {output_filename_png}")

    plt.show() # Mostrar el gráfico

# Ejecutar la función para generar la visualización
if __name__ == "__main__":
    generate_pca_visualization()

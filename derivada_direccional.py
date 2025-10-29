# d:\0. Universidad Iberoamericana\10. fundamentos estadisticos y matematicos para la IA\Graficas\script-graficas.py

# =============================================================================
# 1. IMPORTACIÓN DE LIBRERÍAS
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

# =============================================================================
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# =============================================================================
# Definimos una función escalar f(x, y) para visualizar.
# Usaremos un paraboloide elíptico para que las curvas de nivel sean claras.
def f(x, y):
    return (x - 1)**2 + 2 * (y - 1)**2

# Definimos la función del gradiente de f(x, y).
# ∇f = [∂f/∂x, ∂f/∂y] = [2(x-1), 4(y-1)]
def grad_f(x, y):
    return np.array([2 * (x - 1), 4 * (y - 1)])

# Punto de interés P donde evaluaremos el gradiente y las direcciones.
P = np.array([2.5, 2.0])

# Calculamos el vector gradiente en el punto P.
grad_P_actual = grad_f(P[0], P[1])

# Para visualización, escalamos el gradiente a una longitud razonable.
# Esto es crucial para que los vectores y sus etiquetas no se salgan de los límites del gráfico.
display_vector_length = 1.0
grad_P_display = grad_P_actual / np.linalg.norm(grad_P_actual) * display_vector_length

# Vector de dirección arbitrario v.
v = np.array([-2.0, 1.5])
# Normalizamos v para que su longitud no domine el gráfico.
v_norm = v / np.linalg.norm(v)
v_display = v_norm * display_vector_length # Escalar para display

# Calculamos el ángulo θ entre el gradiente y el vector v.
cos_theta = np.dot(grad_P_actual, v_norm) / (np.linalg.norm(grad_P_actual) * np.linalg.norm(v_norm))
theta_rad = np.arccos(np.clip(cos_theta, -1.0, 1.0))
theta_deg = np.degrees(theta_rad)

# =============================================================================
# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
# =============================================================================
def generar_grafico_derivada_direccional():
    """
    Genera y personaliza el gráfico de la derivada direccional.
    """
    # --- Configuración Estética Inicial ---
    plt.style.use('seaborn-v0_8-whitegrid') # Estilo profesional y limpio.    # Aumentamos el ancho de la figura para dejar espacio para la leyenda externa.
    fig = plt.figure(figsize=(15, 6.75)) # Aspect ratio modificado para PowerPoint + leyenda.
    ax = fig.add_subplot(111)

    # --- Creación de las Curvas de Nivel ---
    x_range = np.linspace(-1, 4, 200)
    y_range = np.linspace(-1, 4, 200)
    X, Y = np.meshgrid(x_range, y_range)
    Z = f(X, Y)
    
    # Paleta de colores amigable con el daltonismo (Viridis)
    # Reducimos el número de niveles y aumentamos el tamaño de fuente para clabel
    contour = ax.contour(X, Y, Z, levels=10, cmap='viridis', alpha=0.7) # Menos niveles para menos solapamiento
    ax.clabel(contour, inline=True, fontsize=10, fmt='%1.1f') # Fuente más grande

    # --- Dibujo de Vectores ---
    arrow_props = dict(facecolor='black', width=0.05, head_width=0.3, head_length=0.4)
    text_offset_multiplier = 1.1 # Multiplicador para la posición del texto respecto al final del vector
    
    # Vector Gradiente (Máximo Ascenso)
    ax.arrow(P[0], P[1], grad_P_display[0], grad_P_display[1], **arrow_props, color='#d62728') # Rojo
    ax.text(P[0] + grad_P_display[0] * text_offset_multiplier, 
            P[1] + grad_P_display[1] * text_offset_multiplier, 
            "∇f(P)", 
            fontsize=14, weight='bold', color='#d62728', ha='left', va='bottom') # Ajuste de alineación

    # Vector de Máximo Descenso
    ax.arrow(P[0], P[1], -grad_P_display[0], -grad_P_display[1], **arrow_props, color='#1f77b4') # Azul
    ax.text(P[0] - grad_P_display[0] * text_offset_multiplier, 
            P[1] - grad_P_display[1] * text_offset_multiplier, 
            "-∇f(P)", 
            fontsize=14, weight='bold', color='#1f77b4', ha='right', va='top') # Ajuste de alineación

    # Vector de Dirección v
    ax.arrow(P[0], P[1], v_display[0], v_display[1], **arrow_props, color='#2ca02c') # Verde
    ax.text(P[0] + v_display[0] * text_offset_multiplier, 
            P[1] + v_display[1] * text_offset_multiplier, 
            "v", 
            fontsize=14, weight='bold', color='#2ca02c', ha='right', va='bottom') # Ajuste de alineación

    # --- Anotaciones y Puntos ---
    # Punto P
    ax.plot(P[0], P[1], 'ko', markersize=10, label='Punto P')
    ax.text(P[0] + 0.1, P[1] - 0.2, "P", fontsize=14, weight='bold', color='black', ha='left', va='top')

    # Ángulo θ
    angle_start_rad = np.arctan2(grad_P_display[1], grad_P_display[0])
    # Asegurarse de que el ángulo de inicio y fin estén en el rango correcto para Arc
    # y que theta2 sea mayor que theta1 para dibujar el arco correctamente.
    theta1_arc = np.degrees(angle_start_rad)
    theta2_arc = np.degrees(angle_start_rad + theta_rad)

    # Ajustar el radio del arco para que no colisione con las etiquetas de los vectores
    arc_radius = 0.5
    arc = Arc(P, arc_radius, arc_radius, angle=0, theta1=theta1_arc, theta2=theta2_arc,
              color='purple', linewidth=1.5, linestyle='--')
    ax.add_patch(arc)
    
    # Posición del texto 'θ' a mitad del arco
    angle_text_pos_rad = angle_start_rad + theta_rad / 2
    ax.text(P[0] + arc_radius * 0.6 * np.cos(angle_text_pos_rad), # 0.6 para que esté dentro del arco
            P[1] + arc_radius * 0.6 * np.sin(angle_text_pos_rad), 
            "θ",
            fontsize=16, color='purple', ha='center', va='center')

    # --- Ajustes Finales del Gráfico ---
    ax.set_aspect('equal', adjustable='box')    # Ajustar límites para asegurar que todos los elementos sean visibles
    # Se han hecho más generosos para acomodar los vectores y etiquetas escaladas.
    ax.set_xlim(min(x_range) - 0.5, max(x_range) + 0.5)
    ax.set_ylim(min(y_range) - 0.5, max(y_range) + 0.5)
    
    # Títulos y Etiquetas con tipografía profesional
    font_opts = {'family': 'sans-serif', 'fontname': 'Arial'}
    # Usamos fig.suptitle para el título principal, liberando espacio en el eje.
    fig.suptitle("Visualización de la Derivada Direccional", fontsize=18, weight='bold', **font_opts)
    ax.set_xlabel("Eje X", fontsize=12, **font_opts)
    ax.set_ylabel("Eje Y", fontsize=12, **font_opts)

    # Creación de una leyenda descriptiva
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color='#d62728', lw=4, label='∇f(P): Dirección de máximo ascenso'),
        Line2D([0], [0], color='#1f77b4', lw=4, label='-∇f(P): Dirección de máximo descenso'),
        Line2D([0], [0], color='#2ca02c', lw=4, label='v: Dirección arbitraria'),
        Line2D([0], [0], marker='o', color='w', label='P: Punto de evaluación',
               markerfacecolor='k', markersize=10)
    ]
    # Colocamos la leyenda fuera del área del gráfico para evitar colisiones.
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=11)
    
    return fig, ax

# =============================================================================
# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
# =============================================================================
def agregar_copyright(fig):
    """
    Añade una marca de agua/copyright a la figura.
    """
    fig.text(0.98, 0.02, "© Alejandro Quintero Ruiz. Generado con Python.", 
             ha='right', va='bottom', fontsize=10, color='gray', style='italic')

# =============================================================================
# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
# =============================================================================
if __name__ == "__main__":
    # Generar el gráfico
    figura, eje = generar_grafico_derivada_direccional()
    
    # Agregar el copyright
    agregar_copyright(figura)
    
    # Ajustar el layout para que no se corten los elementos
    # rect ajustado para dejar espacio para el suptitle y la leyenda externa.
    figura.tight_layout(rect=[0, 0.03, 0.9, 0.95]) # [left, bottom, right, top]
    
    # Guardar la imagen en formatos de alta calidad
    # Formato SVG (Vectorial, ideal para escalabilidad y edición)
    ruta_svg = "derivada_direccional.svg"
    figura.savefig(ruta_svg, format='svg', dpi=300, bbox_inches='tight')
    
    # Formato PDF (Vectorial, excelente para documentos)
    ruta_pdf = "derivada_direccional.pdf"
    figura.savefig(ruta_pdf, format='pdf', dpi=300, bbox_inches='tight')    # bbox_inches='tight' es crucial para asegurar que todos los elementos (incluida la leyenda externa)
    # se incluyan en la imagen final sin ser recortados.


    # Formato PNG (Rasterizado de alta resolución, para compatibilidad)
    ruta_png = "derivada_direccional.png"
    figura.savefig(ruta_png, format='png', dpi=300, bbox_inches='tight')
    
    print(f"Gráfico guardado exitosamente en los siguientes formatos:")
    print(f"- SVG: {ruta_svg}")
    print(f"- PDF: {ruta_pdf}")
    print(f"- PNG: {ruta_png}")
    
    # Mostrar el gráfico (opcional)
    plt.show()

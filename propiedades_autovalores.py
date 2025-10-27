# 1. Importación de Librerías
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# --- Configuración de Estilo Profesional ---
# Usamos un estilo limpio y una fuente sans-serif profesional como 'Arial' o 'Helvetica'.
# Si no están disponibles, Matplotlib usará una alternativa predeterminada.
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 12,
    'figure.titlesize': 20,
    'axes.titlepad': 20,
    'axes.labelpad': 15,
})

# 2. Definición de Datos/Parámetros Matemáticos

# Matriz A: Definida Positiva
A = np.array([[2, -1], 
              [-1, 2]])
eigvals_A, eigvecs_A = np.linalg.eig(A)
det_A = np.linalg.det(A)
prod_eigvals_A = np.prod(eigvals_A)

# Matriz B: Indefinida (no es definida positiva)
B = np.array([[1, 2], 
              [2, 1]])
eigvals_B, eigvecs_B = np.linalg.eig(B)
det_B = np.linalg.det(B)
prod_eigvals_B = np.prod(eigvals_B)

# 3. Función o Bloque de Generación del Gráfico

def create_eigenvalue_visualization():
    """
    Genera y configura el gráfico completo para visualizar las propiedades de los autovalores.
    """
    # Crear una figura con una relación de aspecto 16:9 para PowerPoint
    fig = plt.figure(figsize=(16, 9))
    
    # Usar GridSpec para un diseño complejo y organizado
    gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.4, wspace=0.3)
    
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[1, 0], projection='3d')
    ax4 = fig.add_subplot(gs[1, 1], projection='3d')
    
    # --- Colores Armónicos (considerando daltonismo) ---
    color_positive = '#1f77b4'  # Azul
    color_negative = '#d62728'  # Rojo
    color_surface_A = 'viridis'
    color_surface_B = 'cividis'

    # --- Subgráfico 1: Autovalores de la Matriz A (Definida Positiva) ---
    ax1.set_title('Caso 1: Matriz Definida Positiva', fontweight='bold')
    ax1.axhline(0, color='gray', linewidth=0.8, linestyle='--')
    ax1.plot(eigvals_A, [0, 0], 'o', markersize=12, color=color_positive, label='Autovalores > 0')
    ax1.set_xlim(-2, 4)
    ax1.set_ylim(-1, 1)
    ax1.set_yticks([])
    ax1.set_xlabel('Valor del Autovalor')
    ax1.spines['left'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.xaxis.set_ticks_position('bottom')
    ax1.legend(loc='upper right')
    
    # Anotaciones para Matriz A
    matrix_str_A = f"Matriz A:\n[[{A[0,0]}, {A[0,1]}],\n [{A[1,0]}, {A[1,1]}]]"
    det_str_A = f"det(A) = {det_A:.2f}"
    prod_str_A = f"λ₁ × λ₂ = {eigvals_A[0]:.2f} × {eigvals_A[1]:.2f} = {prod_eigvals_A:.2f}"
    ax1.text(-1.8, 0.7, matrix_str_A, va='top', fontsize=11, bbox=dict(boxstyle='round,pad=0.5', fc='aliceblue', ec='lightsteelblue'))
    ax1.text(-1.8, 0.2, f"{det_str_A}\n{prod_str_A}", va='top', fontsize=11)

    # --- Subgráfico 2: Autovalores de la Matriz B (Indefinida) ---
    ax2.set_title('Caso 2: Matriz Indefinida', fontweight='bold')
    ax2.axhline(0, color='gray', linewidth=0.8, linestyle='--')
    ax2.plot([eigvals_B[0]], [0], 'o', markersize=12, color=color_positive, label='Autovalor > 0')
    ax2.plot([eigvals_B[1]], [0], 'o', markersize=12, color=color_negative, label='Autovalor < 0')
    ax2.set_xlim(-2, 4)
    ax2.set_ylim(-1, 1)
    ax2.set_yticks([])
    ax2.set_xlabel('Valor del Autovalor')
    ax2.spines['left'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax2.xaxis.set_ticks_position('bottom')
    ax2.legend(loc='upper right')

    # Anotaciones para Matriz B
    matrix_str_B = f"Matriz B:\n[[{B[0,0]}, {B[0,1]}],\n [{B[1,0]}, {B[1,1]}]]"
    det_str_B = f"det(B) = {det_B:.2f}"
    prod_str_B = f"λ₁ × λ₂ = {eigvals_B[0]:.2f} × {eigvals_B[1]:.2f} = {prod_eigvals_B:.2f}"
    ax2.text(-1.8, 0.7, matrix_str_B, va='top', fontsize=11, bbox=dict(boxstyle='round,pad=0.5', fc='seashell', ec='sandybrown'))
    ax2.text(-1.8, 0.2, f"{det_str_B}\n{prod_str_B}", va='top', fontsize=11)

    # --- Subgráfico 3: Forma Cuadrática de A ---
    x = np.linspace(-2, 2, 30)
    y = np.linspace(-2, 2, 30)
    X, Y = np.meshgrid(x, y)
    Z_A = A[0,0]*X**2 + (A[0,1]+A[1,0])*X*Y + A[1,1]*Y**2
    ax3.plot_surface(X, Y, Z_A, cmap=color_surface_A, alpha=0.8, edgecolor='k', linewidth=0.2)
    ax3.set_title('Forma Cuadrática xᵀAx > 0', pad=10)
    ax3.set_xlabel('x₁')
    ax3.set_ylabel('x₂')
    ax3.set_zlabel('xᵀAx')
    ax3.view_init(elev=25, azim=-50)

    # --- Subgráfico 4: Forma Cuadrática de B ---
    Z_B = B[0,0]*X**2 + (B[0,1]+B[1,0])*X*Y + B[1,1]*Y**2
    ax4.plot_surface(X, Y, Z_B, cmap=color_surface_B, alpha=0.8, edgecolor='k', linewidth=0.2)
    ax4.set_title('Forma Cuadrática xᵀBx (toma valores > 0 y < 0)', pad=10)
    ax4.set_xlabel('x₁')
    ax4.set_ylabel('x₂')
    ax4.set_zlabel('xᵀBx')
    ax4.view_init(elev=25, azim=-50)

    # Título general de la figura
    fig.suptitle('Propiedades Clave de los Autovalores', fontsize=22, fontweight='bold')
    
    return fig

# Generar el gráfico
main_figure = create_eigenvalue_visualization()

# 4. Bloque de Adición del Copyright
main_figure.text(0.98, 0.02, '© Alejandro Quintero Ruiz. Generado con Python.', 
                 ha='right', va='bottom', fontsize=10, color='gray', style='italic')

# 5. Bloque de Guardado/Exportación del Archivo
# Guardar en formato SVG (vectorial, ideal para escalabilidad) y PNG (alta resolución)
output_filename_svg = "propiedades_autovalores.svg"
output_filename_png = "propiedades_autovalores.png"

plt.savefig(output_filename_svg, format='svg', bbox_inches='tight')
plt.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')

# Mostrar el gráfico (opcional, útil en entornos interactivos como Jupyter)
plt.show()

print(f"Gráfico guardado como '{output_filename_svg}' y '{output_filename_png}'")

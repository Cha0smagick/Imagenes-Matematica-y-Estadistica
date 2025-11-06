# -*- coding: utf-8 -*-
"""
Script para generar un gráfico conceptual de alta calidad sobre los pilares
de la Probabilidad y Estadística para la Inteligencia Artificial.

Autor: Alejandro Quintero Ruiz (Generado con asistencia de IA)
"""

# =============================================================================
# 1. IMPORTACIÓN DE LIBRERÍAS
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, binom, beta

# =============================================================================
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# =============================================================================
# Parámetros para las visualizaciones
np.random.seed(42) # Para reproducibilidad

# --- Datos para Distribuciones ---
# Normal
mu, std = 0, 1
x_norm = np.linspace(mu - 4*std, mu + 4*std, 1000)
y_norm = norm.pdf(x_norm, mu, std)

# Binomial
n_binom, p_binom = 20, 0.4
x_binom = np.arange(binom.ppf(0.001, n_binom, p_binom), binom.ppf(0.999, n_binom, p_binom))
y_binom = binom.pmf(x_binom, n_binom, p_binom)

# --- Datos para EDA ---
eda_data = np.random.randn(150) * 2 + 5 # Datos simulados

# --- Datos para Inferencia Bayesiana ---
x_beta = np.linspace(0, 1, 100)
prior = beta.pdf(x_beta, 2, 2)
posterior = beta.pdf(x_beta, 2 + 6, 2 + 4) # Simulando 6 éxitos y 4 fracasos

# =============================================================================
# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
# =============================================================================
def generar_grafico_conceptual():
    """
    Genera y estiliza el gráfico conceptual completo.
    """
    # --- Configuración Inicial del Gráfico ---
    # Usamos un estilo profesional y una paleta de colores amigable (viridis)
    plt.style.use('seaborn-v0_8-whitegrid')
    fig = plt.figure(figsize=(16, 9))
    gs = fig.add_gridspec(5, 3, hspace=0.8, wspace=0.4)

    # Título principal
    fig.suptitle(
        'Probabilidad y Estadística Descriptiva: Fundamentos para la IA',
        fontsize=24,
        fontweight='bold',
        y=0.96
    )

    # --- Colores y Estilos ---
    colors = plt.cm.viridis(np.linspace(0.1, 0.9, 5))
    title_font = {'fontsize': 14, 'fontweight': 'bold'}

    # --- Bloque 1: Teoría de Probabilidad y Variables Aleatorias ---
    ax1_text = fig.add_subplot(gs[0, 0])
    ax1_text.text(0, 0.5, '1. Teoría de Probabilidad\ny Variables Aleatorias', va='center', ha='left', **title_font, color=colors[0])
    ax1_text.axis('off')

    ax1_discrete = fig.add_subplot(gs[0, 1])
    ax1_discrete.bar(x_binom[:7], y_binom[:7], color=colors[0], alpha=0.7)
    ax1_discrete.set_title('Discretas (PMF)', fontsize=10)
    ax1_discrete.set_yticks([])

    ax1_continuous = fig.add_subplot(gs[0, 2])
    ax1_continuous.plot(x_norm, y_norm, color=colors[0], lw=2)
    ax1_continuous.fill_between(x_norm, y_norm, color=colors[0], alpha=0.3)
    ax1_continuous.set_title('Continuas (PDF)', fontsize=10)
    ax1_continuous.set_yticks([])

    # --- Bloque 2: Valor Esperado (Media) y Varianza ---
    ax2_text = fig.add_subplot(gs[1, 0])
    ax2_text.text(0, 0.5, '2. Valor Esperado (Media)\ny Varianza', va='center', ha='left', **title_font, color=colors[1])
    ax2_text.axis('off')

    ax2_plot = fig.add_subplot(gs[1, 1:])
    ax2_plot.plot(x_norm, y_norm, color=colors[1], lw=2)
    ax2_plot.axvline(mu, color='black', linestyle='--', label=f'Media (μ = {mu})')
    ax2_plot.fill_between(np.linspace(mu-std, mu+std, 100), norm.pdf(np.linspace(mu-std, mu+std, 100)), color=colors[1], alpha=0.4, label=f'Varianza (σ² = {std**2})')
    ax2_plot.set_title('Conceptos Centrales en una Distribución', fontsize=10)
    ax2_plot.legend(fontsize=9)
    ax2_plot.set_yticks([])

    # --- Bloque 3: Distribuciones Clave ---
    ax3_text = fig.add_subplot(gs[2, 0])
    ax3_text.text(0, 0.5, '3. Distribuciones Clave', va='center', ha='left', **title_font, color=colors[2])
    ax3_text.axis('off')

    ax3_binom = fig.add_subplot(gs[2, 1])
    ax3_binom.bar(x_binom, y_binom, color=colors[2], alpha=0.7)
    ax3_binom.set_title('Distribución Binomial', fontsize=10)
    ax3_binom.set_yticks([])

    ax3_norm = fig.add_subplot(gs[2, 2])
    ax3_norm.plot(x_norm, y_norm, color=colors[2], lw=2)
    ax3_norm.fill_between(x_norm, y_norm, color=colors[2], alpha=0.3)
    ax3_norm.set_title('Distribución Normal (Gaussiana)', fontsize=10)
    ax3_norm.set_yticks([])

    # --- Bloque 4: Análisis Exploratorio de Datos (EDA) ---
    ax4_text = fig.add_subplot(gs[3, 0])
    ax4_text.text(0, 0.5, '4. Análisis Exploratorio\nde Datos (EDA)', va='center', ha='left', **title_font, color=colors[3])
    ax4_text.axis('off')

    ax4_hist = fig.add_subplot(gs[3, 1])
    ax4_hist.hist(eda_data, bins=15, color=colors[3], alpha=0.7, density=True)
    ax4_hist.set_title('Histograma', fontsize=10)
    ax4_hist.set_yticks([])

    ax4_box = fig.add_subplot(gs[3, 2])
    ax4_box.boxplot(eda_data, vert=False, patch_artist=True, boxprops=dict(facecolor=colors[3], alpha=0.7))
    ax4_box.set_title('Boxplot', fontsize=10)
    ax4_box.set_xticks([])

    # --- Bloque 5: Inferencia Estadística Bayesiana ---
    ax5_text = fig.add_subplot(gs[4, 0])
    ax5_text.text(0, 0.5, '5. Introducción a la\nInferencia Bayesiana', va='center', ha='left', **title_font, color=colors[4])
    ax5_text.axis('off')

    ax5_bayes = fig.add_subplot(gs[4, 1:])
    ax5_bayes.plot(x_beta, prior, 'k--', label='Creencia Inicial (Prior)')
    ax5_bayes.plot(x_beta, posterior, color=colors[4], lw=3, label='Creencia Actualizada (Posterior)')
    ax5_bayes.fill_between(x_beta, posterior, color=colors[4], alpha=0.3)
    ax5_bayes.text(0.5, 2.5, '+ Datos', fontsize=12, ha='center')
    ax5_bayes.annotate('', xy=(0.5, 2.2), xytext=(0.5, 0.5),
                     arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8))
    ax5_bayes.set_title('Prior + Datos → Posterior', fontsize=10)
    ax5_bayes.legend(fontsize=9)
    ax5_bayes.set_yticks([])

    # =============================================================================
    # 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
    # =============================================================================
    fig.text(
        0.98, 0.02,
        '© Alejandro Quintero Ruiz. Generado con Python.',
        ha='right',
        va='bottom',
        fontsize=10,
        color='gray',
        style='italic'
    )

    return fig

# =============================================================================
# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
# =============================================================================
if __name__ == '__main__':
    # Generar el gráfico
    grafico = generar_grafico_conceptual()

    # Definir nombres de archivo
    nombre_base = 'grafico_fundamentos_estadistica_ia'
    formato_vectorial = 'svg'
    formato_raster = 'png'

    # Guardar en formato vectorial (SVG) - ideal para escalabilidad
    ruta_svg = f'{nombre_base}.{formato_vectorial}'
    grafico.savefig(ruta_svg, format=formato_vectorial, bbox_inches='tight')
    print(f"Gráfico guardado en formato vectorial: {ruta_svg}")

    # Guardar en formato raster (PNG) con alta resolución (DPI)
    ruta_png = f'{nombre_base}.{formato_raster}'
    grafico.savefig(ruta_png, format=formato_raster, dpi=300, bbox_inches='tight')
    print(f"Gráfico guardado en formato raster de alta calidad: {ruta_png}")

    # Mostrar el gráfico (opcional)
    plt.show()

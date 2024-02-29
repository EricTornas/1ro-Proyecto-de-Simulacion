from Insurance_Company import simulate_insurance_risk_model
import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
import seaborn as sns

# Parámetros del modelo
# F es una distribución normal con media  10000 y desviación estándar  20
F = lambda: np.random.normal(10000, 5000)
a0 = 1000000  # Capital inicial
n0 = 500  # Número inicial de asegurados
param_lambda = 0.1  # Tasa de reclamaciones
param_ni = 0.5  # Tasa de nuevos asegurados
param_mi = 0.005  # Tasa de pérdida de asegurados
c = 1000  # Tarifa de pago por asegurado (mensual)
T = 60  # Tiempo final de la simulación (5 años)
cantS = 100
ganancias_maximas_por_simulacion = [0] * cantS
capital_perdido = [0] * cantS

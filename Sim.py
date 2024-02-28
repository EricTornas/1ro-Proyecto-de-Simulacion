from Insurance_Company import simulate_insurance_risk_model 
import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
import seaborn as sns

# Parámetros del modelo
# F es una distribución normal con media  10000 y desviación estándar  20
F = lambda: np.random.normal(10000,  5000)
a0 =  1000000  # Capital inicial
n0 =  500  # Número inicial de asegurados
param_lambda =  0.1  # Tasa de reclamaciones
param_ni =  0.5  # Tasa de nuevos asegurados
param_mi =  0.005  # Tasa de pérdida de asegurados 
c =  1000  # Tarifa de pago por asegurado (mensual)
T =  60  # Tiempo final de la simulación (5 años)
cantS = 100
ganancias_maximas_por_simulacion = [0] * cantS
capital_perdido = [0] * cantS

for j in range(cantS):
    result = simulate_insurance_risk_model(a0, n0,  param_lambda,  param_ni,  param_mi, c, T, F)
    (a, fbm, bankruptcy_time, profits, claims, cant_nNew, cant_nOut) = result
    (profit_fbm, time_fbm) = fbm
    ganancias_maximas_por_simulacion.append(profit_fbm)  
    for i in range(len(claims)):
        (cant_claims, amount) = claims[i]
        capital_perdido[j] += cant_claims


# Análisis estadístico
media_ganancias_maximas = mean(ganancias_maximas_por_simulacion)
varianza_ganancias_maximas = np.var(ganancias_maximas_por_simulacion)
media_Capital_perdido_por_reclamación  = mean(capital_perdido)
varianza_Capital_perdido_por_reclamación = np.var(capital_perdido)



# Imprimir resultados
print(f"Media de las ganancias maximas de las simulaciones: {media_ganancias_maximas}")
print(f"Varianza de las ganancias maximas de las de las simulaciones: {varianza_ganancias_maximas}")
print(f"Media del costo total de las reclamaciones: {media_Capital_perdido_por_reclamación }")
print(f"Varianza del costo total de las reclamaciones: {varianza_Capital_perdido_por_reclamación}")



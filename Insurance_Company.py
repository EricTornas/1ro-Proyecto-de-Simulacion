import numpy as np
import math
import matplotlib.pyplot as plt


def update_Capital(c, n, a, profits, start, end):
    start = math.floor(start)
    end = math.floor(end)
    profits[start] = a
    for i in range(start, end):
        profits[i] += a + c * n * (i - start)


def simulate_insurance_risk_model(a0, n0, param_lambda, param_ni, param_mi, c, T, F):
    t = 0
    a = a0
    n = n0

    cant_nNew = 0
    cant_nOut = 0
    profits = [0] * T
    claims = [(0, 0)] * T
    fbm = (0, 0)
    bankruptcy_time = float("inf")

    # Generamos el primer evento
    X = np.random.exponential(1 / (param_ni + n * param_mi + n * param_lambda))
    tE = X
    while tE <= T:
        update_Capital(c, n, a, profits, t, tE)  # Actualizamos el capital de la empresa
        t = tE  # Actualizamos el tiempo

        if J == 1:  # Nuevo asegurado
            n += 1
            cant_nNew += 1
        elif J == 2:  # Asegurado perdido
            n -= 1
            cant_nOut += 1
        else:  # Reclamación
            Y = F()  # función que genera el monto de una reclamación
            (cant_claims, amount) = claims[
                math.floor(t)
            ]  # Actualizamos la cantidad de Reclamaciones en una unidad temporal y el monto total de esas reclamaciones para esa unidad temporal
            a -= Y
            cant_claims += 1
            amount += Y
            claims[math.floor(t)] = (cant_claims, amount)
            if a <= 0:  # Momento de quiebra
                bankruptcy_time = math.ceil(t)

        (profit_fbm, time_fbm) = fbm  # Actualizamos el mejor momento
        if a > profit_fbm:
            fbm = (a, math.ceil(t))
        # Generamos el próximo evento
        X = np.random.exponential(1 / (param_ni + n * param_mi + n * param_lambda))
        tE = t + X

    return a, fbm, bankruptcy_time, profits, claims, cant_nNew, cant_nOut

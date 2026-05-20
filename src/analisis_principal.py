import pandas as pd

from funciones import (
    calcular_eficiencia,
    crear_reporte_operaciones,
    crear_reporte_ambiental,
    generar_dashboard
)

df = pd.read_excel(
    "../data/dataset_set_A_aguas_residuales.xlsx"
)

print(df.head())

print(df.info())

print(df.describe())

df = calcular_eficiencia(df)

resumen_plantas = df.groupby("planta")[[
    "DBO_entrada_mg_L",
    "DBO_salida_mg_L",
    "eficiencia_tratamiento",
    "caudal_entrada_m3_d"
]].mean()

print(resumen_plantas)

reporte_operaciones = crear_reporte_operaciones(df)

reporte_ambiental = crear_reporte_ambiental(df)

reporte_operaciones.to_excel(
    "../outputs/reporte_operaciones.xlsx",
    index=False
)

reporte_ambiental.to_excel(
    "../outputs/reporte_gestion_ambiental.xlsx",
    index=False
)

generar_dashboard(df)
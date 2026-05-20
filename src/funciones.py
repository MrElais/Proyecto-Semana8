import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def calcular_eficiencia(df):

    df["eficiencia_tratamiento"] = (
        (
            df["DBO_entrada_mg_L"] -
            df["DBO_salida_mg_L"]
        )
        / df["DBO_entrada_mg_L"]
    ) * 100

    return df

def crear_reporte_operaciones(df):

    reporte = df[[
        "fecha_registro",
        "planta",
        "caudal_entrada_m3_d",
        "DBO_entrada_mg_L",
        "DBO_salida_mg_L",
        "energia_aeracion_kWh",
        "lodos_generados_kg_d"
    ]]

    return reporte

def crear_reporte_ambiental(df):

    reporte = df[[
        "fecha_registro",
        "planta",
        "DBO_salida_mg_L",
        "cumplimiento_norma"
    ]]

    return reporte

def generar_dashboard(df):

    plt.figure(figsize=(15, 6))

    # gráfico eficiencia
    plt.subplot(1, 2, 1)

    sns.barplot(
        data=df,
        x="planta",
        y="eficiencia_tratamiento",
        hue="planta",
        palette="Blues",
        legend=False,
        errorbar=None
    )

    plt.title("Eficiencia Promedio")
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    # gráfico DBO salida
    plt.subplot(1, 2, 2)

    sns.barplot(
        data=df,
        x="planta",
        y="DBO_salida_mg_L",
        hue="planta",
        palette="Greens",
        legend=False,
        errorbar=None
    )

    plt.title("DBO Salida Promedio")
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()

    plt.savefig("../outputs/dashboard.png")

    plt.show()
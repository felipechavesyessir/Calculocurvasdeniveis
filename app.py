import math
import pandas as pd
import streamlit as st

st.title("📐 Calculadora de Proporção de Inteiros")

# ── Sidebar ──────────────────────────────────────────────────────────────────
st.sidebar.header("Parâmetros de Entrada")

limite_inferior = st.sidebar.number_input(
    "Limite Inferior",
    value=0.0,
    format="%.4f",
    help="Valor decimal inicial do intervalo.",
)

limite_superior = st.sidebar.number_input(
    "Limite Superior",
    value=10.0,
    format="%.4f",
    help="Valor decimal final do intervalo.",
)

distancia_total = st.sidebar.number_input(
    "Distância Total",
    value=100.0,
    format="%.4f",
    help="A medida real entre os dois limites.",
)

# ── Main area ─────────────────────────────────────────────────────────────────
calcular = st.button("Calcular")

if calcular:
    # Validate inputs
    if limite_superior <= limite_inferior:
        st.error(
            "O **Limite Superior** deve ser maior que o **Limite Inferior**."
        )
    elif distancia_total <= 0:
        st.error("A **Distância Total** deve ser um valor positivo.")
    else:
        delta = limite_superior - limite_inferior

        # Find all integers strictly inside the open interval
        primeiro = math.floor(limite_inferior) + 1
        ultimo = math.ceil(limite_superior) - 1

        inteiros = list(range(primeiro, ultimo + 1))
        inteiros = [n for n in inteiros if limite_inferior < n < limite_superior]

        if not inteiros:
            st.warning(
                "Nenhum número inteiro foi encontrado no intervalo "
                f"({limite_inferior}, {limite_superior})."
            )
        else:
            # Rule-of-three calculation
            resultados = []
            for n in inteiros:
                x = (limite_superior - n) * distancia_total / delta
                resultados.append({"Número Inteiro": n, "Distância até o Limite Superior": round(x, 4)})

            df = pd.DataFrame(resultados)

            st.subheader("Resultados")
            st.table(df)

            # ── Chart ─────────────────────────────────────────────────────────
            st.subheader("Posição dos Inteiros no Intervalo")

            chart_df = df.set_index("Número Inteiro")[["Distância até o Limite Superior"]]
            st.bar_chart(chart_df)

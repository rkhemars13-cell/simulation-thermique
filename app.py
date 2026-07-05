import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuration de la page
st.set_page_config(page_title="Simulation Thermique", layout="centered")
st.title("🌡️ Simulation du refroidissement d'une boisson")
st.write("Faites varier les paramètres dans la barre latérale pour observer l'évolution de la température.")

# Barre latérale pour les paramètres (les curseurs)
st.sidebar.header("Paramètres physiques")
h = st.sidebar.slider("Coeff. conducto-convectif h (W/m²/K)", 5.0, 150.0, 30.0, 5.0)
S = st.sidebar.slider("Surface d'échange S (m²)", 0.01, 0.10, 0.03, 0.005)
m = st.sidebar.slider("Masse de la boisson m (kg)", 0.10, 1.0, 0.33, 0.05)
C = st.sidebar.slider("Capacité thermique C (J/kg/K)", 1000, 4185, 4185, 100)

st.sidebar.header("Températures")
T_initiale = st.sidebar.slider("Température initiale (°C)", 40.0, 90.0, 80.0, 5.0)
T_exterieure = st.sidebar.slider("Température ambiante (°C)", 4.0, 30.0, 20.0, 1.0)

# Calculs physiques
tau = (m * C) / (h * S)
k = 1 / tau
temps = np.linspace(0, 3600, 1000)
temperature = T_exterieure + (T_initiale - T_exterieure) * np.exp(-k * temps)

# Graphique Matplotlib
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(temps / 60, temperature, color='#1a365d', linewidth=2.5, label="Température boisson")
ax.axhline(y=T_exterieure, color='red', linestyle='--', alpha=0.7, label=f"Température ambiante ({T_exterieure}°C)")
ax.axvline(x=tau / 60, color='green', linestyle=':', alpha=0.7, label=f"τ = {tau/60:.1f} min")

ax.set_title(f"Loi de Newton (Constante de temps τ = {tau:.0f} secondes)", fontsize=12, fontweight='bold')
ax.set_xlabel("Temps (en minutes)", fontsize=11)
ax.set_ylabel("Température (°C)", fontsize=11)
ax.set_xlim(0, 60)
ax.set_ylim(min(T_initiale, T_exterieure) - 5, max(T_initiale, T_exterieure) + 5)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc="upper right")

# Affichage du graphique dans l'application web
st.pyplot(fig)

# Petit bilan écrit en dessous
st.subheader("📊 Bilan du système :")
st.write(f"• La constante de temps **τ** est de **{tau:.1f} secondes** (soit **{tau/60:.1f} minutes**).")
st.write(f"• À l'instant t = τ, la température atteint **{T_exterieure + (T_initiale - T_exterieure) * 0.37:.1f} °C**.")

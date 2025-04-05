import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

csv_file = "smart_city_citizen_activity.csv"
df = pd.read_csv(csv_file)

st.title("Analiza activitate cetateni")

st.subheader("Datele initiale")
st.write(df.head(10))

# Distributia varstei
st.subheader("Distributia varstei cetatenilor")
fig, ax = plt.subplots()
df["Age"].hist(bins=20, edgecolor="black", ax=ax)
ax.set_xlabel("Varsta")
ax.set_ylabel("Numar cetateni")
st.pyplot(fig)

# Filtrare dupa varsta
st.subheader("Filtrare dupa varsta")
min_age, max_age = int(df["Age"].min()), int(df["Age"].max())
age_range = st.slider("Selecteaza intervalul de varsta:", min_age, max_age, (30, 50))
filtered_df = df[(df["Age"] >= age_range[0]) & (df["Age"] <= age_range[1])]
st.write(filtered_df)

# Persoanele cu cea mai mare amprenta de carbon
st.subheader("Top 5 cetateni cu cea mai mare amprenta de carbon")
sorted_df = df.sort_values(by="Carbon_Footprint_kgCO2", ascending=False).head(5)
st.write(sorted_df)

# Consumul de energie acasa in functie de varsta
st.subheader("Consumul de energie acasa in functie de varsta")
fig, ax = plt.subplots()
ax.scatter(df["Age"], df["Home_Energy_Consumption_kWh"], alpha=0.5)
ax.set_xlabel("Varsta")
ax.set_ylabel("Consum de energie acasa (kWh)")
st.pyplot(fig)

# Media pasilor parcursi zilnic
st.subheader("Media pasilor parcursi zilnic")
fig, ax = plt.subplots()
df["Steps_Walked"].hist(bins=20, edgecolor="black", ax=ax)
ax.set_xlabel("Numar pasi")
ax.set_ylabel("Numar cetateni")
st.pyplot(fig)

st.subheader("Statistici")
st.write(f"*Varsta medie:* {df['Age'].mean():.2f} ani")
st.write(f"*Consum mediu de energie acasa:* {df['Home_Energy_Consumption_kWh'].mean():.2f} kWh")
st.write(f"*Media pasilor parcursi zilnic:* {df['Steps_Walked'].mean():.0f} pasi")
st.write(f"*Media orelor de somn:* {df['Sleep_Hours'].mean():.2f} ore")
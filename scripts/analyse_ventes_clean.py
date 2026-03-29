import pandas as pd

import matplotlib.pyplot as plt 


import os
dossier = os.path.dirname(__file__)
fichier = os.path.join(dossier, "ventes_clean.csv")

df = pd.read_csv(fichier)

df["Chiffres_affaires"] = df["Quantite"] * df["Prix"]

print("\n=== ANANLYSE DES VENTES (DATA CLEAN) ===")

print("\n--- Résultats globaux ---")
print("CA total :", df["Chiffres_affaires"].sum())

print("\n--- Produits ---")
quantites = df.groupby("Produit")["Quantite"].sum()
print("Produit top :", quantites.idxmax())

print("\n--- Catégories ---")
ca = df.groupby("Categorie")["Chiffres_affaires"].sum()
print("Catégorie top :", ca.idxmax())

ca.plot(kind="bar")

plt.title("Chiffres d'affaires par catégorie")
plt.xlabel("Catégorie")
plt.ylabel("CA")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("graphs/graph_ca_categories.png")

plt.show()

plt.figure()

ca.plot(kind="pie", autopct="%1.1f%%")

plt.title("Répartaition du chiffre d'affaires")
plt.ylabel("")

plt.savefig("graphs/graph_pie.png")

plt.show()

plt.figure()

df["Prix"].plot(kind="hist", bins=3)
plt.title("Distribution des prix")
plt.xlabel("Prix")

plt.tight_layout()

plt.savefig("graphs/graph_hist.png")

plt.show()





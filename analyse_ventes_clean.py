import pandas as pd

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


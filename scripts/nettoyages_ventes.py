import pandas as pd

import os
dossier = os.path.dirname(__file__)
fichier = os.path.join(dossier, "ventes_sales.csv")

df = pd.read_csv(fichier)

print(df.info())
print(df.isnull().sum())

df["Prix"] = pd.to_numeric(df["Prix"], errors='coerce')
print(df)
#supprimer quantités manquantes
df = df.dropna(subset=["Quantite"])
#supprimer prix manquants
df = df.dropna(subset=["Prix"])
#remplir catégorie manquante
df["Categorie"] = df["Categorie"].fillna("Inconnue")
#supprimer quantités négatives
df = df[df["Quantite"] >= 0 ]

print("\n=== DATA CLEAN ===")
print(df)

df["Chiffres_affaires"] = df["Quantite"] * df["Prix"]

print("\nChiffre d'affaires total :", df["Chiffres_affaires"].sum())

quantites = df.groupby("Produit")["Quantite"].sum()
print("\nProduit le plus vendu :", quantites.idxmax())

ca = df.groupby("Categorie")["Chiffres_affaires"].sum()
print("\nCatégorie la plus rentable :", ca.idxmax())

df.to_csv("ventes_clean.csv", index=False)

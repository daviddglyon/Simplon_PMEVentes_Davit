import plotly.express as px
import pandas as pd
import sqlite3

con = sqlite3.connect("SQLite.db")
ventes = pd.read_sql_query("SELECT produit, sum(qte) ventes_par_produit  FROM ventes GROUP BY produit;", con)
ca = pd.read_sql_query("SELECT produit, sum(qte * prix) CA FROM ventes GROUP by produit;", con)
con.close()

figure_ventes_par_produit = px.pie(ventes, values='ventes_par_produit', names='produit', title='quantité vendue par produit')
figure_ventes_par_produit.write_html('ventes-par-produit.html')
print('ventes-par-produit.html généré avec succès !')

figure_ca_par_produit     = px.pie(ca, values='CA', names='produit', title='CA par produit')
figure_ca_par_produit.write_html('ca-par-produit.html')
print('ca-par-produit.html généré avec succès !')



# Importation des bibliothèques nécessaires

import streamlit as st
import plotly.express as px
import seaborn as sns

# Titre de l'application : mot de bienvenue !

st.title("Bienvenue sur l'application de recommandation offerte par votre cinéma !")
st.write("Nous sommes tout simplement ravis de pouvoir vous proposer de prolonger votre expérience cinématographique au-delà de nos murs.")
st.write("\n\n")
st.write('_____')

# Première partie : prise en compte du film de référence

st.subheader("Commencez par nous donner le nom d'un film que vous avez aimé.")
st.markdown(''':rainbow: :rainbow[Un film qui vous a fait rêver, pleurer, vibrer, ... à vous de choisir !]''')
film_ref = st.text_input("Quel est le nom du film que vous avez en tête ?")

st.write("\n\n")
st.write('_____')

# Deuxième partie : ajout de critères personnalisés

st.subheader("Ensuite, dites-nous un peu quel type de film vous ferait envie là, tout de suite, maintenant !")
st.markdown(''':rainbow: :rainbow[Une histoire à pleurer de rire ? Un thriller haletant ? Une lovestory fabuleuse ?]''')

st.radio("Pourriez-vous me dire quel genre de film vous avez envie de regarder ?", ['Comédie', 'Aventure', 'Thriller', 'Romance', 'Documentaire', 'Dessin animé'])
st.number_input("Pourriez-vous me donner la durée maximale (en minutes) de film que vous aimeriez voir ?", min_value=60)

st.write("\n\n")
st.write('_____')

# Troisième partie : propositions de films

st.subheader("Jetez un oeil aux autres films qui pourraient vous plaire !")
st.markdown(''':rainbow: :rainbow[Un océan de possibilités s'offre à vous !]''')

st.write("\n\n")
st.write('_____')

# Quelques graphiques

st.header("Le monde du cinéma te fascine...? Nous aussi !")

st.toggle("Souhaites-tu voir quelques graphiques sur le monde du cinéma ?", value = True)

# Création des graphiques

st.text('Graphiques disponibles :')

scatter_chart = st.checkbox("Diagramme à nuages de points")

bar_chart = st.checkbox("Graphique à barres")

line_chart = st.checkbox("Graphique linéaire")


st.write("\n\n")


# Affichage des graphiques

if scatter_chart :

    st.write("Voici un diagramme à nuages de points :")

elif bar_chart :

    st.write("Voici un graphique à barres :")

elif line_chart :

    st.write("Voici un graphique linéaire :")

else:

    st.write("N'oublie pas de cocher une case si tu veux voir un graphique, et évite de cocher plusieurs cases en même temps !")


# Ajout d'un selectbox

st.selectbox("Quel est ton graphique préféré ?", ['Nuage de points', 'Graphique à barres', 'Graphique linéaire'])

st.write("\n\n")
st.write('_____')

# Ajout d'un select_slider

st.header("Votre avis est précieux, aidez-nous à améliorer cette application de recommandation !")

st.markdown(''':rainbow: :rainbow[Donnez votre avis !]''')
st.select_slider("Alors, t'as pensé quoi de notre appli ?", ['Vraiment nulle', 'Bof', 'Pas mal!', 'Tout à fait correcte', 'Elle est réussie', 'Vraiment trop cool', 'Extraordinaire'], value = 'Extraordinaire')

st.text_area("Pourriez-vous nous expliquer votre avis ?")

# Ajout de boutons

st.checkbox("Souhaites-tu recevoir la programmation du cinéma par e-mail ?")

if st.button("Tu penses réutiliser notre application ?"):
    st.write("Merciiii ! A très bientôt !")

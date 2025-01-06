# Importation des bibliothèques nécessaires
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler
from sklearn.neighbors import NearestNeighbors, KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from deep_translator import GoogleTranslator
translator = GoogleTranslator(source='auto', target='fr')

# Importation du dataset
df = pd.read_csv("df_avecgenretrad.csv")

# Ajout d'un fond sonore
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.audio("mediavision.mp3", format="audio/mpeg", autoplay = False)
with col3:
    st.write(' ')

# Ajout d'un fond d'écran
page_element="""<style>[data-testid="stAppViewContainer"]{background-image: url("https://lafibre.info/images/smileys/201004_Warm_lights_by_Max_Barners.jpg");
  background-size: cover;}</style>"""
st.markdown(page_element, unsafe_allow_html=True)

# Création d'un menu permettant d'accéder à la page d'accueil ou d'accéder à deux stratégies différentes de choix du film
option = st.sidebar.selectbox("Quelle page de notre application souhaiteriez-vous consulter ?", ["Accueil", "Choix par acteur / réalisateur", "Choix par genre / période", "Choix à partir d'un film"])
if option == "Accueil":
    # Première page: page d'accueil
    # Ajout d'un mot de bienvenue
    st.markdown("""<h1 style="color: white; text-align: center;">Bienvenue sur l'application de recommandations</h1>
        <h2 style="color: orange; text-align: center;">Offerte par votre cinéma ! </h2>
        """, unsafe_allow_html=True)
    st.write("\n\n")

    # Ajout du logo de l'agence Multimedia-Creuse, au centre de trois colonnes
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<h3 style="color: white; text-align: center;">Voici une suggestion de documentaires...</h3>
        """, unsafe_allow_html=True)
        st.write(' ')
    with col2:
        st.image("logo.png")
    with col3:
        st.markdown("""<h3 style="color: white; text-align: center;">... en prévision des festivals du cinéma | 2025 </h3>
        """, unsafe_allow_html=True)
        st.write(' ')

    st.write("\n\n")
    st.write('_____')

    # Ajout de quelques documentaires conseillés car thème récurrent des festivals cinéma
    col1, col2, col3 = st.columns(3)
    recoaccueil = df[df['genres'].str.contains("Documentary")].sort_values(by='averageRating', ascending=False).sample(6)

    with col1:
        for i, j in recoaccueil.iloc[0:2].iterrows():
            base_image = "https://image.tmdb.org/t/p/w500"
            URL_image = base_image + j['poster_path']
            base_imdb = "https://www.imdb.com/title/"
            URL_imdb = base_imdb + j['tconst']
            regions = [x.strip("'")for x in j['region'].split(", ")]
            titres = [x.strip("'")for x in j['title'].split(", ")]
            if 'FR' in regions:
                indexfr = regions.index('FR')
                titrefr = titres[indexfr].strip("['[\"").replace('"',"")
            else:
                titrefr = titres[0].strip("['[\"").replace('"',"")
            st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
            st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

            st.write(f"  - 🎭 Genre : {j['Genre_trad']}\n"
                     f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h {int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                     f"  - ⭐ Note moyenne : {j['averageRating']}\n")
            with st.expander("📜 Lire le résumé"):
                if pd.isna(j['overview']) or len(j['overview']) > 4998:
                    st.write("Aucun résumé disponible.")
                else:
                    st.write(translator.translate(j['overview']))

    with col2:
        for i, j in recoaccueil.iloc[2:4].iterrows():
            base_image = "https://image.tmdb.org/t/p/w500"
            URL_image = base_image + j['poster_path']
            base_imdb = "https://www.imdb.com/title/"
            URL_imdb = base_imdb + j['tconst']
            regions = [x.strip("'")for x in j['region'].split(", ")]
            titres = [x.strip("'")for x in j['title'].split(", ")]
            if 'FR' in regions:
                indexfr = regions.index('FR')
                titrefr = titres[indexfr].strip("['[\"").replace('"',"")
            else:
                titrefr = titres[0].strip("['[\"").replace('"',"")
            st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
            st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

            st.write(f"  - 🎭 Genre : {j['Genre_trad']}\n"
                     f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h {int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                     f"  - ⭐ Note moyenne : {j['averageRating']}\n")
            with st.expander("📜 Lire le résumé"):
                if pd.isna(j['overview']) or len(j['overview']) > 4998:
                    st.write("Aucun résumé disponible.")
                else:
                    st.write(translator.translate(j['overview']))

    with col3:
        for i, j in recoaccueil.iloc[4:6].iterrows():
            base_image = "https://image.tmdb.org/t/p/w500"
            URL_image = base_image + j['poster_path']
            base_imdb = "https://www.imdb.com/title/"
            URL_imdb = base_imdb + j['tconst']
            regions = [x.strip("'")for x in j['region'].split(", ")]
            titres = [x.strip("'")for x in j['title'].split(", ")]
            if 'FR' in regions:
                indexfr = regions.index('FR')
                titrefr = titres[indexfr].strip("['[\"").replace('"',"")
            else:
                titrefr = titres[0].strip("['[\"").replace('"',"")
            st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
            st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

            st.write(f"  - 🎭 Genre : {j['Genre_trad']}\n"
                     f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h {int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                     f"  - ⭐ Note moyenne : {j['averageRating']}\n")
            with st.expander("📜 Lire le résumé"):
                if pd.isna(j['overview']) or len(j['overview']) > 4998:
                    st.write("Aucun résumé disponible.")
                else:
                    st.write(translator.translate(j['overview']))

# Deuxième page : choix par acteur
elif option == "Choix par acteur / réalisateur":
    st.markdown("""<h3 style="color: white; text-align: center;">Sur cette page vous allez accéder à une sélection de films en choisissant un acteur !</h3>
    """, unsafe_allow_html=True)
    st.write("\n\n")

    acteur = st.text_input("Entrez le nom d'un acteur:")

    st.write('_____')
    st.markdown("""<h5 style="color: white; text-align: center;">En attendant votre choix, nous vous proposons les films les mieux notés de notre base de données.</h5>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        films_acteur = df[df['primaryName'].str.contains(acteur, case=False, na=False)].sort_values(by='averageRating',ascending=False)
        for index, row in films_acteur.iloc[0:2].iterrows():
            base_image = "https://image.tmdb.org/t/p/w500"
            URL_image = base_image + row['poster_path']
            base_imdb = "https://www.imdb.com/title/"
            URL_imdb = base_imdb + row['tconst']
            regions = [x.strip("'")for x in row['region'].split(", ")]
            titres = [x.strip("'")for x in row['title'].split(", ")]
            if 'FR' in regions:
                indexfr = regions.index('FR')
                titrefr = titres[indexfr].strip("['[\"").replace('"',"")
            else:
                titrefr = titres[0].strip("['[\"").replace('"',"")
            st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
            st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(row['startYear'])})</span></div>""", unsafe_allow_html=True)

            st.write(f"  - 🎭 Genre : {row['Genre_trad']}\n"
                     f"  - ⌛ Durée : {int(row['runtimeMinutes']//60)}h {int(row['runtimeMinutes']-((row['runtimeMinutes']//60)*60))}min\n"
                     f"  - ⭐ Note moyenne : {row['averageRating']}\n")
            with st.expander("📜 Lire le résumé"):
                if pd.isna(row['overview']) or len(row['overview']) > 4998:
                    st.write("Aucun résumé disponible.")
                else:
                    st.write(translator.translate(row['overview']))

    with col2:
        films_acteur = df[df['primaryName'].str.contains(acteur, case=False, na=False)].sort_values(by='averageRating', ascending=False)
        for index, row in films_acteur.iloc[2:4].iterrows():
            base_image = "https://image.tmdb.org/t/p/w500"
            URL_image = base_image + row['poster_path']
            base_imdb = "https://www.imdb.com/title/"
            URL_imdb = base_imdb + row['tconst']
            regions = [x.strip("'")for x in row['region'].split(", ")]
            titres = [x.strip("'")for x in row['title'].split(", ")]
            if 'FR' in regions:
                indexfr = regions.index('FR')
                titrefr = titres[indexfr].strip("['[\"").replace('"',"")
            else:
                titrefr = titres[0].strip("['[\"").replace('"',"")
            st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
            st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(row['startYear'])})</span></div>""", unsafe_allow_html=True)

            st.write(f"  - 🎭 Genre : {row['Genre_trad']}\n"
                     f"  - ⌛ Durée : {int(row['runtimeMinutes']//60)}h {int(row['runtimeMinutes']-((row['runtimeMinutes']//60)*60))}min\n"
                     f"  - ⭐ Note moyenne : {row['averageRating']}\n")
            with st.expander("📜 Lire le résumé"):
                if pd.isna(row['overview']) or len(row['overview']) > 4998:
                    st.write("Aucun résumé disponible.")
                else:
                    st.write(translator.translate(row['overview']))

    with col3:
        films_acteur = df[df['primaryName'].str.contains(acteur, case=False, na=False)].sort_values(by='averageRating', ascending=False)
        for index, row in films_acteur.iloc[4:6].iterrows():
            base_image = "https://image.tmdb.org/t/p/w500"
            URL_image = base_image + row['poster_path']
            base_imdb = "https://www.imdb.com/title/"
            URL_imdb = base_imdb + row['tconst']
            regions = [x.strip("'")for x in row['region'].split(", ")]
            titres = [x.strip("'")for x in row['title'].split(", ")]
            if 'FR' in regions:
                indexfr = regions.index('FR')
                titrefr = titres[indexfr].strip("['[\"").replace('"',"")
            else:
                titrefr = titres[0].strip("['[\"").replace('"',"")
            st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
            st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(row['startYear'])})</span></div>""", unsafe_allow_html=True)

            st.write(f"  - 🎭 Genre : {row['Genre_trad']}\n"
                     f"  - ⌛ Durée : {int(row['runtimeMinutes']//60)}h {int(row['runtimeMinutes']-((row['runtimeMinutes']//60)*60))}min\n"
                     f"  - ⭐ Note moyenne : {row['averageRating']}\n")
            with st.expander("📜 Lire le résumé"):
                if pd.isna(row['overview']) or len(row['overview']) > 4998:
                    st.write("Aucun résumé disponible.")
                else:
                    st.write(translator.translate(row['overview']))

    st.write("\n\n")
    st.write('_____')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')
    with col2:
        st.write(' ')
    with col3:
        st.write(' ')

    st.write("\n\n")

# Troisième page : choix par genre et par période
elif option == "Choix par genre / période" :
    st.markdown("""<h2 style="color: white; text-align: center;"> Hey ! Ici vous allez pouvoir choisir un genre et une période pour votre film ✨ </h2>
    """, unsafe_allow_html=True)

    st.write('_____')
    st.write("\n\n")

    genres = {
        'Drame': 0,'Crime': 1,'Comédie': 2,'Action': 3,'Aventure': 4,
        'Biographie': 5,'Romance': 6,'Fantaisie': 7,'Horreur': 9,
        'Mystère': 10,'Science-fiction': 11,'Animation': 12,
        'Documentaire': 13,'Western': 14,'Famille': 16,'Thriller': 17,
        'Guerre': 18,'Histoire': 20}

    startyear, endyear = st.select_slider("Choisissez une date de début et une date de fin pour la période de votre film",
                                            options=range(1930, 2025),
                                            value=(1930, 2024))

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')

    with col2:
        X = df[['startYear','genre_facto']]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        model = NearestNeighbors(n_neighbors=3, metric="euclidean")
        model.fit(X_scaled)

        genre_selection = st.selectbox("Choisissez un genre :", list(genres.keys()))
        genre_facto = genres[genre_selection]
        recom_final = pd.DataFrame()

        if st.button("Lancer la recherche"):
            recom = []
            for i in range(startyear, endyear + 1):
                criteres = pd.DataFrame([[i, genre_facto]], columns=['startYear', 'genre_facto'])
                criteres_scaled = scaler.transform(criteres)
                distance, indice = model.kneighbors(criteres_scaled)
                reco = df.iloc[indice[0]].copy()
                reco['Distance'] = distance[0]
                reco = reco[(reco['startYear'] >= startyear) & (reco['startYear'] <= endyear)]
                recom.append(reco)


            recom_final = pd.concat(recom).drop_duplicates(subset=['primaryTitle', 'startYear'])
            recom_final = recom_final.sort_values(["Distance", "averageRating"], ascending=[True, False])

        st.write(' ')
        st.markdown("<h3 style='color: orange; text-align: center;'>Top 6 des recommandations</h3>", unsafe_allow_html=True)
        st.write("\n\n")

    with col3:
        st.write(' ')

    col1, col2, col3 = st.columns(3)
    with col1:
        if recom_final.empty:
            st.write(" ")
        else:
            for i, j in recom_final.iloc[0:2].iterrows():
                base_image = "https://image.tmdb.org/t/p/w500"
                URL_image = base_image + j['poster_path']
                base_imdb = "https://www.imdb.com/title/"
                URL_imdb = base_imdb + j['tconst']
                regions = [x.strip("'")for x in j['region'].split(", ")]
                titres = [x.strip("'")for x in j['title'].split(", ")]
                if 'FR' in regions:
                  indexfr = regions.index('FR')
                  titrefr = titres[indexfr].strip("['[\"").replace('"',"")
                else:
                    titrefr = titres[0].strip("['[\"").replace('"',"")
                st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
                st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

                st.write(f"  - 🎭 Genre : {j['Genre_trad']}\n"
                        f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h {int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                        f"  - ⭐ Note moyenne : {j['averageRating']}\n")
                with st.expander("📜 Lire le résumé"):
                    if pd.isna(j['overview']) or len(j['overview']) > 4998:
                        st.write("Aucun résumé disponible.")
                    else:
                        st.write(translator.translate(j['overview']))
        st.write(' ')

    with col2:
        if recom_final.empty:
            st.markdown("<h5 style='color: white; text-align: center;'>Choisissez une période et un genre ci-dessus !</h5>", unsafe_allow_html=True)

        else:
            for i, j in recom_final.iloc[2:4].iterrows():
                base_image = "https://image.tmdb.org/t/p/w500"
                URL_image = base_image + j['poster_path']
                base_imdb = "https://www.imdb.com/title/"
                URL_imdb = base_imdb + j['tconst']
                regions = [x.strip("'")for x in j['region'].split(", ")]
                titres = [x.strip("'")for x in j['title'].split(", ")]
                if 'FR' in regions:
                  indexfr = regions.index('FR')
                  titrefr = titres[indexfr].strip("['[\"").replace('"',"")
                else:
                    titrefr = titres[0].strip("['[\"").replace('"',"")
                st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
                st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

                st.write(f"  - 🎭 Genre : {j['Genre_trad']}\n"
                        f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h {int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                        f"  - ⭐ Note moyenne : {j['averageRating']}\n")
                with st.expander("📜 Lire le résumé"):
                    if pd.isna(j['overview']) or len(j['overview']) > 4998:
                        st.write("Aucun résumé disponible.")
                    else:
                        st.write(translator.translate(j['overview']))

        st.write(' ')

    with col3:
        if recom_final.empty:
            st.write(" ")
        else:
            for i, j in recom_final.iloc[4:6].iterrows():
                base_image = "https://image.tmdb.org/t/p/w500"
                URL_image = base_image + j['poster_path']
                base_imdb = "https://www.imdb.com/title/"
                URL_imdb = base_imdb + j['tconst']
                regions = [x.strip("'")for x in j['region'].split(", ")]
                titres = [x.strip("'")for x in j['title'].split(", ")]
                if 'FR' in regions:
                  indexfr = regions.index('FR')
                  titrefr = titres[indexfr].strip("['[\"").replace('"',"")
                else:
                    titrefr = titres[0].strip("['[\"").replace('"',"")
                st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
                st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; color: white;">{titrefr}</span>
                            <span style="font-size: 14px; font-weight: normal; color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

                st.write(f"  - 🎭 Genre : {j['Genre_trad']}\n"
                        f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h {int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                        f"  - ⭐ Note moyenne : {j['averageRating']}\n")
                with st.expander("📜 Lire le résumé"):
                    if pd.isna(j['overview']) or len(j['overview'])>4998:
                        st.write("Aucun résumé disponible.")
                    else:
                        st.write(translator.translate(j['overview']))

        st.write(' ')

    st.write("\n\n")
    st.write('_____')

# Quatrième page : sélection à partir d'un film
else:

    # Visuel avec encadré
    with st.form("form 1"):
        st.subheader("Une sélection de trois films à partir d'un film apprécié")

        # Préparation du DataFrame
        df_bis = df.copy()
        colonnes_num = ['genre_facto', 'averageRating', 'numVotes', 'startYear', 'runtimeMinutes']
        features = df_bis[colonnes_num]

        # Normalisation des données numériques
        scaler = RobustScaler().fit(features.values)
        features_scaled = scaler.transform(features.values)
        df_bis[colonnes_num] = features_scaled

        # Utilisation du TfidfVectorizer pour transformer les titres de films en vecteurs
        tfidf_vectorizer = TfidfVectorizer(ngram_range=(1,4), min_df=2, max_df=0.25, sublinear_tf=True, use_idf=True)
        tfidf_matrix = tfidf_vectorizer.fit_transform(df_bis['primaryTitle'])

        # Fusion des données numériques normalisées et des vecteurs TF-IDF en un dataframe
        tfidf_importance = 10
        tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
        tfidf_df *= tfidf_importance

        # Définition des variables à utiliser pour le Machine Learning
        X_bis = pd.concat([df_bis[['genre_facto', 'averageRating', 'numVotes', 'startYear', 'runtimeMinutes']], tfidf_df], axis=1)
        y_bis = df_bis['primaryTitle']

        # Choix de l'algortihme et entraînement
        knn = NearestNeighbors(n_neighbors=4, metric='euclidean')
        knn.fit(X_bis, y_bis)

        # Création du contenu de la liste déroulante
        df_liste_vf = df['titre_fr'].apply(lambda x: x.strip("['[\"")).tolist()
        df_liste_vo = df['primaryTitle'].apply(lambda x: x.strip("['[\"")).tolist()
        df_liste = df_liste_vf + df_liste_vo
        df_liste = list(set(df_liste))
        df_liste.insert(0, '')

        # Ajout d'une selectbox incluant la liste déroulante
        film_select = st.selectbox('Quel film souhaiteriez-vous prendre comme référence ?', df_liste)

        # Bouton pour lancer la recherche
        if st.form_submit_button('Envoyer'):
            st.write('Voici le top 3 des films recommandés à partir du film sélectionné: ')
        else:
            st.write(" ")

        # Par défaut, aucun film affiché
        if film_select == "":
            st.write("")

        else:
            film_select_scaled = df_bis[df_bis.map(lambda x: isinstance(x, str) and film_select.lower() in x.lower()).any(axis=1)]

            # Extraction de la première ligne de la cinquième colonne (primaryTitle)
            film_select_string = film_select_scaled.iloc[0, 4]

            # Si le titre sélectionné est bien dans le DataFrame, alors récupérer son index
            if film_select_string in df_bis['primaryTitle'].values:
                film_select_index = df_bis[df_bis['primaryTitle'] == film_select_string].index[0]

            # Récupérer les caractéristiques de ce film, qui incluent les données numériques et le vecteur TF-IDF
                film_select_features = X_bis.loc[film_select_index].to_frame().T

            # Appliquer le modèle KNN pour trouver les voisins les plus proches
                distances, indices = knn.kneighbors(film_select_features)

            # Récupérer les titres des films les plus proches
                prop = df.iloc[indices[0]].copy()
                prop['Distance'] = distances[0]


            else:
                st.write("Le film n'a pas été trouvé dans la base de données.")

            # Ordre de l'agencement des colonnes dans le dataframe affiché
            prop = prop[['titre_fr', 'primaryTitle', 'startYear', 'runtimeMinutes', 'averageRating',
                         'genre_facto', 'poster_path', 'tconst', 'region', 'title', 'Genre_trad', 'overview']]

            # Affiche des indices à 1 à 3, sans restriction sur les colonnes
            prop = prop.iloc[1:4, :]

            col1, col2, col3 = st.columns(3)
            with col1:
                for i, j in prop.iloc[0:1].iterrows():
                    base_image = "https://image.tmdb.org/t/p/w500"
                    URL_image = base_image + j['poster_path']
                    base_imdb = "https://www.imdb.com/title/"
                    URL_imdb = base_imdb + j['tconst']
                    regions = [x.strip("'")for x in j['region'].split(", ")]
                    titres = [x.strip("'")for x in j['title'].split(", ")]
                    if 'FR' in regions:
                        indexfr = regions.index('FR')
                        titrefr = titres[indexfr].strip("['[\"").replace('"', "")
                    else:
                        titrefr = titres[0].strip("['[\"").replace('"', "")
                    st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
                    st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; 
                    color: white;">{titrefr}</span> <span style="font-size: 14px; font-weight: normal; 
                    color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)
                    st.write(f"  - 🎭 Genre : {j['Genre_trad']}\n"
                             f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h "
                             f"{int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                             f"  - ⭐ Note moyenne : {j['averageRating']}\n")
                    with st.expander("📜 Lire le résumé"):
                        if pd.isna(j['overview']) or len(j['overview']) > 4998:
                            st.write("Aucun résumé disponible.")
                        else:
                            st.write(translator.translate(j['overview']))

            with col2:
                for i, j in prop.iloc[1:2].iterrows():
                    base_image = "https://image.tmdb.org/t/p/w500"
                    URL_image = base_image + j['poster_path']
                    base_imdb = "https://www.imdb.com/title/"
                    URL_imdb = base_imdb + j['tconst']
                    regions = [x.strip("'")for x in j['region'].split(", ")]
                    titres = [x.strip("'")for x in j['title'].split(", ")]
                    if 'FR' in regions:
                        indexfr = regions.index('FR')
                        titrefr = titres[indexfr].strip("['[\"").replace('"', "")
                    else:
                        titrefr = titres[0].strip("['[\"").replace('"', "")
                    st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
                    st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; 
                    color: white;">{titrefr}</span> <span style="font-size: 14px; font-weight: normal; 
                    color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

                    st.write(f"  - 🎭 Genre : {j['Genre_trad']}\n"
                             f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h "
                             f"{int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                             f"  - ⭐ Note moyenne : {j['averageRating']}\n")
                    with st.expander("📜 Lire le résumé"):
                        if pd.isna(j['overview']) or len(j['overview']) > 4998:
                            st.write("Aucun résumé disponible.")
                        else:
                            st.write(translator.translate(j['overview']))

            with col3:
                for i, j in prop.iloc[2:3].iterrows():
                    base_image = "https://image.tmdb.org/t/p/w500"
                    URL_image = base_image + j['poster_path']
                    base_imdb = "https://www.imdb.com/title/"
                    URL_imdb = base_imdb + j['tconst']
                    regions = [x.strip("'")for x in j['region'].split(", ")]
                    titres = [x.strip("'")for x in j['title'].split(", ")]
                    if 'FR' in regions:
                        indexfr = regions.index('FR')
                        titrefr = titres[indexfr].strip("['[\"").replace('"', "")
                    else:
                        titrefr = titres[0].strip("['[\"").replace('"', "")
                    st.markdown(f"""<a href="{URL_imdb}"><img src="{URL_image}"></a>""", unsafe_allow_html=True)
                    st.markdown(f"""<div style="text-align:center;"><span style="font-size: 20px; font-weight: bold; 
                    color: white;">{titrefr}</span> <span style="font-size: 14px; font-weight: normal; 
                    color: white;">({int(j['startYear'])})</span></div>""", unsafe_allow_html=True)

                    st.write(f"  - 🎭 Genre : {j['Genre_trad']}\n"
                             f"  - ⌛ Durée : {int(j['runtimeMinutes']//60)}h "
                             f"{int(j['runtimeMinutes']-((j['runtimeMinutes']//60)*60))}min\n"
                             f"  - ⭐ Note moyenne : {j['averageRating']}\n")

                    with st.expander("📜 Lire le résumé"):
                        if pd.isna(j['overview']) or len(j['overview']) > 4998:
                            st.write("Aucun résumé disponible.")
                        else:
                            st.write(translator.translate(j['overview']))

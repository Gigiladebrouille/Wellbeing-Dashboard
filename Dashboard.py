import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import scipy.stats as stats
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, recall_score, precision_score, f1_score
from scipy.stats import pearsonr, f_oneway, chi2_contingency


def interpret_correlation(corr_value):
    if corr_value > 0.8:
        return "Très forte corrélation positive", "green"
    elif 0.6 < corr_value <= 0.8:
        return "Forte corrélation positive", "lime"
    elif 0.4 < corr_value <= 0.6:
        return "Corrélation positive modérée", "yellow"
    elif 0.2 < corr_value <= 0.4:
        return "Faible corrélation positive", "orange"
    elif -0.2 < corr_value <= 0.2:
        return "Pas de corrélation", "grey"
    elif -0.4 < corr_value <= -0.2:
        return "Faible corrélation négative", "pink"
    elif -0.6 < corr_value <= -0.4:
        return "Corrélation négative modérée", "purple"
    elif -0.8 < corr_value <= -0.6:
        return "Forte corrélation négative", "red"
    else:
        return "Très forte corrélation négative", "darkred"

st.title('SRE-Optimized Workforce Wellness Dashboard')

# Lire les données à partir du fichier csv
data = pd.read_csv("Dashboard.csv")

data_visual = data.copy()

# Remplacement des valeurs 0 et 1 par "Non" et "Oui" respectivement
data_visual["left"] = data_visual["left"].replace({0: "Non", 1: "Oui"})
data_visual["work_accident"] = data_visual["work_accident"].replace({0: "La chance", 1: "Pas de pôt"})
data_visual["promotion_last_5years"] = data_visual["promotion_last_5years"].replace({False: "Non", True: "Oui"})

# Définir le menu de navigation
menu = ['Accueil','Données Brutes' ,'Statistiques', 'Analyse univariée', 'Analyse bivariée', 'Corrélation', 'Contingence', 'ANOVA', 'Multivariés', 'Régression logistique']
choice = st.sidebar.selectbox('Menu', menu)

# Afficher l'application sélectionnée
if choice == 'Accueil':
    st.title("Bienvenue dans le Dashboard d'Analyse du Bien-être des Employés")
    st.write("""
    ## À propos de ce Dashboard
    Ce dashboard est conçu pour fournir des insights détaillés sur le bien-être des employés au sein de l'organisation. Il utilise des données collectées sur divers aspects du travail et de la vie personnelle des employés pour générer des analyses utiles.

    ### Fonctionnalités
    - **Analyse Univariée et Bivariée**: Pour explorer chaque variable en détail et comprendre les relations entre deux variables.
    - **Corrélation et Contingence**: Pour comprendre les relations complexes entre les variables.
    - **ANOVA et Régression Logistique**: Pour des analyses plus avancées et des prédictions.
    - **Statistiques Descriptives**: Pour obtenir un résumé statistique des données.
    
    ### Comment ça marche
    1. **Naviguez** vers l'onglet de votre choix à partir du menu latéral.
    2. **Interagissez** avec les widgets pour filtrer et trier les données selon vos besoins.
    3. **Consultez** les graphiques et les tableaux pour obtenir des insights.
    4. **Utilisez** les informations pour prendre des décisions éclairées concernant le bien-être des employés.

    Pour commencer, cliquez sur l'un des onglets dans le menu de gauche.
    """)

    st.title('Analyse du bien-être des employés')
    st.write("""
    ## Contexte
    Le bien-être des employés est crucial pour le succès à long terme de toute organisation. Un employé heureux est souvent plus productif, engagé et loyal envers l'entreprise. Ce dashboard vise à aider les départements des ressources humaines et les gestionnaires à avoir une meilleure compréhension du bien-être des employés.

    ### Objectif
    Ce dashboard a pour but d'aider les RH à avoir une visualisation claire et des analyses approfondies sur le bien-être des employés. Il utilise des données sur divers aspects tels que le niveau de satisfaction, l'évaluation de la performance, le nombre de projets, etc., pour fournir des insights utiles.

    ### Base de données
    Ci-dessous, vous avez accès à la base de données de tous nos employés, ainsi qu'aux variables qui seront prises en compte dans vos futures analyses. Chaque onglet du dashboard vous permet d'explorer ces variables de différentes manières pour obtenir des insights précieux.
    """)

    
elif choice == 'Données Brutes':
    st.title('Données Brutes')
    st.write(data_visual)

elif choice == 'Statistiques':
    st.title('Statistiques descriptives des variables numériques')
    st.write("""
    ## À propos de cet onglet
    Cet onglet fournit des statistiques descriptives sur les variables numériques de votre ensemble de données.
    
    ### Caractéristiques
    - **Vue d'ensemble des statistiques**: Affiche des mesures telles que la moyenne, la médiane, l'écart-type, etc.
    - **Statistiques clés**: Met en évidence des statistiques importantes pour chaque variable numérique.
    - **Percentiles**: Affiche les percentiles sélectionnés pour chaque variable numérique.
    
    ### Comment l'utiliser
    1. **Naviguez** vers cet onglet à partir du menu latéral.
    2. **Consultez** les statistiques pour obtenir des insights sur les variables numériques.
    3. **Utilisez** les widgets interactifs pour explorer davantage.
    """)

    # Extraire les colonnes numériques
    numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns

    # Calculer les statistiques descriptives
    stats = data[numeric_cols].describe()

    # Afficher le tableau de statistiques
    st.write("Vue d'ensemble des statistiques :")
    st.dataframe(stats)

    # Choix des percentiles
    percentile_choice = st.selectbox("Choisissez le percentile à afficher :", [25, 50, 75, 90, 95, 99])

    # Mettre en évidence des statistiques clés avec des widgets
    st.write("Statistiques clés :")

    col1, col2, col3 = st.columns(3)

    for col in numeric_cols:
        mean_val = data[col].mean()
        median_val = data[col].median()
        std_val = data[col].std()

        # Identifier les valeurs aberrantes
        outlier_condition = np.abs(data[col] - mean_val) > 2 * std_val
        num_outliers = np.sum(outlier_condition)

        # Utiliser un code couleur pour les valeurs aberrantes
        outlier_color = 'red' if num_outliers > 0 else 'green'

        with col1:
            st.metric(label=f"Moyenne de {col}", value=f"{mean_val:.2f}")
        with col2:
            st.metric(label=f"Médiane de {col}", value=f"{median_val:.2f}")
        with col3:
            st.metric(label=f"Écart-type de {col}", value=f"{std_val:.2f}")

        st.write(f"Nombre de valeurs aberrantes pour {col} : ", num_outliers, f"🚨" if num_outliers > 0 else "✅")

        # Afficher les percentiles
        percentile_val = np.percentile(data[col], percentile_choice)
        st.write(f"Le percentile {percentile_choice} pour {col} est {percentile_val:.2f}")

elif choice == 'Analyse univariée':
    
    st.title('Analyse Univariée')
    st.write("""
    ## À propos de cet onglet
    L'analyse univariée est l'étude statistique d'une seule variable. Elle est utilisée pour obtenir un résumé et des insights sur les données.
    
    ### Caractéristiques
    - **Boxplot**: Pour visualiser la distribution des données.
    - **Statistiques descriptives**: Pour obtenir des mesures telles que la moyenne, la médiane, etc.
    
    ### Comment l'utiliser
    1. **Naviguez** vers cet onglet à partir du menu latéral.
    2. **Sélectionnez** la variable que vous souhaitez analyser.
    3. **Consultez** les graphiques et les statistiques pour obtenir des insights sur la variable.
    """)

    # Sélectionner la variable à afficher
    variable = st.selectbox('Sélectionnez une variable', data.select_dtypes(include=['int64', 'float64', 'object']).columns)

    # Créer des colonnes pour les graphiques
    col1, col2, col3 = st.columns(3)

    # Histogramme
    with col1:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.hist(data[variable], bins=30, color='skyblue', edgecolor='black')
        ax.set_xlabel('Valeur')
        ax.set_ylabel('Fréquence')
        ax.set_title('Histogramme')
        st.pyplot(fig)

    # Boxplot (seulement pour les variables numériques)
    if data[variable].dtype in ['int64', 'float64']:
        with col2:
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.boxplot(x=data[variable], color='green')
            ax.set_title('Boxplot')
            st.pyplot(fig)

    # KDE (seulement pour les variables numériques)
    if data[variable].dtype in ['int64', 'float64']:
        with col3:
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.kdeplot(data[variable], fill=True, color='purple')
            ax.set_title('KDE')
            st.pyplot(fig)

    # Diagramme en barres pour les variables catégorielles
    if data[variable].dtype == 'object':
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.countplot(x=variable, data=data, palette='viridis')
        ax.set_title('Diagramme en barres')
        st.pyplot(fig)

elif choice == 'Analyse bivariée':
    
    st.title('Analyse Bivariée')
    st.write("""
    ## À propos de cet onglet
    L'analyse bivariée est l'étude statistique de deux variables pour comprendre la relation entre elles.
    
    ### Caractéristiques
    - **Graphique dynamique**: Pour visualiser la relation entre les deux variables sélectionnées.
    - **Tableau dynamique**: Pour afficher la moyenne de la deuxième variable en fonction de la première.
    
    ### Comment l'utiliser
    1. **Naviguez** vers cet onglet à partir du menu latéral.
    2. **Sélectionnez** les deux variables que vous souhaitez analyser.
    3. **Consultez** le graphique et le tableau pour comprendre la relation entre les variables.
    """)

    # Extraire les colonnes du dataframe
    all_cols = data.columns

    # Afficher les options de sélection pour les variables
    var1 = st.selectbox("Choisissez la première variable", all_cols)
    var2 = st.selectbox("Choisissez la deuxième variable", all_cols)
    color_var = st.selectbox("Choisissez une variable pour le dégradé de couleurs", all_cols, index=0)

    # Choix du type de graphique
    chart_type = st.selectbox("Choisissez le type de graphique", ['Scatter Plot', 'Line Plot', 'Bar Plot', 'Pie Chart', 'Boxplot groupé', 'Violin Plot'])

    # Ajout d'une option pour filtrer les données
    with st.expander("Filtrer les données"):
        min_val, max_val = st.slider("Filtrer les données en fonction de la deuxième variable", float(data[var2].min()), float(data[var2].max()), [float(data[var2].min()), float(data[var2].max())])
        data_filtered = data[(data[var2] >= min_val) & (data[var2] <= max_val)]

    # Générer le tableau dynamique
    table = pd.pivot_table(data_filtered, values=var2, index=[var1], aggfunc='mean')
    st.write("Tableau dynamique :")
    st.dataframe(table)

# Générer le graphique dynamique
    if chart_type == 'Scatter Plot':
        fig = px.scatter(data_filtered, x=var1, y=var2, color=color_var, 
                     title=f"Scatter Plot de {var1} vs {var2}", 
                     labels={var1: f"{var1} (Axe des X)", var2: f"{var2} (Axe des Y)"})
    elif chart_type == 'Line Plot':
        fig = px.line(data_filtered, x=var1, y=var2, color=color_var, 
                      title=f"Line Plot de {var1} vs {var2}", 
                      labels={var1: f"{var1} (Axe des X)", var2: f"{var2} (Axe des Y)"})
    elif chart_type == 'Bar Plot':
        fig = px.bar(data_filtered, x=var1, y=var2, color=color_var, 
                     title=f"Bar Plot de {var1} vs {var2}", 
                     labels={var1: f"{var1} (Axe des X)", var2: f"{var2} (Axe des Y)"})
    elif chart_type == 'Pie Chart':
        fig = px.pie(data_filtered, names=var1, values=var2, color=color_var, 
                     title=f"Pie Chart de {var1} vs {var2}")
    elif chart_type == 'Boxplot groupé':
        fig = px.box(data_filtered, x=var1, y=var2, color=color_var, 
                     title=f"Boxplot groupé de {var1} vs {var2}", 
                     labels={var1: f"{var1} (Axe des X)", var2: f"{var2} (Axe des Y)"})
    elif chart_type == 'Violin Plot':
        fig = px.violin(data_filtered, x=var1, y=var2, color=color_var, 
                    title=f"Violin Plot de {var1} vs {var2}", 
                    labels={var1: f"{var1} (Axe des X)", var2: f"{var2} (Axe des Y)"})

    st.write(f"{chart_type} :")
    st.plotly_chart(fig)

elif choice == 'Corrélation':
    
    st.title('Analyse de Corrélation')
    st.write("""
    ## À propos de cet onglet
    L'analyse de corrélation est utilisée pour évaluer la force et la direction de la relation linéaire entre deux variables quantitatives.
    
    ### Caractéristiques
    - **Matrice de corrélation**: Affiche les coefficients de corrélation entre les variables.
    - **Heatmap**: Pour une représentation visuelle de la matrice.
    
    ### Comment l'utiliser
    1. **Naviguez** vers cet onglet à partir du menu latéral.
    2. **Consultez** la matrice de corrélation et la heatmap pour comprendre les relations entre les variables.
    """)
    
    # Extraire les colonnes numériques du dataframe
    numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns

    # Afficher les options de sélection pour les variables
    var1 = st.selectbox("Choisissez la première variable", numeric_cols)
    var2 = st.selectbox("Choisissez la deuxième variable", numeric_cols)

    # Choix du type de corrélation
    corr_type = st.selectbox("Type de corrélation", ['Pearson', 'Spearman', 'Kendall'])

    # Ajout d'une option pour filtrer les données
    with st.expander("Filtrer les données"):
        min_val1, max_val1 = st.slider(f"Filtrer {var1}", float(data[var1].min()), float(data[var1].max()), [float(data[var1].min()), float(data[var1].max())])
        min_val2, max_val2 = st.slider(f"Filtrer {var2}", float(data[var2].min()), float(data[var2].max()), [float(data[var2].min()), float(data[var2].max())])
        data_filtered = data[(data[var1] >= min_val1) & (data[var1] <= max_val1) & (data[var2] >= min_val2) & (data[var2] <= max_val2)]

    # Calculer la matrice de corrélation
    if corr_type == 'Pearson':
        corr = data_filtered[[var1, var2]].corr(method='pearson')
    elif corr_type == 'Spearman':
        corr = data_filtered[[var1, var2]].corr(method='spearman')
    elif corr_type == 'Kendall':
        corr = data_filtered[[var1, var2]].corr(method='kendall')

    # Créer le masque pour éviter les redondances
    mask = np.ones_like(corr, dtype=bool)
    mask[np.tril_indices_from(mask)] = False

    # Afficher la heatmap avec le masque
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, mask=mask, annot=True, ax=ax)
    plt.title(f'Matrice de Corrélation ({corr_type}) entre {var1} et {var2}')
    plt.xlabel(var1)
    plt.ylabel(var2)
    st.pyplot(fig)

    # Interprétation du coefficient de corrélation
    coeff = corr.loc[var1, var2]
    if coeff > 0:
        direction = 'positive'
    else:
        direction = 'négative'

    if abs(coeff) < 0.3:
        strength = 'faible'
    elif abs(coeff) < 0.7:
        strength = 'modérée'
    else:
        strength = 'forte'

    st.write(f"### Interprétation du Coefficient de Corrélation")
    st.write(f"La corrélation {direction} entre {var1} et {var2} est {strength} (Coefficient = {coeff:.2f}).")

elif choice == 'Contingence':
    
    st.title('Table de Contingence')
    st.write("""
    ## À propos de cet onglet
    Une table de contingence est un outil statistique utilisé pour analyser les relations entre deux variables catégorielles.
    
    ### Caractéristiques
    - **Table de contingence**: Affiche la distribution croisée des données entre deux variables.
    
    ### Comment l'utiliser
    1. **Naviguez** vers cet onglet à partir du menu latéral.
    2. **Consultez** la table pour comprendre la relation entre les deux variables catégorielles sélectionnées.
    """)
    
    # Extraire les colonnes catégorielles du dataframe
    categorical_cols = data.select_dtypes(include=['object', 'bool']).columns

    # Afficher les options de sélection pour les variables
    var1 = st.selectbox("Choisissez la première variable", categorical_cols)
    var2 = st.selectbox("Choisissez la deuxième variable", categorical_cols)

    # Calculer la table de contingence
    table = pd.crosstab(data[var1], data[var2], margins=True)
    
    st.subheader('Table de contingence')
    # Afficher la table de contingence
    st.write(table)

    # Test du chi-carré
    chi2, p, dof, expected = chi2_contingency(table)
    st.subheader('Test du chi-carré')
    st.write(f"Valeur du chi-carré : {chi2}")
    st.write(f"Valeur-p : {p}")
    st.write(f"Nombre de degrés de liberté : {dof}")

    # Interprétation du test du chi-carré
    if p < 0.05:
        st.write("🔴 Les variables sont dépendantes (p < 0.05)")
    else:
        st.write("🟢 Les variables sont indépendantes (p >= 0.05)")

    # Heatmap de la table de contingence
    st.subheader('Heatmap de la table de contingence')
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(table, annot=True, cmap="coolwarm", ax=ax)
    plt.title('Heatmap de la table de contingence')
    plt.xlabel(var1)
    plt.ylabel(var2)
    st.pyplot(fig)

elif choice == 'ANOVA':
    
    st.title('Analyse de la variance (ANOVA)')
    st.write("""
    ## À propos de cet onglet
    L'Analyse de la Variance (ANOVA) est utilisée pour analyser les différences entre les groupes de données. 
    Elle est particulièrement utile pour comparer les moyennes de trois groupes ou plus.
    
    ### Caractéristiques
    - **Tableau ANOVA**: Affiche les résultats de l'ANOVA, y compris la valeur F et la valeur p.
    
    ### Comment l'utiliser
    1. **Naviguez** vers cet onglet à partir du menu latéral.
    2. **Consultez** le tableau ANOVA pour évaluer si les moyennes de différents groupes sont statistiquement différentes.
    """)

    # Extraire les colonnes numériques du dataframe
    numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = data.select_dtypes(include=['object', 'bool']).columns.tolist()

    # Widgets pour la sélection des variables
    dependent_var = st.selectbox("Choisissez la variable dépendante", numeric_cols)
    independent_var = st.selectbox("Choisissez la variable indépendante", categorical_cols)

    # Effectuer le test ANOVA
    if st.button("Effectuer le test ANOVA"):
        import scipy.stats as stats

        # Préparation des données
        categories = data[independent_var].unique()
        data_arrays = [data[dependent_var][data[independent_var] == cat] for cat in categories]

        # Effectuer le test ANOVA
        f_val, p_val = stats.f_oneway(*data_arrays)

        # Afficher les résultats
        st.write(f"Valeur F : {f_val}")
        st.write(f"Valeur p : {p_val}")

        # Interprétation
        if p_val < 0.05:
            st.write("🔴 Les moyennes des groupes sont significativement différentes (p < 0.05)")
        else:
            st.write("🟢 Les moyennes des groupes ne sont pas significativement différentes (p >= 0.05)")

        fig, ax = plt.subplots(figsize=(12, 6))  # Créer un objet figure et axes
        sns.boxplot(x=independent_var, y=dependent_var, data=data, ax=ax)  # Utiliser l'objet axes
        plt.title('Boxplot des groupes')
        st.pyplot(fig)  # Passer l'objet figure à st.pyplot()

elif choice == 'Multivariés':
    
    st.title('Analyse Multivariée')
    st.write("""
    ## À propos de cet onglet
    Cet onglet fournit une analyse multivariée des données, en se concentrant sur les relations entre plusieurs variables à la fois.
    
    ### Caractéristiques
    - **Matrice de corrélation**: Pour visualiser les relations entre les variables numériques.
    - **Heatmap**: Pour une représentation visuelle de la matrice de corrélation.
    
    ### Comment l'utiliser
    1. **Naviguez** vers cet onglet à partir du menu latéral.
    2. **Consultez** la matrice de corrélation et la heatmap pour comprendre les relations entre les variables.
    3. **Utilisez** ces informations pour des analyses plus approfondies ou pour améliorer vos modèles de machine learning.
    """)

    # Transformer la colonne promotion_last_5years en objet
    data['promotion_last_5years'] = data['promotion_last_5years'].astype('object')

    # Sélectionner les colonnes numériques
    numerical_columns = data.select_dtypes(include='number').columns.tolist()
    if 'id_colab' in numerical_columns:
        numerical_columns.remove('id_colab')

    # Widget pour sélectionner les colonnes
    selected_columns = st.multiselect("Sélectionnez les variables numériques", numerical_columns, default=numerical_columns)

    # Widget pour sélectionner le type de corrélation
    corr_type = st.selectbox("Sélectionnez le type de corrélation", ["Pearson", "Spearman"])

    # Calculer la matrice de corrélation
    if corr_type == "Pearson":
        corr_matrix = data[selected_columns].corr(method='pearson')
    else:
        corr_matrix = data[selected_columns].corr(method='spearman')

    # Affichage Matrice Correlation
        st.write(corr_matrix.round(4))

        # Menu déroulant pour la sélection des variables
        var1 = st.selectbox("Choisissez la première variable pour l'interprétation", corr_matrix.columns)
        var2 = st.selectbox("Choisissez la deuxième variable pour l'interprétation", corr_matrix.columns)

        if var1 != var2:
            corr_value = corr_matrix.loc[var1, var2]
            interpretation, color = interpret_correlation(corr_value)
            st.markdown(f"La corrélation entre **{var1}** et **{var2}** est : <span style='color:{color};'>{interpretation}</span>", unsafe_allow_html=True)
        else:
            st.write("Veuillez sélectionner deux variables différentes pour l'interprétation.")


        st.subheader('Heatmap de la corrélation de cette matrice.')
        fig, ax = plt.subplots(figsize=(10, 8))  # Taille personnalisée
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
        plt.title('Heatmap de Corrélation')
        st.pyplot(fig)
    
elif choice == 'Régression logistique':
    
    st.title('Régression logistique')
    st.write("""
    ## À propos de cet onglet
    Dans cet onglet, nous utilisons un modèle de régression logistique pour prédire si un employé va quitter l'entreprise ou non.
    
    ### Caractéristiques
    - **Matrice de confusion**: Pour évaluer la performance du modèle.
    - **Rapport de classification**: Pour obtenir des métriques clés comme la précision, le rappel, etc.
    - **Prédiction pour chaque employé**: Une table montrant les prédictions du modèle pour chaque employé.
    
    ### Comment l'utiliser
    1. **Naviguez** vers cet onglet à partir du menu latéral.
    2. **Consultez** les métriques pour évaluer la performance du modèle.
    3. **Analysez** la table de prédiction pour prendre des décisions basées sur les données.
    """)

    # Sélectionner les colonnes pertinentes pour la régression logistique
    df = data[['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company', 'work_accident', 'promotion_last_5years', 'left']]
    
    # Convertir la variable 'promotion_last_5years' en entier
    df['promotion_last_5years'] = pd.to_numeric(df['promotion_last_5years'], errors='coerce')
    
    # Remplacer les valeurs booléennes de la colonne 'left' par des entiers (0 ou 1)
    df['left'] = df['left'].apply(lambda x: 1 if x else 0)

    # Séparer les données en variables indépendantes (X) et dépendante (y)
    X = df.drop('left', axis=1)
    y = df['left']

    # Créer un modèle de régression logistique avec un paramètre de régularisation
    model = LogisticRegression(C=0.95)

    # Entraîner le modèle sur les données
    model.fit(X, y)

    # Prédire les tendances pour les données de test
    y_pred = model.predict(X)

    # Afficher la matrice de confusion avec un code couleur
    st.subheader('Matrice de confusion')
    cm = confusion_matrix(y, y_pred)
    fig, ax = plt.subplots(figsize=(5, 5))
    sns.heatmap(cm, annot=True, cmap="coolwarm", fmt="d", cbar=False, ax=ax)
    st.pyplot(fig)


    # Afficher le rapport de classification
    st.subheader('Rapport de classification')
    report = classification_report(y, y_pred)
    st.text(report)

    # Ajouter une interactivité pour l'interprétation des résultats
    selected_metric = st.selectbox("Choisissez une métrique pour l'interprétation", ["Précision", "Rappel", "Score F1"])
    if selected_metric == "Précision":
        st.write(f"La précision du modèle est de {precision_score(y, y_pred):.2f}")
    elif selected_metric == "Rappel":
        st.write(f"Le rappel du modèle est de {recall_score(y, y_pred):.2f}")
    elif selected_metric == "Score F1":
        st.write(f"Le score F1 du modèle est de {f1_score(y, y_pred):.2f}")

    # Afficher la prédiction de tendance pour chaque employé
    st.subheader('Prédiction de tendance pour chaque employé')
    pred_df = pd.DataFrame({'Tendance réelle': y, 'Tendance prévue': y_pred})
    st.write(pred_df)

    # Calculer les métriques
    recall = recall_score(y, y_pred)
    precision = precision_score(y, y_pred)
    f1 = f1_score(y, y_pred)
    
    # Afficher les métriques
    st.subheader('Métriques du modèle')
    st.write(f"Le rappel du modèle est de {recall:.2f}")
    st.write(f"La précision du modèle est de {precision:.2f}")
    st.write(f"Le score F1 du modèle est de {f1:.2f}")
    
    # Interprétation logique
    st.subheader('Interprétation du modèle')
    if recall > 0.8 and precision > 0.8:
        st.success("Le modèle est très performant.")
    elif recall > 0.8:
        st.warning("Le modèle a un bon rappel mais une précision faible. Il pourrait y avoir des faux positifs.")
    elif precision > 0.8:
        st.warning("Le modèle a une bonne précision mais un rappel faible. Il pourrait y avoir des faux négatifs.")
    else:
        st.error("Le modèle a besoin d'être amélioré.")
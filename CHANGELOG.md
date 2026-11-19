# Journal des modifications

Numérotation majeure.mineure.correctif. Une version majeure peut changer le format des données ; l’application migre alors automatiquement les anciennes données au démarrage.

## 2.8.1 (19/11/2026)

- Publication sous licence GNU GPL version 3 ou ultérieure (fichier LICENSE).
- Exemple de résultat LCWO de l’Analyse remplacé par un exemple inventé ; indicatif d’exemple fictif (F4XXX).
- Exports : téléchargement direct par le navigateur, sans dépendance à un service extérieur.

## 2.8.0 (18/11/2026)

- Tirage « Derniers caractères plus fréquents » adouci : le dernier caractère revient 2,5 fois plus souvent, l’avant-dernier 1,7 fois et celui d’avant 1,3 fois.
- Nouvel onglet Manipulateur : pioche (barre Espace, touche au choix, souris, écran tactile) ou manipulateur iambique à deux palettes (modes A et B).
- Moteur de reconnaissance des caractères envoyés, qui suit votre vitesse, avec exercices d’émission (caractères, groupes, mots, votre indicatif) et mesure de la régularité.
- Deux jeux au manipulateur : Écho et Pluie de lettres.
- Suivi : chaque séance peut être supprimée (deux clics).
- Les caractères à revoir se réécoutent cinq fois de suite, avec des silences plus courts.

## 2.7.0 (16/11/2026)

- Nouvelle page d’accueil : choix de l’exercice en tuiles de même taille, son et conditions de réception.
- Le choix d’un exercice ouvre la page d’exercice : 1. leçon, 2. options, 3. écoute et copie.
- Nouvel exercice Écoute SWL (à partir de la leçon 40) : un QSO différent à chaque écoute entre deux stations, avec les abréviations HF usuelles ; on relève les indicatifs, les rapports et, si on le souhaite, prénom, QTH et puissance.
- Copie en police à chasse fixe (IBM Plex Mono) : tous les groupes de même longueur ont la même largeur.

## 2.6.0 (15/11/2026)

- Morse machine : plus de son à la bonne réponse, seul le bip d’erreur reste.
- Morse machine : liste des caractères de la leçon avec un point vert et le nombre de réussites du premier coup ; « Remettre à zéro » la vide aussi.

## 2.5.0 (15/11/2026)

- L’application s’appelle désormais Tympan, avec son icône (onglet du navigateur, écran d’accueil et barre supérieure).
- Les sauvegardes faites sous l’ancien nom « Entraînement Koch » restent restaurables.

## 2.4.0 (15/11/2026)

- Page Entraînement réorganisée en étapes : 1. leçon Koch, 2. exercice et ses options, 3. son, 4. écoute et copie.
- Un seul endroit pour choisir l’exercice : Leçon Koch, Chaque caractère deux fois, Caractères choisis, Indicatifs, Texte en clair, Révision, Morse machine. La leçon Koch propose un tirage aléatoire ou avec les derniers caractères plus fréquents.
- Tous les exercices se limitent aux caractères de la leçon choisie : caractères cochés, indicatifs (à partir de la leçon 23), mots et textes en clair, écoutes ciblées.
- Suivi : la précision moyenne du jour s’affiche du minimum de la période à 100 %, avec les jalons de passage de leçon.

## 2.3.0 (15/11/2026)

- « Lancer l’écoute » rejoue toujours la même écoute tant qu’elle n’est pas corrigée ; pendant la lecture, le bouton la recommence du début. Un bouton « Arrêter » distinct apparaît pendant la lecture.
- Délai de 2 secondes avant chaque écoute, avec compte à rebours (aussi avant le premier caractère de la révision et de la Morse machine).
- Sortie audio maintenue éveillée par un signal inaudible, pour que le premier caractère ne soit plus coupé dans les casques (option dans Paramètres, activée par défaut).
- Les boutons proposés après une écoute, et l’écoute ciblée de l’Analyse, préparent l’écoute et ramènent à la zone d’écoute sans la lancer.

## 2.2.0 (15/11/2026)

- Résultat : le taux d’erreur s’affiche à côté de la précision.
- Copie : avant la validation, une ligne dont un groupe n’a pas le bon nombre de caractères passe en rouge ; la validation demande alors une confirmation.
- Tirage des caractères en leçon Koch : aléatoire, trois derniers caractères trois fois plus fréquents, ou chaque caractère deux fois, mélangé.
- Après une écoute : refaire la même écoute, nouvelle écoute, nouvelle écoute pondérée, révision des seuls caractères manqués.
- L’analyse détaillée (Pareto et tableau) s’affiche directement sous le résultat.
- Morse machine : un caractère de la leçon est joué, vous tapez la touche ; un son confirme la bonne réponse, un bip signale l’erreur. Les séances de 5 caractères ou plus sont enregistrées dans le suivi.

## 2.1.1 (14/11/2026)

- Mode révision : les répétitions sont jouées à la vitesse caractère avec un espacement standard, sans l’allongement de la vitesse réelle.

## 2.1.0 (14/11/2026)

- Mode révision : chaque caractère de la leçon Koch s’affiche en grand et est joué plusieurs fois (5 par défaut), puis l’application passe au suivant. Ordre, nombre d’écoutes, pause et lecture en boucle réglables.
- Aucune représentation écrite du code Morse n’apparaît plus, ni à l’écran ni dans le code source ; un caractère manqué est marqué par ∅.

## 2.0.0 (11/11/2026)

- Style graphique « Nuit » et navigation en quatre sections : Entraînement, Analyse, Suivi, Paramètres.
- Nouveaux contenus : caractères choisis, indicatifs, texte en clair (proverbes et poèmes du domaine public).
- Conditions de réception : bruit de fond filtré et QSB (évanouissement et variation de fréquence).
- Bouton « Nouvelle écoute » ciblée sur les caractères prioritaires.
- Analyse de Pareto des caractères manqués, sur vos écoutes ou sur un résultat LCWO collé.
- Suivi jour par jour : calendrier, séries, courbes de progression, import de l’historique LCWO (JSON).
- Page Paramètres : indicatif et locator affichés dans la barre, seuil, volume, sauvegarde et restauration.
- Correction par réalignement des groupes : un groupe manqué n’a plus besoin d’une ligne vide.
- Format des données : 2 (les réglages de la version 1.0.0 sont repris).

## 1.0.0 (11/11/2026)

- Première version : leçons Koch, réglages d’écoute, copie par groupes de 5 et correction.

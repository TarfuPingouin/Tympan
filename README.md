# Tympan 2.8.1

Tympan est une application d’entraînement à la lecture au son du Morse (méthode Koch), en un seul fichier : `index.html`.
Conformément à la méthode, le code n’est jamais représenté par écrit : on apprend chaque caractère par son son uniquement.

## Utilisation en local

Ouvrez `index.html` dans votre navigateur (double-clic). Rien à installer.

Les données (réglages, indicatif, historique) sont stockées dans le navigateur, séparément pour chaque adresse : la version ouverte en local et celle d’un serveur ne partagent pas leurs données. Pour passer de l’une à l’autre, utilisez Paramètres > Exporter toutes les données, puis Restaurer une sauvegarde.

## Utilisation sur un serveur

1. Copiez `index.html` dans le dossier servi (par exemple `/var/www/tympan`), en lecture seule :
   `chown root:root index.html && chmod 444 index.html`
2. Nginx : reprenez `deploiement/nginx-tympan.conf` (adaptez le nom de domaine et les certificats).
   Apache : copiez `deploiement/.htaccess` à côté de `index.html` (module `mod_headers` requis).
3. Après chaque mise à jour de `index.html`, lancez `python3 deploiement/maj-empreinte-csp.py` puis rechargez le serveur.

## Pourquoi le serveur ne peut pas être attaqué depuis l’application

- Le serveur ne fait que servir un fichier statique : aucun PHP, CGI, base de données ni point d’envoi. L’application ne transmet jamais rien au serveur ; tout se passe dans le navigateur.
- Les configurations n’autorisent que les requêtes GET et HEAD sur `index.html`, désactivent l’exécution de scripts côté serveur et le listage des dossiers, et renvoient 404 pour tout le reste.
- La politique de sécurité du contenu (CSP) n’autorise que le script intégré, identifié par son empreinte SHA-256, ainsi que les polices IBM Plex (Sans, Sans Condensed et Mono) de Google Fonts. Toute connexion réseau sortante, tout formulaire et tout encadrement de la page sont interdits.
- Les fichiers importés (export LCWO, sauvegardes) sont lus dans le navigateur, limités à 5 Mo, vérifiés champ par champ et affichés uniquement comme du texte : ils ne peuvent pas injecter de code.

Si vous ne voulez dépendre d’aucun service externe, hébergez les polices IBM Plex vous-même, puis remplacez les adresses Google Fonts dans `index.html` et dans la CSP.

## Icône

Le dossier `icone` contient l’icône en SVG et en PNG 180 × 180, si vous voulez la réutiliser ailleurs. Elle est déjà intégrée dans `index.html` : rien à copier sur le serveur.

## Versions

Le numéro de version est affiché dans le pied de page et dans Paramètres > Version. Voir `CHANGELOG.md`.

## Licence

Tympan est un logiciel libre, publié sous licence GNU General Public License version 3 ou ultérieure (GPL-3.0-or-later). Vous pouvez l’utiliser, l’étudier, le modifier et le redistribuer ; toute version modifiée que vous distribuez doit rester sous la même licence, avec son code source. Le texte complet est dans le fichier `LICENSE`.

Les proverbes et extraits de poèmes intégrés sont dans le domaine public. Les polices IBM Plex, chargées depuis Google Fonts, sont distribuées sous SIL Open Font License.

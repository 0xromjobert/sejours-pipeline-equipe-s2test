# Contribuer à sejours-pipeline-equipe

Les règles de l'équipe. Elles s'appliquent à tout le monde, formateur compris.

## Le cycle

1. Prenez un ticket (onglet **Issues**) et assignez-le-vous (**Assignees**).
2. Partez de `main` à jour : `git switch main` puis `git pull`.
3. Créez votre branche : `git switch -c DE-1xx-sujet-court`.
4. Commitez, poussez, ouvrez la pull request.
5. Attendez la CI verte, relisez vos propres **Files changed**, puis demandez une revue.
6. Après la fusion : `git switch main`, `git pull`, `git branch -d DE-1xx-sujet-court`.

## Les noms

| Élément | Règle | Exemple |
| --- | --- | --- |
| Branche | numéro du ticket + sujet, minuscules et tirets | `DE-102-age-max` |
| Commit | préfixe de type + ce que fait le commit | `feat: refuser un âge supérieur à 120 ans` |
| Pull request | numéro du ticket + titre clair | `DE-102 · Refuser un âge supérieur à 120 ans` |

Préfixes : `feat` (fonctionnalité), `fix` (correction), `docs` (documentation), `refactor` (réécrire sans changer le résultat), `test` (tests), `ci` (intégration continue).

## La pull request

- Remplir le modèle : **Quoi**, **Pourquoi**, **Comment vérifier**.
- Écrire `Closes #n` (n = le numéro de l'issue) : l'issue se ferme toute seule à la fusion.
- Le relecteur vient d'**un autre binôme** que le vôtre.
- `main` est protégée : 1 approbation et une CI verte pour fusionner.

## Jamais dans le dépôt

Aucun secret (`.env`), aucune donnée (`data/`), aucune base (`*.duckdb`). Même fictifs.

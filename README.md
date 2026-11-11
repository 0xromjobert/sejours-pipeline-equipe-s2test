# sejours-pipeline

Lit des séjours hospitaliers dans un CSV, valide chaque ligne, charge les séjours valides dans DuckDB.
Données **fictives** uniquement.

```
uv sync
uv run pytest
cp .env.example .env
uv run --env-file .env sejours-pipeline
```

## Lancer le pipeline

1. Copier `.env.example` en `.env` et indiquer le chemin du CSV.
2. `uv run --env-file .env sejours-pipeline`
3. Le log indique le nombre de séjours chargés et rejetés.

## Les règles de validation

- `id` et `service` ne sont pas vides
- `entree` et `sortie` sont des dates, la sortie n'est pas avant l'entrée
- `age` est positif

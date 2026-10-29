# Cap Pro : ton cap vers le métier (application élèves)

Étape 2 : version locale avec comptes, fiches de cours, quiz et suivi des scores.

## Lancer

```
pip install -r requirements.txt
streamlit run app.py
```

Ouvre l'adresse affichée (souvent http://localhost:8501), crée un compte et teste.

## Fichiers

- `app.py` : l'interface (connexion, cours, quiz, progrès)
- `db.py` : comptes et scores (SQLite local, remplacé par Supabase plus tard)
- `content.py` : les cours et quiz par filière (électricité complète, autres filières en exemples)

## Prochaines étapes

3. Assistant IA (Groq) et aide aux exposés
4. Orientation
5. Supabase + dépôt GitHub + déploiement sur Streamlit Cloud
6. Rôles admin / super_admin et paiement par niveau

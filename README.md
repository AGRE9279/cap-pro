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

## Assistant IA (étape 3)

L'assistant et l'aide aux exposés utilisent Groq. Il faut une clé API Groq (celle d'AcademieIA convient).

- Sur Streamlit Cloud : App > Settings > Secrets, puis ajouter :
  ```
  GROQ_API_KEY = "ta_cle_groq"
  ```
- En local : définir la variable d'environnement `GROQ_API_KEY`.
- Facultatif : `GROQ_MODEL` (autre modèle Groq) et `DAILY_AI_LIMIT` (20 questions par élève et par jour par défaut).

Sans clé, l'appli fonctionne : seuls l'assistant et les exposés affichent un message d'attente.

## Prochaines étapes

4. Orientation
5. Supabase + dépôt GitHub + déploiement sur Streamlit Cloud
6. Rôles admin / super_admin et paiement par niveau

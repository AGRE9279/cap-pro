"""Cap Pro : application pour élèves de l'enseignement technique et professionnel.

Lancer :  streamlit run app.py
"""
import streamlit as st

import ai
import content
import db

st.set_page_config(page_title="Cap Pro", page_icon="🧭", layout="centered")
db.init()

NOMS_FILIERES = content.FILIERES  # {"1": "Electricite / Electrotechnique", ...}


# ---------- Connexion / inscription ----------
def page_auth():
    st.title("🧭 Cap Pro")
    st.caption("Ton cap vers le métier : cours, quiz et aide pour les élèves de l'enseignement technique et professionnel.")
    tab_in, tab_up = st.tabs(["Se connecter", "Créer un compte"])

    with tab_in:
        with st.form("login"):
            u = st.text_input("Nom d'utilisateur")
            p = st.text_input("Mot de passe", type="password")
            ok = st.form_submit_button("Se connecter")
        if ok:
            user = db.check_login(u, p)
            if user:
                st.session_state.user = user
                st.rerun()
            else:
                st.error("Nom d'utilisateur ou mot de passe incorrect.")

    with tab_up:
        with st.form("signup"):
            nom = st.text_input("Ton nom et prénom")
            u = st.text_input("Choisis un nom d'utilisateur")
            fil = st.selectbox("Ta filière", list(NOMS_FILIERES), format_func=NOMS_FILIERES.get)
            p1 = st.text_input("Mot de passe (6 caractères minimum)", type="password")
            p2 = st.text_input("Répète le mot de passe", type="password")
            ok = st.form_submit_button("Créer mon compte")
        if ok:
            if not (nom.strip() and u.strip()):
                st.error("Écris ton nom et choisis un nom d'utilisateur.")
            elif len(p1) < 6:
                st.error("Le mot de passe doit avoir au moins 6 caractères.")
            elif p1 != p2:
                st.error("Les deux mots de passe ne sont pas identiques.")
            else:
                user = db.create_user(u, nom, p1, fil)
                if user:
                    st.session_state.user = user
                    st.rerun()
                else:
                    st.error("Ce nom d'utilisateur est déjà pris.")


# ---------- Pages ----------
def choisir_filiere(cle):
    ids = list(NOMS_FILIERES)
    defaut = st.session_state.user.get("filiere") or ids[0]
    index = ids.index(defaut) if defaut in ids else 0
    return st.selectbox("Filière", ids, index=index, format_func=NOMS_FILIERES.get, key=f"fil_{cle}")


def page_cours():
    st.header("📚 Cours et fiches")
    f = choisir_filiere("cours")
    fiches = content.FICHES.get(f, [])
    if not fiches:
        st.info("Pas encore de fiches pour cette filière.")
        return
    for titre, corps in fiches:
        with st.expander(titre):
            st.text(corps)


def page_quiz():
    st.header("📝 Quiz")
    f = choisir_filiere("quiz")
    quiz = content.QUIZ.get(f, [])
    if not quiz:
        st.info("Pas encore de quiz pour cette filière.")
        return

    with st.form(f"quiz_{f}"):
        reponses = []
        for i, (q, choix, _, _) in enumerate(quiz):
            reponses.append(st.radio(f"{i + 1}. {q}", choix, index=None, key=f"q_{f}_{i}"))
        envoye = st.form_submit_button("Valider mes réponses")

    if not envoye:
        return
    if any(r is None for r in reponses):
        st.warning("Réponds à toutes les questions avant de valider.")
        return

    score = 0
    for i, (q, choix, bonne, expl) in enumerate(quiz):
        juste = choix.index(reponses[i]) == bonne
        score += juste
        if juste:
            st.success(f"{i + 1}. Bonne réponse. {expl}")
        else:
            st.error(f"{i + 1}. Pas tout à fait. Bonne réponse : {choix[bonne]}. {expl}")
    db.save_score(st.session_state.user["id"], f, score, len(quiz))
    st.subheader(f"Résultat : {score} / {len(quiz)}")


def page_progres():
    st.header("📈 Mon progrès")
    scores = db.get_scores(st.session_state.user["id"])
    if not scores:
        st.info("Tu n'as pas encore passé de quiz.")
        return
    for s in scores:
        nom = NOMS_FILIERES.get(s["filiere"], s["filiere"])
        st.write(f"**{nom}** : {s['score']} / {s['total']} ({s['created_at'][:10]})")


def page_chat(mode, titre, intro):
    """Discussion avec l'IA (mode 'assistant' ou 'expose')."""
    user = st.session_state.user
    st.header(titre)
    st.caption(intro)

    cle = f"chat_{mode}"
    historique = st.session_state.setdefault(cle, [])
    if historique and st.button("Nouvelle conversation", key=f"reset_{mode}"):
        st.session_state[cle] = []
        st.rerun()

    for m in historique:
        with st.chat_message(m["role"]):
            st.write(m["content"])

    question = st.chat_input("Écris ta question ici...")
    if not question:
        return

    if db.count_ai_today(user["id"]) >= ai.daily_limit():
        st.warning("Tu as atteint la limite de questions pour aujourd'hui. Reviens demain !")
        return

    historique.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)
    with st.chat_message("assistant"):
        with st.spinner("Je réfléchis..."):
            reponse, erreur = ai.ask(mode, historique, NOMS_FILIERES.get(user.get("filiere"), ""))
        if erreur:
            st.error(erreur)
            historique.pop()
        else:
            st.write(reponse)
            historique.append({"role": "assistant", "content": reponse})
            db.add_ai_usage(user["id"])


def page_bientot(titre, texte):
    st.header(titre)
    st.info(texte)


# ---------- Application ----------
def main():
    if "user" not in st.session_state:
        page_auth()
        return

    user = st.session_state.user
    with st.sidebar:
        st.write(f"Bonjour **{user['nom']}**")
        page = st.radio(
            "Menu",
            ["Cours", "Quiz", "Assistant IA", "Exposés", "Orientation", "Mon progrès"],
        )
        if st.button("Se déconnecter"):
            del st.session_state["user"]
            st.rerun()

    if page == "Cours":
        page_cours()
    elif page == "Quiz":
        page_quiz()
    elif page == "Assistant IA":
        page_chat("assistant", "🤖 Assistant IA", "Pose une question sur ton cours ou ton métier.")
    elif page == "Exposés":
        page_chat("expose", "🗂️ Aide aux exposés", "Je t'aide à trouver ton sujet et à construire ton plan.")
    elif page == "Orientation":
        page_bientot("🧭 Orientation", "Bientôt disponible.")
    else:
        page_progres()


main()

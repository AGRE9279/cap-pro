"""Contenu du bot : filieres, fiches de cours, quiz, orientation.

IMPORTANT : ce fichier est un MODELE. Remplace et complete le contenu avec
les vrais programmes de tes eleves (programme officiel, notes de profs).
Ne publie pas d'informations d'orientation (concours, dates, frais) sans les
avoir verifiees aupres du Ministere de l'Enseignement Technique, de la
Formation Professionnelle et de l'Apprentissage (METFPA) ou de l'etablissement.
"""

FILIERES = {
    "1": "Electricite / Electrotechnique",
    "2": "Comptabilite et gestion",
    "3": "Informatique",
    "4": "Couture / Stylisme",
    "5": "Mecanique automobile",
}

# Fiches de cours : une fiche courte = un message WhatsApp lisible
FICHES = {
    "1": [
        (
            "Loi d'Ohm",
            "La loi d'Ohm relie tension, courant et résistance.\n\n"
            "U = R × I\n"
            "U en volts (V), R en ohms (Ω), I en ampères (A).\n\n"
            "On peut aussi écrire : I = U ÷ R et R = U ÷ I.\n\n"
            "Exemple : R = 100 Ω et I = 0,5 A donne U = 50 V.",
        ),
        (
            "Puissance électrique",
            "P = U × I\n"
            "P en watts (W).\n\n"
            "Exemple : une lampe sous 220 V qui consomme 0,5 A "
            "a une puissance de 110 W.\n\n"
            "1 kW = 1000 W.",
        ),
        (
            "Énergie électrique et kWh",
            "L'énergie consommée dépend de la puissance et de la durée.\n\n"
            "W = P × t\n"
            "Avec P en kW et t en heures, W s'exprime en kWh (c'est ce que "
            "compte le compteur).\n\n"
            "Exemple : un appareil de 1000 W (1 kW) qui fonctionne 3 h "
            "consomme 3 kWh.",
        ),
        (
            "Circuit en série",
            "Les composants sont placés l'un après l'autre, sur une seule boucle.\n\n"
            "• Le courant est le même partout.\n"
            "• Les tensions s'additionnent.\n"
            "• Les résistances s'additionnent : Rt = R1 + R2.\n\n"
            "Exemple : R1 = 10 Ω et R2 = 20 Ω donnent Rt = 30 Ω.\n"
            "Si un composant est coupé, tout le circuit s'arrête.",
        ),
        (
            "Circuit en parallèle",
            "Les composants sont placés sur des branches séparées.\n\n"
            "• La tension est la même sur chaque branche.\n"
            "• Les courants des branches s'additionnent.\n"
            "• 1/Rt = 1/R1 + 1/R2.\n\n"
            "Exemple : deux résistances de 100 Ω en parallèle donnent Rt = 50 Ω.\n"
            "Si une branche est coupée, les autres continuent de fonctionner "
            "(c'est le montage des prises et des lampes dans une maison).",
        ),
        (
            "Courant continu et alternatif",
            "• Courant continu (DC) : il circule toujours dans le même sens "
            "(piles, batteries, panneaux solaires).\n"
            "• Courant alternatif (AC) : il change de sens régulièrement "
            "(réseau électrique de la maison).\n\n"
            "Le réseau domestique est en alternatif. Vérifie la tension et la "
            "fréquence en vigueur dans ton pays avec ton professeur.",
        ),
        (
            "Protections : fusible et disjoncteur",
            "Ils protègent l'installation contre la surcharge (trop de courant) "
            "et le court-circuit.\n\n"
            "• Fusible : il fond et coupe le circuit, puis il faut le remplacer.\n"
            "• Disjoncteur : il se déclenche, puis on le réarme.\n"
            "• Disjoncteur différentiel : il protège les personnes contre les "
            "chocs électriques en détectant les fuites de courant.",
        ),
        (
            "Règles de sécurité",
            "1. Couper l'alimentation avant toute intervention.\n"
            "2. Vérifier l'absence de tension avec un appareil de mesure.\n"
            "3. Ne jamais travailler les mains mouillées ou pieds nus sur sol humide.\n"
            "4. Utiliser des outils isolés et le matériel de protection.\n"
            "5. Ne jamais remplacer un fusible par un fil ou un fusible plus fort.\n"
            "6. En cas de doute, demander à ton professeur ou à un électricien "
            "qualifié.",
        ),
    ],
    "2": [
        (
            "Le principe de la partie double",
            "Chaque operation comptable est enregistree deux fois : "
            "au debit d'un compte et au credit d'un autre.\n\n"
            "Total des debits = Total des credits.",
        ),
        (
            "Le bilan",
            "Le bilan est une photo du patrimoine de l'entreprise a une date.\n"
            "A gauche : l'ACTIF (ce que l'entreprise possede).\n"
            "A droite : le PASSIF (ce qu'elle doit : capitaux propres + dettes).\n\n"
            "Actif = Passif.",
        ),
    ],
    "3": [
        (
            "Qu'est-ce qu'un algorithme ?",
            "Un algorithme est une suite d'instructions claires pour resoudre "
            "un probleme.\n\n"
            "Exemple : faire du the = chauffer l'eau, mettre le the, attendre, servir.",
        ),
    ],
    "4": [
        (
            "Prendre les mesures",
            "Mesures de base : tour de poitrine, tour de taille, tour de hanches, "
            "longueur d'epaule, longueur de manche, longueur du vetement.\n"
            "Mesure toujours sur une personne debout, sans trop serrer le metre.",
        ),
    ],
    "5": [
        (
            "Les 4 temps du moteur",
            "1. Admission : le melange entre.\n"
            "2. Compression : il est comprime.\n"
            "3. Combustion/Detente : l'etincelle le fait exploser, le piston descend.\n"
            "4. Echappement : les gaz sortent.",
        ),
    ],
}

# Quiz : (question, [choix A, B, C], index bonne reponse, explication)
QUIZ = {
    "1": [
        ("Quelle est la formule de la loi d'Ohm ?", ["U = R × I", "P = U ÷ I", "I = U × R"], 0,
         "U = R × I : la tension est égale à la résistance multipliée par le courant."),
        ("Une résistance de 50 Ω est traversée par un courant de 2 A. Quelle est la tension ?", ["25 V", "100 V", "52 V"], 1,
         "U = R × I = 50 × 2 = 100 V."),
        ("Quelle est l'unité du courant électrique ?", ["Le volt", "L'ampère", "L'ohm"], 1,
         "Le courant se mesure en ampères (A)."),
        ("Une tension de 220 V et un courant de 2 A. Quelle est la puissance ?", ["110 W", "440 W", "222 W"], 1,
         "P = U × I = 220 × 2 = 440 W."),
        ("Un appareil de 2000 W fonctionne pendant 3 heures. Quelle énergie consomme-t-il ?", ["6 kWh", "2 kWh", "6 W"], 0,
         "2000 W = 2 kW, donc W = 2 × 3 = 6 kWh."),
        ("Dans un circuit en série, quelle grandeur est la même partout ?", ["La tension", "Le courant", "La puissance"], 1,
         "En série, le courant est le même dans tous les composants."),
        ("R1 = 10 Ω et R2 = 20 Ω en série. Quelle est la résistance totale ?", ["30 Ω", "200 Ω", "6,7 Ω"], 0,
         "En série, les résistances s'additionnent : 10 + 20 = 30 Ω."),
        ("Deux résistances de 100 Ω sont montées en parallèle. Quelle est la résistance totale ?", ["200 Ω", "50 Ω", "100 Ω"], 1,
         "1/Rt = 1/100 + 1/100 = 2/100, donc Rt = 50 Ω."),
        ("Quel appareil protège les personnes contre les chocs électriques ?", ["L'interrupteur simple", "Le disjoncteur différentiel", "L'ampoule"], 1,
         "Le disjoncteur différentiel détecte les fuites de courant et coupe le circuit."),
        ("Avant d'intervenir sur une installation, que faut-il faire en premier ?", ["Commencer vite", "Couper le courant et vérifier l'absence de tension", "Toucher les fils pour tester"], 1,
         "On coupe toujours l'alimentation, puis on vérifie l'absence de tension."),
    ],
    "2": [
        ("Dans un bilan, que represente l'actif ?", ["Ce que l'entreprise doit", "Ce que l'entreprise possede", "Les benefices"], 1,
         "L'actif regroupe ce que l'entreprise possede."),
        ("Que dit la partie double ?", ["Debits = Credits", "Actif > Passif", "Charges = Produits"], 0,
         "Chaque operation est enregistree au debit et au credit pour le meme montant."),
    ],
    "3": [
        ("Un algorithme est...", ["Un virus", "Une suite d'instructions", "Un cable"], 1,
         "C'est une suite d'instructions pour resoudre un probleme."),
    ],
    "4": [
        ("Comment doit etre la personne pendant la prise de mesures ?", ["Assise", "Debout", "Allongee"], 1,
         "Debout, pour avoir des mesures fiables."),
    ],
    "5": [
        ("Combien de temps compte un moteur a 4 temps ?", ["2", "4", "6"], 1,
         "Admission, compression, combustion, echappement."),
    ],
}

# Orientation : modele a verifier et completer avant diffusion
ORIENTATION = {
    "1": (
        "Filieres de l'enseignement technique et professionnel",
        "Les parcours typiques : formation de niveau CAP/BEP, puis BT, puis BTS "
        "ou Bac technique selon la serie.\n\n"
        "Pour connaitre les series, conditions d'acces, dates d'inscription et "
        "etablissements, rapproche-toi de ton etablissement ou du METFPA. "
        "[A completer avec les informations officielles]",
    ),
    "2": (
        "Stages et insertion",
        "Conseils : prepare un CV d'une page, une lettre courte, et demande un "
        "stage dans les entreprises de ta ville (garages, ateliers, cabinets, "
        "PME). Un stage bien fait ouvre souvent la porte a un emploi.\n"
        "[A completer avec les entreprises partenaires de ton etablissement]",
    ),
    "3": (
        "Metiers et debouches",
        "Electricien, comptable, technicien informatique, couturier/styliste, "
        "mecanicien... Beaucoup de ces metiers permettent aussi de se mettre a "
        "son compte.\n[A completer par filiere]",
    ),
}

# Messages de l'assistant IA par mode
SYSTEM_PROMPTS = {
    "assistant": (
        "Tu es un assistant pedagogique pour des eleves de l'enseignement "
        "technique et professionnel en Cote d'Ivoire. Reponds en francais "
        "simple, avec des exemples concrets du quotidien ivoirien et des "
        "metiers techniques. Reponses courtes (maximum 150 mots), adaptees a "
        "la lecture sur WhatsApp : pas de tableaux, pas de markdown complexe. "
        "Si tu n'es pas sur, dis-le et invite l'eleve a verifier avec son "
        "professeur. Ne fais pas les devoirs a la place de l'eleve : guide-le."
    ),
    "expose": (
        "Tu aides un eleve ivoirien de l'enseignement technique et "
        "professionnel a preparer un expose ou un rapport de stage. Pose-lui "
        "une question a la fois pour l'aider a trouver son sujet, son plan "
        "(introduction, 2 ou 3 parties, conclusion) et ses idees. Francais "
        "simple, messages courts adaptes a WhatsApp. N'invente jamais de "
        "sources, chiffres ou citations : conseille plutot ou chercher "
        "(manuel, professeur, entreprise, bibliotheque). Aide l'eleve a "
        "ecrire avec ses propres mots."
    ),
}

MENU = (
    "Bienvenue ! Je suis ton assistant pour l'enseignement technique et professionnel.\n\n"
    "Reponds avec un numero :\n"
    "1 - Cours et revisions\n"
    "2 - Poser une question a l'assistant IA\n"
    "3 - Aide pour un expose ou un rapport\n"
    "4 - Orientation et debouches\n\n"
    "Ecris MENU a tout moment pour revenir ici."
)

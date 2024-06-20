# GradesCalculator

`GradesCalculator` est un package Python qui permet de calculer une note globale à partir de notes pondérées. Il inclut un script exécutable en ligne de commande pour effectuer ce calcul facilement.

## Installation

Pour installer le package, vous pouvez utiliser `pip` après avoir construit le package localement. Suivez ces étapes :

1. Clonez le dépôt ou téléchargez les fichiers nécessaires.
2. Assurez-vous d'être dans le répertoire contenant `setup.py`.
3. Exécutez les commandes suivantes :

```bash
python setup.py sdist bdist_wheel
pip install .
```

## Utilisation

Une fois installé, vous pouvez utiliser le script en ligne de commande pour calculer les notes. Voici comment l'utiliser :

```bash
calcule_notes note1 poids1 note2 poids2 note3 poids3 ...
```

### Exemple
Supposons que vous avez les notes et poids suivants :

- Note 1 : 3.6 avec un poids de 10
- Note 2 : 4.6 avec un poids de 15
- Note 3 : 5.3 avec un poids de 25
- Note 4 : 4.0 avec un poids de 5
- Note 5 : 4.9 avec un poids de 45
Pour calculer la note globale, exécutez la commande suivante :

```bash
calcule_notes 3.6 10 4.6 15 5.3 25 4.0 5 4.9 45
```
### Résultat

Le script affichera la note globale précise arrondie à 0.1 près et arrondie à 0.5 près :

```bash
Precise Overall Grade (rounded to the nearest 0.1): X.X
Rounded Overall Grade (rounded to the nearest 0.5): Y.Y
```

### Structure du Répertoire

La structure du répertoire pour votre package gradescalculator doit ressembler à ceci :

```bash
gradescalculator/
│
├── gradescalculator/
│   ├── __init__.py
│   └── main.py
│
├── setup.py
└── README.md

```

## Auteur
- Quentin Berthet - [profil github](https://github.com/BERTHETquentin)
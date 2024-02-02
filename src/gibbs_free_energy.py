import os
import re
from distances_calculator import calculate_interatomic_distances_from_file, merge_distances
import numpy as np

def read_scoring_values(pair, scoring_values_directory):
    # Chemin vers le fichier des valeurs de score pour la paire
    file_path = os.path.join(scoring_values_directory, f"{pair}_scoring_values.txt")
    print("Chemin du fichier :", file_path)
    
    scores = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()  # Retirer les espaces en début et fin de ligne
            if line:  # Vérifier si la ligne n'est pas vide
                score_match = re.search(r'Score: (-?\d+(\.\d+)?)', line)
                if score_match:
                    score = float(score_match.group(1))
                    scores.append(score)
                
    result = {pair: scores}
    print("Résultat :", result)
    return result


def calculate_scores(dista_filtered, scoring_values_directory):
    scores_dict = {}
    # Lire d'abord les valeurs de score pour toutes les paires
    all_scoring_values = {}
    for pair in dista_filtered.keys():
        all_scoring_values[pair] = read_scoring_values(pair, scoring_values_directory)[pair]

    # Calcul des scores pour les distances filtrées
    for pair, distances in dista_filtered.items():
        scores_dict[pair] = []
        scoring_values = all_scoring_values[pair]
        for distance in distances:
            index = int(distance)
            if index < len(scoring_values):
                score = scoring_values[index]
                scores_dict[pair].append(score)
            else:
                scores_dict[pair].append(0.0)

    return scores_dict


def calculate_gibbs_free_energy(scores_dict):
    total_gibbs_free_energy = 0.0

    # Itérer sur chaque paire et ses scores dans scores_dict
    for pair, scores in scores_dict.items():
        # Somme de tous les scores pour la paire actuelle
        total_gibbs_free_energy += sum(scores)

    return total_gibbs_free_energy


def main():
    # Structure ARN exemple
    rna_structure = '/home/henes/Téléchargements/1c2x.pdb'

    # Calcul des distances interatomiques pour la structure ARN
    dista = calculate_interatomic_distances_from_file(rna_structure)

    # Filtrer les distances supérieures à 20
    dista_filtered = {pair: [distance for distance in distances if distance <= 20] for pair, distances in dista.items()}

    # Calcul des scores pour les distances filtrées
    scores_dict = calculate_scores(dista_filtered, '/home/henes/Téléchargements')

    gibbs_free_energy_estimation = calculate_gibbs_free_energy(scores_dict)
    print("Estimation de l'énergie libre de Gibbs :", gibbs_free_energy_estimation)


if __name__ == "__main__":
    main()


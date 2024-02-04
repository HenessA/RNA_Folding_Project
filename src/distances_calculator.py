from itertools import combinations
from Scoring_values import compute_scoring_values
from itertools import combinations
import math
import math
import argparse
from itertools import combinations

SCRIPT_DESCRIPTION = """
Calculate scoring values for interatomic distances and write them to CSV and TXT files.
"""

parser = argparse.ArgumentParser(description=SCRIPT_DESCRIPTION)

args = parser.parse_args()

def read_pdb(file_path):
    atoms_data = []
    with open(file_path, 'r') as pdb_file:
        for line in pdb_file:
            if line.startswith('ATOM'):
                atom_name = line[12:16].strip()
                residue_name = line[17:20].strip()
                residue_number = int(line[22:26].strip())
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                atoms_data.append({
                    'atom_name': atom_name,
                    'residue_name': residue_name,
                    'residue_number': residue_number,
                    'x': x,
                    'y': y,
                    'z': z
                })
    return atoms_data

def calculate_distance(coord1, coord2):
    return math.sqrt(sum((a - b)**2 for a, b in zip(coord1, coord2)))

def calculate_interatomic_distances_from_file(file_path):
    atoms_data = read_pdb(file_path)
    base_pair_distances = {
        'AA': [], 'AU': [], 'AC': [], 'AG': [],
        'UU': [], 'UC': [], 'UG': [],
        'CC': [], 'CG': [], 'GG': []
    }

    c3_atoms = [(atom['residue_number'], atom['x'], atom['y'], atom['z']) for atom in atoms_data if atom['atom_name'] == "C3'"]

    for (res1, x1, y1, z1), (res2, x2, y2, z2) in combinations(c3_atoms, 2):
        if abs(res1 - res2) >= 3:
            base_pair = atoms_data[res1 - 1]['residue_name'] + atoms_data[res2 - 1]['residue_name']
            distance = calculate_distance((x1, y1, z1), (x2, y2, z2))
            if base_pair in base_pair_distances:
                base_pair_distances[base_pair].append(distance)

    return base_pair_distances


def merge_distances(distances_list):
    merged_distances = {
        'AA': [], 'AU': [], 'AC': [], 'AG': [],
        'UU': [], 'UC': [], 'UG': [],
        'CC': [], 'CG': [], 'GG': []
    }

    for distances in distances_list:
        for base_pair, distance_list in distances.items():
            merged_distances[base_pair].extend(distance_list)

    return merged_distances

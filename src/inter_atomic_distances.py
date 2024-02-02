from distances_calculator import calculate_interatomic_distances_from_file, merge_distances
from frequency_calculator import compute_observed_frequencies, compute_reference_frequency
from Scoring_values import compute_scoring_values, write_scoring_values
def main():
    pdb_files = ['/home/henes/Téléchargements/1drr.pdb',
                 '/home/henes/Téléchargements/2ap0.pdb',
                 '/home/henes/Téléchargements/1c2x.pdb',
                 '/home/henes/Téléchargements/7jrs.pdb',
                 '/home/henes/Téléchargements/7jrt.pdb',
                 ]

    distances_list = []
    for file_path in pdb_files:
        distances_list.append(calculate_interatomic_distances_from_file(file_path))
    output_file = "distances_output.txt"
    merged_distances = merge_distances(distances_list)

    with open("/home/henes/Téléchargements/merged_distances.txt", "w") as output_file:
        for base_pair, pair_distances in merged_distances.items():
            output_file.write(f"Base Pair: {base_pair}, Distances: {pair_distances}\n")

 # Compute observed frequencies
    observed_frequencies = compute_observed_frequencies(merged_distances)

    # Print observed frequencies
    print("Observed Frequencies:")
    for base_pair, frequencies in observed_frequencies.items():
        print(f"Base Pair: {base_pair}, Frequencies: {frequencies}")
    print(" ")
    print(" ")

    reference_freq = compute_reference_frequency(list(merged_distances.values()))
    print("Reference Frequencies:", reference_freq)

    # Compute scoring values for each base pair
    scoring_values = compute_scoring_values(observed_frequencies, reference_freq)

    #Write scoring values to files
    write_scoring_values(scoring_values)


if __name__ == "__main__":
    main()

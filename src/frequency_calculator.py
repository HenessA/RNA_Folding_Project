import argparse

num_intervals = 20
interval_size = 1.0  # Angstrom


SCRIPT_DESCRIPTION = """
Calculate observed and reference frequencies for interatomic distances.
"""
parser = argparse.ArgumentParser(description=SCRIPT_DESCRIPTION)

args = parser.parse_args()

def compute_observed_frequencies(pair_distances_list):

    observed_freq = {}

    for base_pair, distance_list in pair_distances_list.items():
        # Filter distances less than or equal to 20.00 as for the assignment
        filtered_distances = [distance for distance in distance_list if distance <= 20.00]


        frequency = [0] * num_intervals

        # Count the number of filtered distances falling into each interval for the current pair
        for distance in filtered_distances:
            bin_index = min(int(distance / interval_size), num_intervals - 1)
            frequency[bin_index] += 1


        total_distances = len(filtered_distances)
        if total_distances > 0:
            frequency = [count / total_distances for count in frequency]

        observed_freq[base_pair] = frequency

    return observed_freq


def compute_reference_frequency(distances_lists):
    # Filter all distances to keep only those equal to or less than 20.0
    filtered_distances = [distance for distances_list in distances_lists for distance in distances_list if distance <= 20.0]

    if not filtered_distances:
        return {}  # Return an empty dictionary if no distances are found

    # Initialize frequency counters for each distance bin
    frequency = [0] * num_intervals

    # Count the number of distances falling into each bin
    for distance in filtered_distances:
        bin_index = min(int(float(distance) / interval_size), num_intervals - 1)
        frequency[bin_index] += 1

    # Normalize frequencies by dividing by the total number of distances
    total_distances = len(filtered_distances)
    if total_distances > 0:
        frequency = [count / total_distances for count in frequency]

    return frequency





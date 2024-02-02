import csv
import math

def compute_scoring_values(observed_freq, reference_freq):
    scoring_values = {}
    for base_pair, observed in observed_freq.items():
        if isinstance(reference_freq, dict):
            reference = reference_freq.get(base_pair, [0] * len(observed))  # Use 0 frequencies if not found
        else:
            reference = reference_freq
        scoring_values[base_pair] = []
        for i, ref in enumerate(reference):
            if ref > 0 and observed[i] > 0:
                score = -math.log(observed[i] / ref)
            else:
                score = 0  # Set score to 0 if either observed or reference frequency is non-positive
            scoring_values[base_pair].append(score)
    return scoring_values

def write_scoring_values(scoring_values):
    for base_pair, scores in scoring_values.items():
        # Writing to CSV file
        with open(f"{base_pair}_scoring_values.csv", "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Distance", "Score"])
            for i, score in enumerate(scores):
                distance = i + 0.5  # Midpoint of the interval
                csv_writer.writerow([distance, score if score != "N/A" else None])

        # Writing to TXT file
        with open(f"{base_pair}_scoring_values.txt", "w") as txt_file:
            txt_file.write(f"Pair: {base_pair}\n")
            for i, score in enumerate(scores):
                interval = i + 1
                txt_file.write(f"Interval: {interval}, Score: {score if score != 'N/A' else 'N/A'}\n")

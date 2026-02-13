# utils/loader.py

import os


def list_maps(maps_folder="maps"):
    """
    Returns list of available map filenames.
    """
    if not os.path.exists(maps_folder):
        raise FileNotFoundError(f"{maps_folder} folder not found.")

    return [f for f in os.listdir(maps_folder) if f.endswith(".txt")]


def load_map(file_path):
    """
    Loads puzzle map from file and returns tuple representation.
    """
    with open(file_path, "r") as f:
        lines = f.readlines()

    numbers = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        for p in parts:
            if p == "_" or p == "0":
                numbers.append(0)
            else:
                numbers.append(int(p))

    if len(numbers) != 9:
        raise ValueError("Map must contain exactly 9 values.")

    if set(numbers) != set(range(9)):
        raise ValueError("Map must contain numbers 0–8 exactly once.")

    return tuple(numbers)
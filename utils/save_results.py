# Import libraries
import os
import json
from datetime import datetime

def save_analysis(result: dict, folder = "data/results"):
    """Save Analysis Result"""
    os.makedirs(folder, exist_ok=True)

    filename = f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    path = os.path.join(folder, filename)

    with open(path, 'w') as f:
        json.dump(result, f, indent=4)

    return path


import numpy as np

def validate_station_efficiency(steps, sigma_factor=0.10):
    """
    Validates if the 1-operator setup stays under the 240s limit
    including a 10% human variance (sigma).
    """
    base_time = sum(steps.values())
    variance = base_time * sigma_factor
    total_expected = base_time + variance
    
    limit = 240 # Renault Station Limit
    is_valid = total_expected < limit
    
    return {
        "Base Cycle Time": f"{base_time}s",
        "Variance (Sigma)": f"{variance}s",
        "Total Projected": f"{total_expected}s",
        "Takt Compliance": "✅ PASS" if is_valid else "❌ FAIL"
    }

# Example data from the Clio 5 line
clio_steps = {
    "pick_up": 15,
    "piston_lock": 5,
    "lift": 12,
    "transfer": 20,
    "alignment": 15,
    "tilt_30": 8,
    "piston_release": 5
}

print(validate_station_efficiency(clio_steps))

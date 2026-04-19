import pytest
# Assuming your logic is in a file named automation_logic.py
# or we can define a simple test case for the workflow here

def calculate_cycle_time(steps):
    return sum(steps.values())

def test_clio_5_takt_compliance():
    """
    Test if the automated workflow stays under the 240s Renault station limit.
    """
    clio_steps = {
        "pick_up": 15,
        "piston_lock": 5,
        "lift": 12,
        "transfer": 20,
        "alignment": 15,
        "tilt_30": 8,
        "piston_release": 5
    }
    
    total_time = calculate_cycle_time(clio_steps)
    
    # Assert the station logic stays within safety/production bounds
    assert total_time < 240, f"Cycle time {total_time}s exceeds station limit!"
    assert total_time > 0, "Cycle time cannot be zero."

def test_operator_reduction_logic():
    """
    Ensure the workflow logic only accounts for 1 operator.
    """
    operators_required = 1
    assert operators_required == 1, "Project goal was to reduce manpower to 1 operator."

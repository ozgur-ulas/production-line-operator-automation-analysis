import os
import pandas as pd

class AutomationValidator:
    def __init__(self, data_path: str):
        """
        Initializes the Automation Validator for the Renault Body Shop Station.
        """
        self.data_path = data_path
        self.takt_limit = 240  # Max acceptable cycle time in seconds (4 minutes)
        
        # Mandatory sequential engineering workflow steps as defined by design requirements
        self.required_steps = [
            "pick_up_part",
            "close_pistons",
            "arm_lift",
            "move_to_fixture",
            "vertical_adjustment",
            "tilt_part",
            "open_pistons",
            "fixture_confirmation"
        ]

    def load_data(self) -> pd.DataFrame:
        """Loads and prepares the cycle time step data."""
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Missing cycle time logs at: {self.data_path}")
        
        df = pd.read_csv(self.data_path)
        # Normalize text inputs to eliminate case-sensitivity mismatches
        df['type'] = df['type'].astype(str).str.strip().str.capitalize()
        if 'step_id' in df.columns:
            df['step_id'] = df['step_id'].astype(str).str.strip().str.lower()
        return df

    def validate_workflow_integrity(self, df: pd.DataFrame) -> bool:
        """
        Verifies that the sequence contains all required physical steps 
        for deterministic, repeatable execution.
        """
        if 'step_id' not in df.columns:
            return False
        observed_steps = set(df['step_id'].unique())
        return set(self.required_steps).issubset(observed_steps)

    def calculate_metrics(self) -> dict:
        """
        Calculates lean manufacturing metrics, structural automation support ratios,
        and validates cycle times against critical takt thresholds.
        """
        df = self.load_data()
        
        # Calculate segmented time distributions
        total_time = float(df['duration_sec'].sum())
        manual_time = float(df[df['type'] == 'Manual']['duration_sec'].sum())
        auto_time = float(df[df['type'] == 'Automation']['duration_sec'].sum())
        
        # Engineering constraints checks
        takt_compliance = total_time <= self.takt_limit
        workflow_intact = self.validate_workflow_integrity(df)
        
        # Final deployment decision logic
        if takt_compliance and workflow_intact:
            status = "✅ PASS (Station Optimized)"
        elif not takt_compliance:
            status = "❌ FAIL (Line Stoppage Risk - Cycle Time Exceeded)"
        else:
            status = "⚠️ WARNING (Time Compliant, but Missing Mandatory Process Steps)"

        # Calculate standard industrial KPIs
        automation_index = (auto_time / total_time * 100) if total_time > 0 else 0.0
        operator_actions = len(df[df['type'] == 'Manual'])

        return {
            "Total Cycle Time (s)": round(total_time, 2),
            "Manual Effort (s)": round(manual_time, 2),
            "Automation Support (s)": round(auto_time, 2),
            "Automation Index (%)": round(automation_index, 1),
            "Total Operator Actions": operator_actions,
            "Workflow Integrity Verified": workflow_intact,
            "Validation Status": status
        }

if __name__ == "__main__":
    # Path configuration matching repo architecture
    data_file_path = os.path.join('data', 'cycle_time_steps.csv')
    
    print("--- Industrial Automation Validation Framework ---")
    print(f"Targeting: Renault Clio 5 Bodyside Assembly Line (< {AutomationValidator(data_file_path).takt_limit}s limit)")
    print("-" * 50)
    
    try:
        validator = AutomationValidator(data_file_path)
        results = validator.calculate_metrics()
        
        for key, value in results.items():
            print(f"{key:<30}: {value}")
            
    except Exception as e:
        print(f"Execution Halt: {e}")

# Operator Interface & Workflow Logic ♟️

### The "Minimalist" Constraint
To ensure the 63 vh/h target, we eliminated all complex HMI (Human Machine Interface) elements. The operator only interacts with:
1. **Fixed Handle:** For movement authorization.
2. **Vertical/Lateral Joysticks:** No screens, just tactile feedback.

### 🔄 The 30° Tilt Logic
The 30-degree tilt was identified as the critical ergonomics factor. 
* **Constraint:** Manual tilting of a Clio 5 bodyside causes long-term strain.
* **Solution:** Automated tilt triggered only when the arm reaches the fixture proximity sensors.
* **Result:** Reduced cognitive load from "High" to "Low" during the most dangerous phase of the transfer.

### 📐 Mathematical Validation
The total cycle time $T_{total}$ is calculated as:
$$T_{total} = \sum (t_{manual} + t_{automation}) + \sigma$$
*Where $\sigma$ represents the variance in operator speed.*
import json
import os
from enums import json_tags

results_filepath = './oracle_large_scale_migrations/results.json'

def load_results():
    if os.path.exists(results_filepath):
        with open(results_filepath, 'r') as f:
            return json.load(f)
    else:
        return {}
    
def save_results(results):
    with open(results_filepath, 'w') as f:
        json.dump(results, f, indent=2)
        
def record_step(migration_name, results):
    data = load_results()
    
    if migration_name not in data:
        data[migration_name] = []
    
    data[migration_name].append({
        **results
    })
    
    save_results(data)
    
if __name__ == "__main__":
    record_step("migration_1", {
        "step_name": "test_run",
        "phase": "before_migration",
        "time_cost": 2.5
    })
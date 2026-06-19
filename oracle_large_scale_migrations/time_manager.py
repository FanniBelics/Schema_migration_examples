from contextlib import contextmanager
import time
from enums import states, json_tags

@contextmanager
def measure(label):
    start = time.perf_counter()
    result = {}
    try:
        yield result
    finally:
        end = time.perf_counter()
        duration = end - start
        print(f"[{label}] took {duration:.6f} seconds")
        result['time_cost'] = duration
        
        
if __name__ == "__main__":
    label = 'expand_table'
    with measure(label) as result:
        time.sleep(2)
        result[json_tags.step_name.value] = label
        result[json_tags.phase.value] = states.before_migration.value
    print(result)
from enum import Enum


class states(Enum):
    before_migration = "before_migration"
    in_migration_state = "in_migration_state"
    after_migration = "after_migration"
    
class json_tags(Enum):
    step_name = "step_name"
    phase = "phase"
    time_cost = "time_cost"
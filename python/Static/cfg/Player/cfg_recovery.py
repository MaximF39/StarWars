update_energy = 1 # s
update_health = 1 # s

def recovery_energy(max_energy, repair_skills):
    return int(max_energy * 0.01 + repair_skills * 2)

def recovery_health(max_health, repair_skills):
    return int(max_health * 0.005 + repair_skills * 2)
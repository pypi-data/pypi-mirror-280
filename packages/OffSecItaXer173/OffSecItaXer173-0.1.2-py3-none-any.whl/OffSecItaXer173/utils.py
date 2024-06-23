from .corsi import corsi

def durata_totale():
    return sum(corso.durata for corso in corsi)

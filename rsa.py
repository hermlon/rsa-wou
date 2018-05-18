import secrets

def find_next_prime(random_number):
    """Diese Funktion gibt die nächst größere Primzahl zu einer Zahl zurück"""
    
    pass

def euklid_ext(a, b):
    """Gibt für Primzahlen a und b mit ggT(a, b) = 1 das Tupel (x, y) zurück, für die a * x + b * y = 1 gilt"""
    
    pass

def generate_key(p, q):
    """Diese Funktion generiert aus den Primzahlen p und q den privaten Schlüssel (d, n) und den öffentlichen Schlüssel (e, n) und gibt diese als Tupel (priv_key, pub_key) also ((d, n), (e, n)) zurück"""
    
    # Hinweise
    # kein Plan...
    pass

def encrypt(pub_key, message):
    """Diese Funktion verschlüsselt die Nachricht message nachdem jedes Zeichen in eine Dezimalzahl (UTF-8 Unicode) umgewandelt wurde und gibt die verschlüsselte Zahl für jeden Buchstaben als Liste cipher zurück"""

    pass

def decrypt(priv_key, cipher):
    """Diese Funktion entschlüsselt die Liste c, welche den UTF-8 Unicode Dezimalwert für jedes Zeichen enthält und gibt die Nachricht als String message zurück"""
    pass

"""
# Hauptprogramm

# Bereich in dem die generierte Zufallszahl liegen soll
keylength = 10 * 100

# generiert eine Kryptosichere Zufallszahl und sucht die nächste Primzahl
p = find_next_prime(secrets.randbelow(keylength))
q = find_next_prime(secrets.randbelow(keylength))

keys = generate_key(p, q)

priv_key = keys[0]
pub_key = keys[1]

cipher = encrypt(pub_key, 'Test')
print(decrypt(priv_key, cipher))
"""

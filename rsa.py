import secrets

def find_next_prime(random_number):
    """Diese Funktion gibt die nächst größere Primzahl zu einer Zahl zurück"""
    
    pass

def euklid_ext(a, b):
    """Gibt für a und b mit ggT(a, b) = 1 das Tupel (x, y) zurück, für die a * x + b * y = 1 gilt"""
    x = 0
    y = 0
    # Hinweise:
    # Zuerst den einfachen euklidischen Algorithmus implementieren
    # Der erweiterte kann gleichzeitig mit dem einfachen ausgeführt werden, d. h. es wird nicht wie im Unterricht am Ende rückwärts ausgeführt, da man sonst alle Zahlen zwischenspeichern müsste
    # a % b     Rest bei Division a durch b
    # a // b        Ganzzahliges Ergebnis der Division a durch b, abgerundet
    while a != 1:
        c = a // b      
        d = a % b
        print(str(a) + ' = ' + str(c) + ' * ' + str(b) + ' mod ' + str(d))
        
        x = x + 1
        y = y + b
        print(str(x) + '       ' + str(y))
        a = b
        b = d
        
        
        
def generate_key(p, q):
    """Diese Funktion generiert aus den Primzahlen p und q den privaten Schlüssel (d, n) und den öffentlichen Schlüssel (e, n) und gibt diese als Tupel (priv_key, pub_key) also ((d, n), (e, n)) zurück"""
    
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
euklid_ext(121,18)
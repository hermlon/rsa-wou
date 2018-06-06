import secrets
import math

def find_all_primes(random_number):
    Prim = [2]
    i= 0
    a=3
    while a < math.sqrt(random_number):
        f = a % Prim[i]
        if f == 0:
            a = a+1
            i=0
        else:
            if i == len(Prim)-1:
                Prim.append(a)
                a=a+1
                i = 0
            else:
                i = i+1
    return Prim
                
def find_next_prime(random_number):
    """Diese Funktion gibt die nächst größere Primzahl zu einer Zahl zurück"""
    
    while True:
        g = False
        Prim= find_all_primes(random_number)
        for n in Prim:
            if random_number % n == 0:
                g = True
        if g:
            random_number=random_number+1
            Prim= find_all_primes(random_number)
        else:   
            return random_number

def euklid_ext(a, b):
    """Gibt für Primzahlen a und b mit ggT(a, b) = 1 das Tupel (x, y) zurück, für die a * x + b * y = 1 gilt"""
    cnt_a = 0
    cnt_b = 1
    old_cnt_a = 1
    old_cnt_b = 0

    while b != 0:
        rest = a % b
        q = a // b
        aux_cnt_a = cnt_a
        aux_cnt_b = cnt_b

        cnt_a = q * cnt_a + old_cnt_a
        cnt_b = q * cnt_b + old_cnt_b

        old_cnt_a = aux_cnt_a
        old_cnt_b = aux_cnt_b
        
        a = b
        b = rest
    # print('{} , {}'.format(old_cnt_a, old_cnt_b))
    return old_cnt_b

def generate_key(p, q):
    """Diese Funktion generiert aus den Primzahlen p und q den privaten Schlüssel (d, n) und den öffentlichen Schlüssel (e, n) und gibt diese als Tupel (priv_key, pub_key) also ((d, n), (e, n)) zurück"""
    n = p * q
    euler_n = (p-1)*(q-1)
    e = 7
    d = euklid_ext(euler_n, e)
    priv_key = (d, n)
    pub_key = (e, n)
    return (priv_key, pub_key)

def encrypt(pub_key, message):
    """Diese Funktion verschlüsselt die Nachricht message nachdem jedes Zeichen in eine Dezimalzahl (UTF-8 Unicode) umgewandelt wurde und gibt die verschlüsselte Zahl für jeden Buchstaben als Liste cipher zurück"""
    e = pub_key[0]
    n = pub_key[1]
    cipher = []
    for character in message:
        m = ord(character)
        c = m ** e % n
        cipher.append(c)

    return cipher

def decrypt(priv_key, cipher):
    """Diese Funktion entschlüsselt die Liste c, welche den UTF-8 Unicode Dezimalwert für jedes Zeichen enthält und gibt die Nachricht als String message zurück"""
    d = priv_key[0]
    n = priv_key[1]
    message = ''
    for c in cipher:
        m = c ** d % n
        message += chr(m)
    return message

# Hauptprogramm

# Bereich in dem die generierte Zufallszahl liegen soll
keylength = 100

# generiert eine Kryptosichere Zufallszahl und sucht die nächste Primzahl
p = find_next_prime(secrets.randbelow(keylength))
q = find_next_prime(secrets.randbelow(keylength))

print('{}, {}'.format(p, q))
p = 31
q = 13

keys = generate_key(p, q)

priv_key = keys[0]
pub_key = keys[1]


cipher = encrypt(pub_key, 'Test_1')
print(decrypt(priv_key, cipher))

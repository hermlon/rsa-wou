import secrets
import math
import logging
import sys


def find_primes(start, end, known_primes):
    n = start
    # nächste ungerade Zahl
    if n % 2 == 0:
        n += 1
        
    while n <= math.sqrt(end):
        for p in known_primes:
            if n % p == 0:
                break
        else:
            known_primes.append(n)
        n += 2
    return known_primes

def find_next_prime(a):
    """Diese Funktion gibt die nächst größere Primzahl zu einer Zahl zurück (und berechnet alle bekannten Primzahlen nicht jedes mal neu)"""
    # nächste ungerade Zahl
    if a % 2 == 0:
        a += 1
        
    primes = find_primes(3, a, [2])
    
    while True:
        primes = find_primes(a, a+2, primes)
        for p in primes:
            if a % p == 0:
                break
        else:
            return a
        a += 2

def find_all_primes(random_number):
    Prim = [2]
    i= 0
    a=3
    # kleiner gleich, da sonst Quadratzahlen Primzahlen sind
    while a <= math.sqrt(random_number):
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

def find_next_prime_slow(random_number):
    """Diese Funktion gibt die nächst größere Primzahl zu einer Zahl zurück (und berechnet alle bekannten Primzahlen jedes mal neu)"""
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
    org_a = a
        
    cnt_a = 0
    cnt_b = 1
    old_cnt_a = 1
    old_cnt_b = 0

    while b != 0:
        rest = a % b
        q = a // b

        old_cnt_a, cnt_a = cnt_a, -q * cnt_a + old_cnt_a
        old_cnt_b, cnt_b = cnt_b, -q * cnt_b + old_cnt_b
        
        a = b
        b = rest

    if old_cnt_b < 0:
        # b ist negativ, das positive modulo a gleiche Ergebnis ist b + a
        return old_cnt_b + org_a
    else:
        return old_cnt_b

def generate_key(p, q):
    """Diese Funktion generiert aus den Primzahlen p und q den privaten Schlüssel (d, n) und den öffentlichen Schlüssel (e, n) und gibt diese als Tupel (priv_key, pub_key) also ((d, n), (e, n)) zurück"""
    n = p * q
    euler_n = (p-1)*(q-1)
    # vierte Fermat Zahl -> schnelle Potenzierung
    e = 2 ** 16 + 1
    d = euklid_ext(euler_n, e)
    priv_key = (d, n)
    pub_key = (e, n)
    
    logging.debug('Privater Schlüssel: d: {}, n: {}'.format(d, n))
    logging.debug('Öffentlicher Schlüssel: e: {}, n: {}'.format(e, n))
    
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
        
    logging.debug('Verschlüsselte Nachricht: {}'.format(cipher))
    return cipher

def decrypt(priv_key, cipher):
    """Diese Funktion entschlüsselt die Liste c, welche den UTF-8 Unicode Dezimalwert für jedes Zeichen enthält und gibt die Nachricht als String message zurück"""
    d = priv_key[0]
    n = priv_key[1]
    message = ''
    for c in cipher:
        m = c ** d % n
        message += chr(m)
        
    logging.debug('Entschlüsselte Nachricht: {}'.format(message))
    return message

def random_key(keylength):
    """Gibt einen zufällig generierten RSA key mit keylength < Zufallszahl für Primzahlfindung < keylength * 2 zurück"""
    p = 0
    q = 0
    # unterschiedliche Primzahlen
    while p == q:
        # generiert eine Kryptosichere Zufallszahl und sucht die nächste Primzahl
        p = find_next_prime(secrets.randbelow(keylength)+keylength)
        q = find_next_prime(secrets.randbelow(keylength)+keylength)
    logging.debug('Zufällige Primzahlen p: {}, q: {}'.format(p, q))
    return generate_key(p, q)


if __name__ == '__main__':
	# Hauptprogramm
	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	
	# zufälliges Schlüsselpaar generieren
	keypair = random_key(300)
	
	priv_key = keypair[0]
	pub_key = keypair[1]
	
	# verschlüsseln:
	cipher = encrypt(pub_key, 'Eine Testnachricht mit Einhorn und schwebenden Businessman! \U0001F984 \U0001F574')
	
	# entschlüsseln
	print(decrypt(priv_key, cipher))
	

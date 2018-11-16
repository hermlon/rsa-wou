import rsa


def v(pub_key, message):
	print('Geheimtext: {}'.format(rsa.encrypt(pub_key, message)))

def e(cipher):
	global priv_key
	print('Klartext: {}'.format(rsa.decrypt(priv_key, cipher)))
	
# zufälliges Schlüsselpaar generieren
keypair = rsa.random_key(10)

priv_key = keypair[0]
pub_key = keypair[1]

print('-------------RSA------------')
print('Öffentlicher Schlüssel: {}'.format(pub_key))
print('Privater Schlüssel: {}'.format(priv_key))

print('Verschlüsseln: v(privater_schlüssel, text)')
print('z. B.: v((17, 247), \'Hallo!\')')
print('Entschlüsseln: v(geheimtext)')
print('z. B.: v([128, 67, 231, 231, 63, 167])')
print('----------------------------')

import pdb; pdb.set_trace();

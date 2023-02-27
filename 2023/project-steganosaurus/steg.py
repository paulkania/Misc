
import random as r

#key -> symmetric key
#rb -> random bit data with the key used in order to hide the plaintext 'pgp
#pgp -> plaintext transfered into bin

#E(key,pgp,rbv1)->rbv2
#arguably rbv2 is as much the key as is what i call the key. both are equally indispensable for the revealing of the plaintext, though rbv2 is more of a ciperhtext, and the key is shorter.


#1turn pgp key into binary
pgpo='CB536D9E10B1251DD59CBF686CA79961EA6170E3'
pgp='CB536D9E10B1251DD59CBF686CA79961EA6170E3'
pgp=pgp.lower()
bp=bin(int(pgp,16))
bpo=bin(int(pgp,16))
ip=(int(bp,2))
hp=hex(ip)

#2create random string that is larger than pgpkey
s=''
while len(s) < (len(pgp)*14):
    s+=str(r.random())[2:]

#3turn  this random string into binary.
rb=bin(int(s))
rboo=rb


#4turn the binary into a list, so that i can impregnate my pgp-bin into the random data
rbl=[]
while rb:
    rbl.append(rb[0])
    rb=rb[1:]


#5 for each binary digit in my binary-pgp-fingerprint, i choose a random number. this random number is where the next pgp binary datum will be impregnated into the larger rand-data-string.
#also forms the secret-key
#additionally to choosing the key, i also use the key in this function, to take a pgp-bin-plug, and plug into into the randbits.
ji=0
key=[]
while bp:
    j=r.randint(1,14)
    ji+=j
    key.append(j)
    plug=bp[0]
    rbl[ji]=plug
    bp=bp[1:]

print(key)

#6 using the key and the random data to pull back out the thing.
#concievably, if i used this program on an airgapped machine, and then saved the key, and the random data, and kept them secret, i could bring them together in order to pull the plaintext out of the ciphertext with the key.
reconstruct=''
keyagg=0
while key:
    reconstruct+=(rbl[key[0]+keyagg])
    keyagg+=key[0]
    key=key[1:]

print('------------')
print(reconstruct)
fin=int(reconstruct,2)
print(hex(fin))
print(pgpo)


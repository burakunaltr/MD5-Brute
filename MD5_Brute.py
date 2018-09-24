#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__          = "Burak Ünal"
__email__           = "burakunalofficial[H0RS3]gmail.com"

import random
import hashlib


md5hash = "f61be98714f03b991bf2fa4250202343"  # ctfussu0r texti için hash değeri (Sadece hash biliniyor tabi.)

def MD5cek(plaintext): # MD5 çıktı üreten method
    m = hashlib.md5()
    m.update(plaintext.encode('utf-8'))
    return m.hexdigest()

def karistir(): # Karakterleri karan method
    s = "s0rusu" # ctfsorusu harflerinden oluşacak 9 karakterli, ilk 3 karakteri ctf olacak text için kalan harfler
    c = ''.join(random.sample(s, len(s))) # karılan harfleri değişkene atama
    k = 'ctf' + c # kombinasyon daraltmak için ekleme çıkarma
    return k

abc=""

while MD5cek(abc) != md5hash: # abc değişkenindeki değerin MD5 hash karşılığı doğru olmadığı sürece dön.
    print("olmadı ===>",abc)
    abc = karistir()
    if MD5cek(abc) == md5hash: # değişkenin MD5 karşılığı doğruysa döngüden çık. Sonucu bas.
        print("BULDUM BULDUM ====>",abc)
        break

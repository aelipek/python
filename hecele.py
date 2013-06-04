#! /susr/bin/python
# -*- coding: utf-8 -*-
 
import sys
 
def lowercase(ch):
    return {
    'İ':u'i',
    'I':u'ı',
    'Ç':u'ç',
    'Ğ':u'ğ',
    'Ş':u'ş'   
    }.get(ch, ch.lower())
       
def sesli(ch):
    ch = lowercase(ch)
    if ch in [u'a', u'e', u'i', u'ı', u'o', u'ö', u'u', u'ü']:
        return True
    else:
        return False


hece =list()

def hecele(str):
    index=0
    length=len(str)
    while sesli(str[index]) ==False and length>index+1:
        index=index+1
    global hece #fonksiyon dışında tanımlanan listeyi global yaparak içeride 
    try:        #güncellemenin yolunu açmış olduk
        if sesli(str[index+1]) :
            hece.append(str[0:index+1])
            #print str[0:index+1]
            hecele(str[index+1:])
        elif length>index+2:
            if sesli(str[index+2]) :
                hece.append(str[0:index+1])
                #print str[0:index+1]
                hecele(str[index+1:])
            elif length>index+3:
                if sesli(str[index+3]) :
                    hece.append(str[0:index+2])
                    #print str[0:index+2]
                    hecele(str[index+2:])
                else:
                    if str[index+1:index+4] in [u'str', u'ktr', u'mtr', u'nsp']:
                        #print "istisna!.."
                        hece.append(str[0:index+2])
                        #print str[0:index+2]
                        hecele(str[index+2:])
                    else:
                        #print "üç sessiz, normal kural"
                        hece.append(str[0:index+3])
                        #print str[0:index+3]
                        hecele(str[index+3:])
            else:
                 hece.append(str)
                #print unicode(str)
        else:
            hece.append(str)
            #print unicode(str)
    except:
        hece.append(str)
        #print unicode(str)
def metin(cumle):
    cumle = unicode(cumle, 'utf8')
    cumle = cumle.strip('."\',;')
    words = cumle.split()
    
    for word in words: 
        hecele(word)
    yeni_hece= list()
    for i in hece: #bu listeyi her seferinden boşaltmam gerekti çünkü 
        yeni_hece.append(i)  #fonksiyonu her çağırmamda üstüne ekleme yapıyor
    for i in range(len(hece)): #global yapmamdan kaynaklandı sanırım
       hece.pop()
    return yeni_hece
    

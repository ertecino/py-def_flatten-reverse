# Bir listeyi düzleştiren fonksiyon

def flatten(liste):
  """
  Bir listeyi düzleştiren fonksiyon.

  Parametreler:
    liste: Düzleştirilecek liste.

  Döndürülen değer:
    Düzleştirilmiş liste.

  Örnek bir liste: 
    ornek_liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
    sonuc = flatten(ornek_liste)
    print(sonuc)  
  """
  yeni_liste = [] # Yeni bir liste oluşturuyoruz
  for eleman in liste: # Listeyi döngü ile geziyoruz
      if isinstance(eleman, list): # Eğer eleman bir liste ise
          yeni_liste.extend(flatten(eleman)) # Elemanı fonksiyona gönderip sonucu yeni listeye ekliyoruz
      else: # Eğer eleman bir liste değilse
          yeni_liste.append(eleman) # Elemanı yeni listeye ekliyoruz
  return yeni_liste # Yeni listeyi döndürüyoruz




# Verilen listenin içindeki elemanları tersine döndüren fonksiyon

def reverse(liste):
  """
  Verilen listenin içindeki elemanları tersine döndüren fonksiyon.

  Parametreler:
    liste: Elemanları tersine döndürülecek liste.

  Döndürülen değer:
    Elemanları tersine döndürülmüş liste.

  Örnek bir liste: 
    ornek_liste = [[1, 2], [3, 4], [5, 6, 7]]
    sonuc = reverse(ornek_liste)
    print(sonuc) 
    [[7, 6, 5], [4, 3], [2, 1]]
  """
  yeni_liste = [] # Yeni bir liste oluşturuyoruz
  for eleman in liste: # Listeyi döngü ile geziyoruz
      if isinstance(eleman, list): # Eğer eleman bir liste ise
          yeni_liste.append(reverse(eleman)) # Elemanı fonksiyona gönderip sonucu yeni listeye ekliyoruz
      else: # Eğer eleman bir liste değilse
          yeni_liste.append(eleman) # Elemanı yeni listeye ekliyoruz
  return yeni_liste[::-1] # Yeni listeyi tersine çevirip döndürüyoruz
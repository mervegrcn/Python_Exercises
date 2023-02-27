###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)

l = [1,2,3,4]
type(l)

d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
type(d)

t = ("Machine Learning", "Data Science")
type(t)

s = {"Python", "Machine Learning", "Data Science"}
type(s)


###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."

text = text.upper().replace(",", "").replace(".", "").split(" ")


###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.

print("Eleman sayısı: ", len(lst))

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.

print("Sıfırıncı ve onuncu index'teki elemanlar: ", lst[0],",",lst[10])

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.

data = lst[0:4]

# Adım 4: Sekizinci index'teki elemanı silin.

lst.pop(8)

# Adım 5: Yeni bir eleman ekleyin.

lst.append(":)")

# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.

lst.insert(8, "N")


###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.

dict.keys()

# Adım 2: Value'lara erişiniz.

dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

dict.update({'Daisy': ['England', 13]})
#FARKLI YOL:
dict['Daisy'][1] = 13

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict.update({'Ahmet': ['Turkey', 24]})

# Adım 5: Antonio'yu dictionary'den siliniz.

dict.pop("Antonio")

#alternatif
del dict["Antonio"]

###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################

l = [2, 13, 18, 93, 22]

odd = []
even = []

def oddeven(list):
     for i in list:
          if i % 2 == 0:
               even.append(i)
          else:
               odd.append(i)
     return odd, even

odd, even = oddeven(l)

# List Comprehension - Alternatif yol
def oddeven(list):
    even = [x for x in list if x % 2 == 0]
    odd = [x for x in list if x % 2 != 0]
    return odd, even

even, odd = oddeven(l)
print("Even Numbers: ", even)
print("Odd Numbers: ", odd)

###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

ogrenciler = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]


def universite(ogrenciler):
    for x,student in enumerate(ogrenciler):
        if x<3:
            print("Mühendislik Fakültesi" + " " + str(x+1) + ". öğrenci:" + "" + student)
        else:
            print("Tıp Fakültesi" + " " + str(x-2) + ". öğrenci:" + "" + student)

universite(ogrenciler)

# Alternatif
for index, ogrenci in enumerate(ogrenciler):
    if index < 3:
        print("Mühendislik Fakültesi {}. öğrenci: {}".format(index+1, ogrenci))
    else:
        print("Tıp Fakültesi {}. öğrenci: {}".format(index-2, ogrenci))


###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve
# kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

x = list(zip(ders_kodu, kredi, kontenjan))
type(x)

for i in x:
    print("Kredisi "+ str(i[1]) +" olan "+ str(i[0]) + " kodlu dersin kontenjanı " + str(i[2])+" kişidir.")


# Alternatif 1
for ders_kodu, kredi, kontenjan in zip(ders_kodu,kredi,kontenjan):
    print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")

#Alternatif 2
ders_bilgisi = list(zip(kredi, ders_kodu, kontenjan))

for ders in ders_bilgisi:
    print("Kredisi ", ders[0], " olan ", ders[1], " kodlu dersin kontenjanı ", ders[2], " kişidir")

###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise
# 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def kume_kapsama(kume1,kume2):
    if kume1.issuperset(kume2) == True:
        print("Kesisim: ", kume1.intersection(kume2))
    else:
        print("Fark: ", kume2.difference(kume1))

kume_kapsama(kume1,kume2)


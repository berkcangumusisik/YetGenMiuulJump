print("Hello World")

print("Hello AI Era")
# print() fonksiyonu ile ekrana çıktı vermeyi sağlar.
"""
 Pycharmda belli alanı çalıştırmak için çalıştırmak istediğimiz alanı seçip sağ tık ile "Execute Selection in Python" diyerek ya da alt + shift+ e ile o alanı console üzerinden çalıştırabiliyoruz.
 
"""

# Sayılar(Numbers) ve Karakter Dizileri(String)

"""
String metinsel ifadelerdir ve tırnak içerisinde yazılır.
Numbers sayısal ifadelerdir ve tırnak içinde yazzılmaz. 3 adettir.
Numbers:
    - integer : tam sayıları ifade eder 3, 5, 7
    - float : ondaklıklı sayılardır. 3.4, 0.0, -32.2 
"""

print(9)
9.2

type(9.2) # type() bir ifadenin tip bilgisine erişmeyi sağlar.

type("MRB")

# Atamlar ve Değişkenler
"""
Atama işlemi bir değişkene bir değer atamak demektir.
değişken_adi = değer

Değişkenler bir değeri tutmak için ve bir nesneyi tanımlamak için kullanılır.
"""

a = 9
a
b = "Hello AI Era"
b

c = 10
a * c
a * 9
a - c

# Virtual Environment (Sanal Ortam)
"""
- İzole çalışma ortamı oluşturmak için kullanılan bir araçtır.
- Projeler arası bağımlılıkları ortadan kaldırmak için kullanılır.
- Örneğin bir projede python 3.7 kullanıyorsak diğer projede python 3.8 kullanabiliriz.
- conda, venv, virtualenv, pipenv gibi çeşitleri vardır.
"""

# Package Management (Paket Yönetimi)
"""
- Paket yönetimi bir yazılımın bağımlılıklarını yönetmek için kullanılır.
- Örneğin bir projede pandas kütüphanesini kullanıyorsak bu kütüphanenin bağımlılıklarını da yüklememiz gerekir.
- pip, conda, pipenv gibi çeşitleri vardır. 

"""

# Sanal Ortamlar ile Paket Yönetimi Araçlarının İlişkisi
"""
- conda ve pipenv hem sanal ortam oluşturur hem de paket yönetimini yapar.
- venv ve virtualenv paket yönetimi konusunda pip kullanır.
- pip sadece paket yönetimini yapar.
- conda hem sanal ortam oluşturur hem de paket yönetimini yapar.
"""

# Virtual Environment Kurulumu
"""
- conda env list ile kurulu sanal ortamları görebiliriz.
- conda create -n <env_name> python=<version> ile sanal ortam oluşturabiliriz.
- conda activate <env_name> ile sanal ortamı aktif edebiliriz.
- conda deactivate ile sanal ortamı deaktif edebiliriz.
- conda list ile kurulu paketleri görebiliriz.
- conda install <package_name> ile paket kurabiliriz.
- conda install <package_name>=<version> ile paket kurabiliriz.
- conda remove <package_name> ile paket silebiliriz.
- conda install <package_name>,<package_name> ile birden fazla paket kurabiliriz.
- conda upgrade <package_name> ile paket güncelleyebiliriz.
- conda upgrade --all ile tüm paketleri güncelleyebiliriz.

pip : pypi(python package index) üzerinden paketleri kurar.
pip list ile kurulu paketleri görebiliriz.
pip install <package_name> ile paket kurabiliriz.
pip install <package_name>==<version> ile paket kurabiliriz.
"""
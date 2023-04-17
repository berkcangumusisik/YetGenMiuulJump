"""
Makine Öğrenmesine Giriş
- Makine öğrenmesi, bilgisayarların insanlara benzer şekilde öğrenmek maksadıyla çeşitli algoritma ve tekniklerin geliştirilmesi için çalışan bir bilim dalıdır.
Değişken Türleri
- Sayısal Değişkenler: Yaş fiyat vb. kesiklidir.
- Kategorik Değişkenler(Nominal, Ordinal) : Kadın erkek vb. gibi. Kadın erkek nominal, 1. sınıf 2. sınıf 3. sınıf ordinal
- Bağımlı Değişken(target, dependent, output, response): Tahmin edilmek istenen değişken.
- Bağımsız Değişken(predictor, independent, input, feature): Bağımlı değişkeni tahmin etmek için kullanılan değişkenler.
Öğrenme Türleri
- Pekiştirmeli Öğrenme(Reinforcement Learning)

Bir robot düşünelim. Bir kapalı odaya kapatılarak bu odadan çıkması isteniyor. Başarısız her denemede cezalandırılıyor. Robotun pekiştirme yoluyla odadan çıkmasını sağlatmak örnek verilebilir.
Deneme - yanılmaya dayanır.
- Denetimli öğrenme(Supervised Learning)

Denetimli Öğrenme algoritmasındaki en önemli nokta etiketli bir veri kümesi (labeled dataset) kullanılmasıdır.
- Denetimsiz öğrenme(Unsupervised Learning)
Etiketli bir veri kümesi olmadan veri kümesi kullanılmasıdır.


Problem Türleri
- Regresyon problemlerinde bağımlı değişken sayısaldır.
- Sınıflandırma problemlerinde bağımlı değişken kategorik.
Model Başarı Değerlendirme Yöntemleri
Tahminler ne kadar başarılı sorusuna cevap aranır.
Model Doğrulama Yöntemleri
*  Sınama Seti Yöntemi (Holdout Method):
Veri seti, eğitim seti ve test seti olarak ikiye bölünür.
Eğitim seti üzerinde modelleme işlemi yani eğitim işlemi (Train) gerçekleştirilir.
Model burada öğrenir.
Daha sonra ilgili model test setinden sorular sorulur ve model test edilir.
Bu şekilde iki setin başarısı değerlendirilir.
K-Katlı Çapraz Doğrulama (K-Fold Cross Validation)

- Özellikle veri seti az olduğunda eğitim ve test setinin bölünme işlemlerinde test setinin taşıdığı bilgilerin verimliliği sorgulanabilir.
- Bu kapsamda Holdout metoduna alternatif olarak K-Katlı Çapraz Doğrulama Yöntemi Kullanılır. Bu yöntem iki şekilde kullanılabilir:

Birinci Metot: (Çapraz Doğrulama)

Orijinal veri seti 5 eşit parçaya bölünür.
1,2,3,4,5 numaralı parçalardan 1,2,3,4 numaralı ile model kurulur. 5 numaralı parça ile test edilir.
Ardından 1,2,3,5 numaralı parça ile model kurulur ve 4 numaralı parça ile test edilir.
Ardından 1,2,4,5 numara model, 3 numara test, 1,3,4,5 numara model ve 2 numara test ve son olarak 2,3,4,5 numaralı parça model ve 1 numaralı parça test için kullanılır.
Testlerin hatalarının ve başarılarının ortalaması alınır ve Cross Validation hatası bulunur.
İkinci Metot: Özellikle zengin ve bol gözlem değerine sahip bir veri setinde çalışıldığında yaygın bir kullanıma sahiptir.

Veri Seti, Eğitim ve Test seti olacak şekilde ikiye bölünür.
Eğitim setine birinci metottaki Çapraz Doğrulama (Cross Validation) uygulanır.

En son modelin hiç görmediği Test seti ile tekrar test edilir.

"""
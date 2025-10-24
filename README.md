# ipTables Log Arama Aracı

Bu Python betiği, `ipTables.log` dosyalarını analiz ederek belirli IP adreslerinin tespiti için tasarlanmıştır. Arama sonuçları, okunabilirliği artırmak amacıyla ilgili IP adresinin vurgulandığı bir HTML raporu olarak oluşturulur.

## Temel Özellikler

* **IP Adresi Tespiti:** Belirtilen bir IP adresini log dosyası içerisinde arar.
* **Yön Filtreleme:** Arama işlemi, trafiğin yönüne göre (`Source`, `Destination` veya `Any`) filtrelenebilir.
* **HTML Raporlama:** Eşleşen log kayıtları, aranan IP adresi vurgulanarak yapılandırılmış bir HTML dosyasına (`sonuc.html`) aktarılır.
* **Komut Satırı Arayüzü:** Betik, kullanıcıdan gerekli IP adresi ve arama tipi parametrelerini komut satırı aracılığıyla talep eder.

## Sistem Gereksinimleri

* Python 3.x sürümü gereklidir.

Betik, Python standart kütüphanesi (`re`) dışında harici bir bağımlılık gerektirmez.

## Kullanım Talimatları

1.  Projeyi yerel makinenize klonlayınız veya dosyaları indiriniz:
    ```bash
    git clone [https://github.com/enesdolgun33/IpTables-Log-Searcher](https://github.com/enesdolgun33/IpTables-Log-Searcher)
    cd IpTables-Log-Searcher
    ```
   

2.  Analiz edilecek `ipTables.log` dosyasının, betik dosyası (`ipTables-Log-Searcher.py`) ile aynı dizinde bulunduğundan emin olunuz. (Depoda test amacıyla örnek bir `ipTables.log` dosyası mevcuttur.)

3.  Komut satırı veya terminal üzerinden betiği çalıştırınız:
    ```bash
    python ipTables-Log-Searcher.py
    ```

4.  İstendiğinde, aranacak hedef IP adresini belirtilen formatta giriniz:
    ```
    Lütfen aranacak IP adresini girin (örn: 192.168.2.89): 192.168.2.89
    ```

5.  Ardından, arama tipini (`Source`, `Destination` veya `Any`) belirtiniz:
    ```
    Arama tipini seçin (Source/Destination/Any): Any
    ```

6.  İşlem tamamlandığında, sonuçları içeren `sonuc.html` dosyası aynı dizinde oluşturulacaktır. Bu dosya, bir web tarayıcısı kullanılarak görüntülenebilir.

## Log Dosyası Formatı Hakkında Not

Bu betik, log satırlarının `SRC=` ve `DST=` anahtar kelimelerini içeren belirli bir formatta olduğunu varsaymaktadır. Örnek log satırları aşağıdaki gibidir:

Oct 16 09:06:23 raspberrypi kernel: [17367.419780] IN=wlan0 OUT= MAC=b8:27:eb:8c:4a:cc:2c:3a:e8:08:71:ad:08:00 SRC=192.168.2.89 DST=192.168.2.233 LEN=44 TOS=0x00 PREC=0x00 TTL=255 ID=3 PROTO=TCP SPT=49153 DPT=8080 WINDOW=2144 RES=0x00 SYN URGP=0 Oct 16 09:06:46 raspberrypi kernel: [17390.521244] IN=wlan0 OUT= MAC=b8:27:eb:8c:4a:cc:2c:3a:e8:08:71:ad:08:00 SRC=192.168.2.89 DST=192.168.2.233 LEN=44 TOS=0x00 PREC=0x00 TTL=255 ID=2 PROTO=TCP SPT=49153 DPT=8080 WINDOW=2144 RES=0x00 SYN URGP=0

Eğer kullanılan log dosyası formatı bu yapıdan farklı ise, `ipTables-Log-Searcher.py` dosyasındaki `find_ip_in_log` fonksiyonu içerisindeki düzenli ifade (regex) desenlerinin (`re.search` ile başlayan satırlar) güncellenmesi gerekebilir.

## Lisans Bilgisi

Bu proje, MIT Lisansı koşulları altında dağıtılmaktadır. Lisansın tam metni için (varsa) `LICENSE` dosyasına başvurulabilir.

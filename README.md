# watepy
Python script untuk menambahkan logo watermark pada gambar. 
Implementasi dan uji coba digunakan untuk manambahkan watermark untuk photo produk ecommerce

### Requirements
Pillow:
```
pip install pillow
```
[Pillow Docs](https://python-pillow.github.io/)

### Penggunaan
script ini akan menambahkan watermark pada gambar didalam satu folder yang spesifik. 
1. folder watermark besirikan logo yang akan menjadi watermark
2. folder photo berisikan photo yang akan akan ditambahkan watermark, bisa dalam sub-sub folder diphoto
3. posisi dari waterwark secara default akan mengarah ketengah, untuk merubahnya silahkan langsung edit dikoding dan ada referensi untuk posisi-posisi yang lainnya.
4. untuk ukuran watermark usahakan squere dan untuk pembesaran logo watermark silahkan persentase 50% ditingkatkan.
5. Hasil export dapat dilihat difolder output

### Last Update
- optimasi auto resize logo watermark untuk potrait dan landscape
- pembaharuan deteksi posisi gambar untuk resize logo watermark (19 mar 20)

### Kelemahan (BUG)
- Untuk photo yang tidak jelas potrait atau landscape maka logo watermark akan kelihatan tidak simetris
- Hasil export masih dalam satu folder, Belum bisa mengexport dengan folder inputan yang sama (19 mar 20)

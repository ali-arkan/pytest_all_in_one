## README – test_all_in_one.py

Bu dosya, **Pytest** kullanarak üç farklı test türünü **tek bir dosyada** göstermeyi amaçlayan küçük bir örnektir:

1. **API Testi** – `requests` kütüphanesi ile REST API’den dönen JSON verisini doğrular.
2. **UI (Web) Testi** – `playwright` ile bir web sayfasına gidip başlığını kontrol eder.
3. **Veritabanı Testi** – `sqlite3` ile geçici (in-memory) bir veritabanında kayıt doğrulaması yapar.

---

### 📂 Dosya

* **test_all_in_one.py** : Tüm testler ve pytest fixture’ları tek dosyada yer alır.

---

### 🔧 Kurulum

1. Python 3.9+ kurulu olduğundan emin olun.
2. Gerekli kütüphaneleri yükleyin:

   ```bash
   pip install pytest requests playwright
   playwright install
   ```

   > `playwright install` tarayıcı binary’lerini indirir.

---

### ▶️ Testleri Çalıştırma

Aynı klasörde terminalden:

```bash
pytest -v test_all_in_one.py
```

* `-v` : Daha ayrıntılı çıktı verir.

---

### 🧩 Testlerin Görevleri

| Test fonksiyonu       | Açıklama                                                                                                   |
| --------------------- | ---------------------------------------------------------------------------------------------------------- |
| `test_api_user_check` | Demo API (`jsonplaceholder.typicode.com`) üzerinden bir kullanıcının `id` ve `email` alanını kontrol eder. |
| `test_ui_title_check` | `https://example.com` sayfasının başlığında **"Example Domain"** metni var mı doğrular.                    |
| `test_db_user_exists` | In-memory SQLite veritabanında **"Ali"** adında bir kullanıcı kaydının varlığını kontrol eder.             |

---

### 💡 Notlar

* Bu proje **eğitim ve demo** amaçlıdır.
* Gerçek projelerde Playwright veya Selenium için daha gelişmiş konfigürasyon ve raporlama kullanabilirsiniz.

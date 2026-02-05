# Flask Görev Yöneticisi (Advanced To-Do App)

Bu proje, kullanıcıların görevlerini öncelik sırasına, kategorilere ve teslim tarihlerine göre yönetmesini sağlayan bir web uygulamasıdır. **Python (Flask)** ve **SQLite** veri tabanı kullanılarak geliştirilmiştir.

## Proje Hakkında

Uygulama, temel **CRUD** (Oluşturma, Okuma, Güncelleme, Silme) işlemlerinin yanı sıra, kullanıcı deneyimini iyileştiren bir sıralama algoritması ve görsel arayüz geliştirmeleri içerir.

## Öne Çıkan Özellikler

* **Tam Kontrol (CRUD):** Görev ekleme, silme ve mevcut görevleri düzenleme (Edit) özelliği.
* **Akıllı Sıralama Algoritması:** Görevler otomatik olarak şu sıraya göre listelenir:
    1.  Tamamlanmamış Görevler
    2.  Öncelik Seviyesi (Yüksek > Düşük)
    3.  Tarih Yakınlığı
* **Öncelik Yönetimi:** Görevlere *Düşük*, *Orta* veya *Yüksek* öncelik atayabilme ve renkli etiketlerle görselleştirme.
* **Kategorilendirme:** *Okul*, *İş*, *Proje* gibi etiketlerle işleri gruplama.
* **Zaman Yönetimi:** Son tarih (Due Date) belirleme ve tarihi geçen görevler için otomatik **(!Gecikti)** uyarısı.
* **Arama (Search):** Görev başlıkları içinde anlık filtreleme yapabilme.
* **Arayüz:** Bootstrap 5 ile geliştirilmiş, tamamlanan görevlerin üzerini çizen ve soluklaştıran dinamik UI.

## Kullanılan Teknolojiler

Bu projede aşağıdaki teknolojiler kullanılmıştır:

| **Backend** | Python, Flask | Sunucu tarafı mantığı ve rota yönetimi. |
| **Veritabanı** | SQLite, SQLAlchemy | Veri saklama ve ORM yapısı. |
| **Frontend** | Bootstrap 5, HTML/CSS | Responsive tasarım ve hazır bileşenler. |
| **Template Engine** | Jinja2 | Dinamik HTML oluşturma. | | Dinamik HTML oluşturma. |

Nama : Velicia Willy

NPM : 2506657384

Kelas : PBP D

## Hyperlinks
1. [Tugas 1](#tugas-1)
2. [Tutorial 2](#tutorial-2)
3. [Tugas 2](#tugas-2)
4. [Tutorial 3](#tutorial-3)
5. [Tugas 3](#tugas-3)
6. [Tugas 4](#tugas-4)
7. [Tutorial 5](#tutorial-5)
8. [Tugas 5](#tugas-5)
9. [Tugas 6](#tugas-6)


## Tugas 1
### Perubahan
1. Mengubah color palette website
2. Menambahkan section skills, experience, dan projects
3. Mengubah tata letak elemen-elemen pada website
4. Menambahkan kredensial database di berkas .env.prod

### Pertanyaan Reflektif
1. Selain yang sudah ada di template yang diberikan asdos di tutorial 01, saya menggunakan elemen ul dan li untuk membuat bullet list pada section skills dan experience. Elemen tersebut membuat tampilan daftar skill dan experience saya terlihat lebih rapi dan mudah dibaca.
2. Tantangan tata letak yang saya temukan adalah menentukan letak yang pas bagi masing-masing section. Setelah menambahkan section-section baru (skills, experience, projects) di section hero-details, layout dari website menjadi tidak seimbang. Kolom sebelah kiri jadi memiliki lebih banyak konten daripada kolom sebelah kanan yang hanya berisi foto. Akhirnya, saya melakukan penyesuaian tata letak. Dalam proses penyesuaian, saya memindahkan beberapa elemen ke section lain dan membuat section baru. Saya juga mengubah grid-template-areas pada file css agar dapat menyusun section-section yang ada sesuai keinginan saya. Selain itu, ketika website dibuka dengan tampilan mobile, pengaturan tata letak yang sudah rapi di tampilan desktop jadi berantakan. Misalnya, margin yang membuat section skills memiliki jarak yang cukup dari foto pada tampilan desktop, mengakibatkan adanya jarak yang besar antara section skills dan section lainnya pada tampilan mobile sehingga harus di-override. Saat mengubah ke tampilan mobile, layout berubah menjadi satu kolom saja. Elemen paling penting (hero-identity dan hero-photo) saya letakkan paling atas agar menjadi hal pertama yang dilihat ketika website dibuka, diikuti oleh hero-info. Sisanya (skills, experience, dan projects) saya letakkan paling bawah karena baru akan dilihat setelah elemen-elemen lain dilihat.
3. Karena website merupakan static website, semua informasi yang ada di dalamnya sudah dituliskan langsung di file html. Hal ini berarti, jika saya ingin mengubah informasi yang ada di website, saya harus mengubah kode html saya dan melakukan push lagi ke pws. Hal ini tentunya tidak efisien. Andai website saya bersifat dynamic, saya hanya perlu mengubah informasi yang ada di database untuk mengubah informasi yang ada di website. Selain itu, saya juga ingin agar tampilan website saya bisa berubah sesuai dengan keinginan pengunjung website. Saya ingin menambahkan toggle untuk mengganti tampilan website ke dark mode pada tugas-tugas berikutnya. 

### AI Disclosure
Saya tidak menggunakan AI untuk tugas ini.
Berikut masalah yang muncul dan cara saya mengatasinya:

Saya sempat bingung dengan tata letak (grid) dari proyek ini. Saya ingin membuat foto berada di sudut kanan atas halaman, bukan di tengah. Akan tetapi, saat saya mengubah properti align menjadi top pada file css, box shadow di bawah foto memanjang sampai ke bagian bawah halaman. Setelah membaca kembali dokumen tutorial 01 dengan saksama, saya mulai memahami tata letak dari proyek ini. Saya sadar bahwa section hero-photo menempati dua baris pada kolom yang sama. Hal ini menyebabkan pemanjangan box shadow tadi. Akhirnya, saya mengubah grid-template-areas untuk membuat section hero-photo jadi lebih kecil.

### Resources yang saya gunakan untuk tugas ini:
1. coolors.co -> untuk mencari color palette yang sesuai keinginan saya. Saya menggunakan color palette yang sudah ada, bukan yang di-generate oleh fitur AI pada website tersebut. Color palette yang saya gunakan: https://coolors.co/palette/393d3f-fdfdff-c6c5b9-62929e-546a7b
2. Aplikasi Font Book di Mac -> untuk mencari font yang sesuai keinginan saya.

## Tutorial 2
### Perubahan yang saya buat (selain yang diinstruksikan):
1. Menghapus section experience dari halaman profil dengan menghapus section tersebut dari index.html dan style.css.

## Tugas 2
### Perubahan
1. Mengubah bahasa pada seluruh website jadi bahasa Inggris.
2. Menghapus section Experience, Skill, dan Projects dari halaman Profile karena sudah dibuat halamannya masing-masing.
3. Menambahkan unit test untuk main page dan models Experience, Skill, dan Projects.

### Pertanyaan Reflektif
1. Saat client mengunjungi alamat/url web kita, url tersebut akan dipetakan oleh urls.py ke fungsi yang ada di views.py. Fungsi ini akan mengirimkan request beserta contextnya (informasi atau data yang akan mengisi placeholder) kepada template. Template yang sudah terisi oleh context inilah yang akan dikembalikan kepada client. urls.py proyek mendaftarkan path dari halaman admin dan halaman utama main, yaitu halaman profile. Sementara itu, urls.py aplikasi mendaftarkan halaman profile, experience, skill, dan projects.

2. Misalnya, ada 20 experience yang dimiliki. Jika semuanya ditulis di dalam template, maka akan ada banyak perulangan kode yang membuat file template panjang, sulit dibaca, dan tidak modular. Apabila kita ingin melakukan perubahan atau perbaikan pada template, misal menukar posisi kategori dengan informasi ongoing atau ended, kita harus melakukan perubahan tersebut satu per satu untuk 20 data experience yang kita miliki. Kita juga harus mengubah file html setiap kali ingin menambahkan data baru. Hal ini tentunya tidak efisien dan mempersulit diri kita sendiri. Oleh karena itu, data sebaiknya disimpan pada model dan template hanya diisi oleh placeholder yang akan diisi oleh data-data pada model.

3. Fungsi makemigrations berperan untuk mendata perubahan apa saja yang terjadi pada model dan melaporkannya kepada kita. Fungsi ini sama sekali tidak mengubah database kita. Sementara itu, fungsi migrate menerapkan perubahan yang ada pada database kita. Contohnya, saya menjalankan kedua perintah tersebut saat menambahkan models baru, yaitu Experience, Skill, dan Projects.

### AI Disclosure
Saya tidak menggunakan AI untuk tugas ini. Saya tidak menemukan banyak masalah saat mengerjakan tugas ini karena saya hanya menerapkan hal-hal yang saya pelajari pada tutorial 2.

### Resources yang saya gunakan untuk tugas ini:
1. Halaman tutorial 2 pada website PBP untuk referensi materi.
###

## Tutorial 3
### Perubahan:
1. Implementasi skeleton untuk index.html, projects.html, experience.html, skill.html, dan file .html lain yang dibuat pada tutorial ini.
2. Implementasi form untuk model Projects, Skill, dan Experience.
3. Implementasi data delivery dengan JSON untuk model Projects saja.

## Tugas 3
### Perubahan:
1. Implementasi delete data untuk Experience dan Skill (sudah diimplementasikan pada Projects di tutorial 3)
2. Implementasi data delivery dengan JSON untuk model Experience dan Skill.
3. Implementasi update data untuk Projects.

### Pertanyaan reflektif:
1. Kita menggunakan ModelForm karena sudah terhubung dengan class Model. Hal ini memungkinkan kita untuk menyambungkan field pada Model yang kita buat dengan field pada form sehingga mempermudah kita. csrf_token diperlukan untuk autentikasi agar server terlindungi dari request yang tidak terotorisasi. Tanpa csrf_token, pihak lain bisa me-redirect request menuju server kita ke suatu API lain yang bisa jadi berbahaya.
2. Karena datanya yang lebih mudah diproses karena berbentuk string dalam format key dan value. Pemrosesan data pada JSON juga didukung oleh sebagian besar bahasa pemrograman, terutama JavaScript yang sering digunakan dalam pemrograman web.
3. Pertama, client mengirimkan request untuk menampilkan halaman berisi data. Data tersebut kita ambil dari database kita dalam bentuk stream of Bytes (di-serialize). Setelah diterima oleh views, data di-deserialize ke dalam format JSON. Data JSON ini di-parse ke dalam bentuk objek dari model kita. Akhirnya, views mengembalikan halaman html yang di-request client beserta contextnya yang berisi data-data objek. Serialization mengubah sebuah objek ke dalam bentuk stream of Bytes. Hal ini memungkinkan data yang dibuat oleh suatu bahasa pemrograman untuk diproses oleh bahasa pemrograman lainnya. 

### AI Disclosure
Saya tidak menggunakan AI untuk tugas ini. Karena saya hanya menerapkan apa yang sudah dipelajari pada Tutorial 3, saya tidak menemukan masalah yang berarti dalam proses pengerjaan tugas ini. Akan tetapi, saya mengalami kesulitan saat ingin mengimplementasi update data (tidak dibahas pada tutorial). Implementasi update data mirip dengan create data, tapi, saya kebingungan akan cara membuat form otomatis terisi dengan data asli dari objek yang ingin kita update. Akhirnya, saya membaca artikel dari w3schools dan forum Stack Overflow untuk memahami cara melakukan update data JSON dengan menggunakan forms serta dokumentasi django untuk memahami widgets. Saya menemukan bahwa menambahkan argumen instance pada ProjectForm() menyelesaikan masalah tersebut.

### Resources:
1. https://www.w3schools.com/django/django_update_record.php 
2. https://stackoverflow.com/questions/42012115/how-to-initialize-a-django-form-with-values-from-a-model
3. https://docs.djangoproject.com/en/6.1/ref/forms/widgets/#django.forms.Widget.attrs 


## Tugas 4
### Perubahan dari Tutorial 4 dan Tugas 4:
1. Menambahkan fitur autentifikasi dan otorisasi untuk semua model.
2. Menerapkan toggle star untuk model Projects dan Experience.
3. Memperbaiki tampilan rusak/tidak rapi saat ukuran window kecil dengan membuat horizontal scroll menu untuk navigation bar.

### AI Disclosure
Saya tidak menggunakan AI untuk tugas ini. Karena saya hanya menerapkan apa yang sudah dipelajari pada Tutorial 3, saya tidak menemukan masalah yang berarti dalam proses pengerjaan tugas ini. 

### Troubleshooting
Saat saya mengecilkan ukuran window, saya menemukan bahwa tampilan web, khususnya bagian navigation bar, jadi tidak rapi. Sebagian dari navigation bar jadi berada di luar layar sehingga tidak terlihat oleh pengguna. Saya mencari solusi untuk masalah ini dengan mengunjungi web w3schools dan melihat-lihat tipe menu bar yang bisa saya buat seperti apa. Saya memilih implementasi yang paling mudah dan tidak memerlukan banyak perubahan kode, yaitu horizontal scroll menu. Saya menetapkan properti overflow sebagai auto, yang akan otomatis menambahkan scrollbar jika diperlukan (saat ada yang keluar layar). Saya juga menetapkan properti whitespace sebagai nowrap agar semua kata ada di baris yang sama.

### Resources
1. https://www.w3schools.com/howto/howto_css_menu_horizontal_scroll.asp
2. https://www.w3schools.com/css/css_overflow.asp
3. https://www.w3schools.com/CSSref/pr_text_white-space.php


## Tutorial 5
### Perubahan:
1. Mengimplementasikan toast
2. Menerapkan debouncing pada search bar halaman Projects
3. Menampilkan data Projects dengan AJAX. Fungsi get_projects_json diperbarui agar dapat merakit JSON secara manual. Fungsi show_projects disederhanakan karena tidak lagi perlu mengirimkan data projects. Mengubah projects.html agar menjadi template untuk AJAX. Menambahkan script AJAX inline untuk merakit sendiri data JSON yang dikirimkan fungsi pada views.
4. Mengubah penambahan proyek baru yang tadinya melalui halaman lain, jadi melalui modal.
5. Mengubah mekanisme penambahan data proyek dengan AJAX agar tidak terjadi perpindahan halaman ataupun reload browser saat pengguna men-submit form create projects.
6. Mengimplementasikan perlindungan website dari XSS.


## Tugas 5
### Perubahan:
1. Menambahkan search bar dengan debouncing pada halaman Skill.
2. Menampilkan data Skill dan Experience dengan AJAX. Fungsi-fungsi views yang berkaitan berubah seperti pada Tutorial 5.
3. Mengubah penambahan skill dan experience baru jadi melalui modal.
4. Mengubah mekanisme penambahan data skill dan experience dengan AJAX agar tidak terjadi perpindahan halaman ataupun reload browser saat pengguna men-submit form create projects.
5. Mengimplementasikan perlindungan website dari XSS untuk model Skill dan Experience.

### Pertanyaan Reflektif
1. Kita menggunakan mekanisme search bar yang langsung menampilkan hasil pencarian sehingga pengguna tidak perlu menekan tombol search. Debouncing atau penundaan sebelum pemanggilan search diperlukan agar halaman tidak terus-menerus mengirim request GET setiap kali pengguna mengetikkan sesuatu di search bar. Dengan teknik debouncing, halaman baru akan menampilkan hasil pencarian setelah sekian waktu pengguna berhenti mengetik (sekian waktu tanpa event input pada search bar).
2. Keyword await digunakan agar eksekusi kode setelah fetch() menunggu hingga fetch() selesai dieksekusi. Tanpa await, selagi menunggu selesainya eksekusi fetch() kode-kode berikutnya akan terus dieksekusi, dengan instruksi fetch() berlanjut di background. Hal ini harus dihindari jika misalnya, kode setelah fetch() adalah kode yang menampilkan data yang di-fetch. Jika kode penampilan data dieksekusi sebelum fetch() selesai dieksekusi, data yang ditampilkan bisa jadi tidak lengkap.
3. Serangan XSS adalah serangan di mana penyerang menyisipkan elemen executable (<script></script>) pada halaman web kita. Penyerang bisa menyisipkan elemen executable dari input form yang kemudian dibaca oleh halaman web ketika ingin menampilkan atau memroses data input sehingga isi dari script dieksekusi. Data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan XSS daripada data yang ditampilkan melalui html langsung karena tidak ada lagi Django yang melakukan auto-escaping html. Hal ini berbahaya untuk keamanan data dan fungsionalitas halaman kita sehingga harus kita mitigasi. Kita dapat memitigasinya dengan memastikan data yang ingin kita tampilkan pada halaman tidak memiliki tag html dengan melakukan input handling pada forms dan melakukan escaping secara manual pada kode AJAX.

### AI Disclosure
Saya tidak menggunakan AI untuk tugas ini. Saya mempelajari isi dari Tutorial 5 dengan baik. Kesulitan yang saya alami disebabkan karena typo saat menyalin kode pada Tutorial 5 dan mengadaptasinya sesuai dengan kebutuhan website saya. Kode yang disalin cukup panjang sehingga ada beberapa bagian yang tidak teradaptasi dengan baik. Misalnya, ```id="project-form"``` pada skill_form_modal.html lupa saya ganti menjadi ```id="skill=form"```, padahal pada skill.html, const skillForm memfilter berdasarkan id "skill-form" sehingga isi form tidak muncul karena objek form dianggap null. Saya menggunakan tab console pada fitur Inspect pada web untuk melacak letak typo saya di mana.

### Resources
1. Halaman Tutorial 5 PBP

## Tugas 6
### Perubahan yang terjadi setelah Tutorial 7 dan Tugas 6:
1. Mengimplementasi Serializer untuk model Projects, Experience, dan Skill.
2. Mengimplementasi Permissions untuk superuser, editor, dan pengguna biasa.
3. Mengimplementasikan API view dan url untuk operasi list, detail, dan star tanpa memuat ulang halaman pada ketiga model.
4. Mengganti mekanisme update model yang tadinya via form pada halaman lain, jadi melalui popup.
5. Menulis unit testing pada tests_api.py untuk menguji serializer, permissions, dan api views pada ketiga model.

### Pertanyaan Reflektif
1. REST atau REpresentational State Transfer adalah sebuah interface antara beberapa komponen berbeda, misalnya client dan server. Dia merupakan rancangan API yang mendefinisikan bagaimana komponen-komponen tersebut dapat berkomunikasi dengan satu sama lain. REST memiliki beberapa ketentuan. Oleh karena itu, mengembalikan JSON saja tidak cukup untuk membuat API disebut sebagai RESTful karena dia hanya menentukan format transfer data saja, bukan menentukan ketentuan komunikasi antar komponen. RESTful API menentukan bahwa url menunjukkan data, tidak seperti pada tutorial-tutorial sebelumnya di mana url menunjukkan aksi. Pada RESTful API, aksi ditunjukkan oleh HTTP method yang digunakan, misalnya GET untuk fetching data dan PATCH untuk mengubah sebagian data. Selain itu, komponen juga saling bertukar respon JSON, bukan objek Python atau baris database. Ada perbedaan antara PUT dan PATCH. PUT mengubah keseluruhan data, sementara PATCH hanya mengubah sebagian. Contoh aplikasinya adalah menggunakan PUT untuk mengubah keseluruhan data/field pada Project dan menggunakan PATCH untuk mengubah judul Project saja. Pada tugas ini, aksi update objek menggunakan PATCH agar perubahan yang terjadi di database hanya perubahan yang diperlukan (yang diubah user).
2. Serializer berperan untuk mengubah objek Python yang kompleks menjadi tipe data yang lebih sederhana seperti dictionary atau list yang kemudian diubah ke dalam format JSON dan sebaliknya. Menggunakan Serializer lebih mudah daripada merakit respons JSON secara manual karena perakitan respons JSON, kontrak data, dan validasinya sudah ditangani oleh Serializer. Penggunaan Serializer juga memudahkan maintenance kode karena perubahan pada Serializer akan langsung teraplikasikan ke seluruh program sehingga kita tidak perlu mengubah format JSON satu per satu. Selain itu, penggunaan Serializer juga mencegah terekposnya data sensitif pengguna seperti password karena Serializer dapat kita set agar tidak mengekspos data-data tersebut.
3. Autentikasi adalah proses yang mengidentifikasi siapa yang melakukan sesuatu, sementara otorisasi mengidentifikasi apakah seseorang berhak untuk melakukan sesuatu. Hak akses harus diperiksa dengan permission class. Menyembunyikan tombol saja tidak cukup karena pengguna dapat mengetikkan url menuju endpoint tertentu dan karena tidak ada otorisasi via permissions, pengguna yang seharusnya tidak bisa melakukan sesuatu (membaca data tertentu misalnya) dapat melakukan hal tersebut. Permission class mencegah pengguna yang tidak terotorisasi untuk melakukan sesuatu melalui url endpoint tersebut.
4. SessionAuthentication memverifikasi siapa yang mengirim suatu request, tapi tidak bisa memverifikasi dari mana request berasal. Jadi, seorang attacker bisa mengirim request dengan berpura-pura menjadi seorang pengguna menggunakan session cookie pengguna tersebut yang tersimpan di browser dan request ini diproses oleh server karena sessionnya terverifikasi. CSRF token mencegah hal ini terjadi karena merupakan string random yang di-generate oleh program dan hanya bisa diakses program. Karena attacker tidak bisa menebak string random ini, csrf tokennya akan invalid sehingga request dari attacker ditolak. Hal ini juga menjadi penyebab test yang menggunakan force_authenticate tidak cukup untuk membuktikan perlindungan CSRF berjalan karena hanya mengetes SessionAuthentication.

### AI Disclosure
Saya menggunakan Gemini AI untuk membantu saya membuat validator DateTimeField pada ExperienceSerializer. Saya menemukan bug di mana form menganggap field ended_at yang kosong memiliki value berupa string kosong alih-alih None.

Prompt: "I have this field in a ModelForm: ended_at = models.DateTimeField(blank=True, null=True). When I leave that field in the form empty, it causes an error with the datetime format. What could be wrong? I'm using a serializer"

Kode yang diberikan AI dan saya pakai langsung:
```
def to_internal_value(self, data):
        # Frontend FormData is often immutable, so we make a mutable copy
        mutable_data = data.copy()
        
        # If the frontend sent an empty string, convert it to None
        if mutable_data.get('ended_at') == '':
            mutable_data['ended_at'] = None
            
        return super().to_internal_value(mutable_data)
```

Kode tersebut mengganti string kosong yang mungkin diperoleh dari field ended_at ke None sehingga tidak menimbulkan error pada datetime format.

Selain itu, saya juga meminta bantuan AI untuk membuat validator pada ExperienceSerializer yang memastikan bahwa tanggal ended_at lebih besar dari tanggal started_at.

Prompt: "I have a DateTimeField in my serializer. How do I make sure that ended_at is after started_at? How would the validate function look like?"

Kode yang diberikan AI yang saya adaptasi ke kode saya:
```
def validate(self, data):
    # 1. Safely extract values. 
    # Using self.instance fallback ensures this works for PATCH (partial updates)
    # where the user might only be updating one of the two dates.
    started_at = data.get('started_at', getattr(self.instance, 'started_at', None))
    ended_at = data.get('ended_at', getattr(self.instance, 'ended_at', None))

    # 2. Perform the comparison if both dates exist
    if started_at and ended_at:
        if ended_at <= started_at:
            # Passing a dictionary attaches the error directly to the 'ended_at' 
            # field in the JSON response, rather than 'non_field_errors'
            raise serializers.ValidationError({
                "ended_at": "The end date must be after the start date."
            })

    return data
```

Link percakapan saya dengan Gemini AI: https://gemini.google.com/share/d/1-QZuRk17yzzcoay0FB9BkvUTLfA8qpF3?usp=sharing 

### Resources
1. Halaman Tutorial 7 PBP
Nama : Velicia Willy

NPM : 2506657384

Kelas : PBP D

### Tugas 1
Perubahan
1. Mengubah color palette website
2. Menambahkan section skills, experience, dan projects
3. Mengubah tata letak elemen-elemen pada website
4. Menambahkan kredensial database di berkas .env.prod

Pertanyaan Reflektif
1. Selain yang sudah ada di template yang diberikan asdos di tutorial 01, saya menggunakan elemen ul dan li untuk membuat bullet list pada section skills dan experience. Elemen tersebut membuat tampilan daftar skill dan experience saya terlihat lebih rapi dan mudah dibaca.

2. Tantangan tata letak yang saya temukan adalah menentukan letak yang pas bagi masing-masing section. Setelah menambahkan section-section baru (skills, experience, projects) di section hero-details, layout dari website menjadi tidak seimbang. Kolom sebelah kiri jadi memiliki lebih banyak konten daripada kolom sebelah kanan yang hanya berisi foto. Akhirnya, saya melakukan penyesuaian tata letak. Dalam proses penyesuaian, saya memindahkan beberapa elemen ke section lain dan membuat section baru. Saya juga mengubah grid-template-areas pada file css agar dapat menyusun section-section yang ada sesuai keinginan saya. Selain itu, ketika website dibuka dengan tampilan mobile, pengaturan tata letak yang sudah rapi di tampilan desktop jadi berantakan. Misalnya, margin yang membuat section skills memiliki jarak yang cukup dari foto pada tampilan desktop, mengakibatkan adanya jarak yang besar antara section skills dan section lainnya pada tampilan mobile sehingga harus di-override. Saat mengubah ke tampilan mobile, layout berubah menjadi satu kolom saja. Elemen paling penting (hero-identity dan hero-photo) saya letakkan paling atas agar menjadi hal pertama yang dilihat ketika website dibuka, diikuti oleh hero-info. Sisanya (skills, experience, dan projects) saya letakkan paling bawah karena baru akan dilihat setelah elemen-elemen lain dilihat.

3. Karena website merupakan static website, semua informasi yang ada di dalamnya sudah dituliskan langsung di file html. Hal ini berarti, jika saya ingin mengubah informasi yang ada di website, saya harus mengubah kode html saya dan melakukan push lagi ke pws. Hal ini tentunya tidak efisien. Andai website saya bersifat dynamic, saya hanya perlu mengubah informasi yang ada di database untuk mengubah informasi yang ada di website. Selain itu, saya juga ingin agar tampilan website saya bisa berubah sesuai dengan keinginan pengunjung website. Saya ingin menambahkan toggle untuk mengganti tampilan website ke dark mode pada tugas-tugas berikutnya.\n\nSaya tidak menggunakan AI untuk tugas ini.
Berikut masalah yang muncul dan cara saya mengatasinya:
Saya sempat bingung dengan tata letak (grid) dari proyek ini. Saya ingin membuat foto berada di sudut kanan atas halaman, bukan di tengah. Akan tetapi, saat saya mengubah properti align menjadi top pada file css, box shadow di bawah foto memanjang sampai ke bagian bawah halaman. Setelah membaca kembali dokumen tutorial 01 dengan saksama, saya mulai memahami tata letak dari proyek ini. Saya sadar bahwa section hero-photo menempati dua baris pada kolom yang sama. Hal ini menyebabkan pemanjangan box shadow tadi. Akhirnya, saya mengubah grid-template-areas untuk membuat section hero-photo jadi lebih kecil.

Resources yang saya gunakan untuk tugas ini:
1. coolors.co -> untuk mencari color palette yang sesuai keinginan saya. Saya menggunakan color palette yang sudah ada, bukan yang di-generate oleh fitur AI pada website tersebut. Color palette yang saya gunakan: https://coolors.co/palette/393d3f-fdfdff-c6c5b9-62929e-546a7b
2. Aplikasi Font Book di Mac -> untuk mencari font yang sesuai keinginan saya.
###

### Tutorial 02
Perubahan yang saya buat (selain yang diinstruksikan):
1. Menghapus section experience dari halaman profil dengan menghapus section tersebut dari index.html dan style.css.
###

### Tugas 2
Perubahan
1. Mengubah bahasa pada seluruh website jadi bahasa Inggris.
2. Menghapus section Experience, Skill, dan Projects dari halaman Profile karena sudah dibuat halamannya masing-masing.
3. Menambahkan unit test untuk main page dan models Experience, Skill, dan Projects.

Pertanyaan Reflektif
1. Saat client mengunjungi alamat/url web kita, url tersebut akan dipetakan oleh urls.py ke fungsi yang ada di views.py. Fungsi ini akan mengirimkan request beserta contextnya (informasi atau data yang akan mengisi placeholder) kepada template. Template yang sudah terisi oleh context inilah yang akan dikembalikan kepada client. urls.py proyek mendaftarkan path dari halaman admin dan halaman utama main, yaitu halaman profile. Sementara itu, urls.py aplikasi mendaftarkan halaman profile, experience, skill, dan projects.

2. Misalnya, ada 20 experience yang dimiliki. Jika semuanya ditulis di dalam template, maka akan ada banyak perulangan kode yang membuat file template panjang, sulit dibaca, dan tidak modular. Apabila kita ingin melakukan perubahan atau perbaikan pada template, misal menukar posisi kategori dengan informasi ongoing atau ended, kita harus melakukan perubahan tersebut satu per satu untuk 20 data experience yang kita miliki. Kita juga harus mengubah file html setiap kali ingin menambahkan data baru. Hal ini tentunya tidak efisien dan mempersulit diri kita sendiri. Oleh karena itu, data sebaiknya disimpan pada model dan template hanya diisi oleh placeholder yang akan diisi oleh data-data pada model.

3. Fungsi makemigrations berperan untuk mendata perubahan apa saja yang terjadi pada model dan melaporkannya kepada kita. Fungsi ini sama sekali tidak mengubah database kita. Sementara itu, fungsi migrate menerapkan perubahan yang ada pada database kita. Contohnya, saya menjalankan kedua perintah tersebut saat menambahkan models baru, yaitu Experience, Skill, dan Projects.

AI Disclosure
Saya tidak menggunakan AI untuk tugas ini. Saya tidak menemukan banyak masalah saat mengerjakan tugas ini karena saya hanya menerapkan hal-hal yang saya pelajari pada tutorial 2.

Resources yang saya gunakan untuk tugas ini:
1. Halaman tutorial 2 pada website PBP untuk referensi materi.
###

### Tutorial 3
Perubahan:
1. Implementasi skeleton untuk index.html, projects.html, experience.html, skill.html, dan file .html lain yang dibuat pada tutorial ini.
2. Implementasi form untuk model Projects, Skill, dan Experience.
3. Implementasi data delivery dengan JSON untuk model Projects saja.
###

### Tugas 3
Perubahan:
1. Implementasi delete data untuk Experience dan Skill (sudah diimplementasikan pada Projects di tutorial 3)
2. Implementasi data delivery dengan JSON untuk model Experience dan Skill.
3. Implementasi update data untuk Projects.

Pertanyaan reflektif:
1. Kita menggunakan ModelForm karena sudah terhubung dengan class Model. Hal ini memungkinkan kita untuk menyambungkan field pada Model yang kita buat dengan field pada form sehingga mempermudah kita. csrf_token diperlukan untuk autentikasi agar server terlindungi dari request yang tidak terotorisasi. Tanpa csrf_token, pihak lain bisa me-redirect request menuju server kita ke suatu API lain yang bisa jadi berbahaya.
2. Karena datanya yang lebih mudah diproses karena berbentuk string dalam format key dan value. Pemrosesan data pada JSON juga didukung oleh sebagian besar bahasa pemrograman, terutama JavaScript yang sering digunakan dalam pemrograman web.
3. Pertama, client mengirimkan request untuk menampilkan halaman berisi data. Data tersebut kita ambil dari database kita dalam bentuk stream of Bytes (di-serialize). Setelah diterima oleh views, data di-deserialize ke dalam format JSON. Data JSON ini di-parse ke dalam bentuk objek dari model kita. Akhirnya, views mengembalikan halaman html yang di-request client beserta contextnya yang berisi data-data objek. Serialization mengubah sebuah objek ke dalam bentuk stream of Bytes. Hal ini memungkinkan data yang dibuat oleh suatu bahasa pemrograman untuk diproses oleh bahasa pemrograman lainnya. 

AI Disclosure
Saya tidak menggunakan AI untuk tugas ini. Karena saya hanya menerapkan apa yang sudah dipelajari pada Tutorial 3, saya tidak menemukan masalah yang berarti dalam proses pengerjaan tugas ini. Akan tetapi, saya mengalami kesulitan saat ingin mengimplementasi update data (tidak dibahas pada tutorial). Implementasi update data mirip dengan create data, tapi, saya kebingungan akan cara membuat form otomatis terisi dengan data asli dari objek yang ingin kita update. Akhirnya, saya membaca artikel dari w3schools dan forum Stack Overflow untuk memahami cara melakukan update data JSON dengan menggunakan forms serta dokumentasi django untuk memahami widgets. Saya menemukan bahwa menambahkan argumen instance pada ProjectForm() menyelesaikan masalah tersebut.

Resources:
1. https://www.w3schools.com/django/django_update_record.php 
2. https://stackoverflow.com/questions/42012115/how-to-initialize-a-django-form-with-values-from-a-model
3. https://docs.djangoproject.com/en/6.1/ref/forms/widgets/#django.forms.Widget.attrs 
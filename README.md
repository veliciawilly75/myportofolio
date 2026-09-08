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

2. Tantangan tata letak yang saya temukan adalah menentukan letak yang pas bagi masing-masing section. Setelah menambahkan section-section baru (skills, experience, projects) di section hero-details, layout dari website menjadi tidak seimbang. Kolom sebelah kiri jadi memiliki lebih banyak konten daripada kolom sebelah kanan yang hanya berisi foto. Akhirnya, saya melakukan penyesuaian tata letak. Dalam proses penyesuaian, saya memindahkan beberapa elemen ke section lain dan membuat section baru. Saya juga mengubah grid-template-areas pada file css agar dapat menyusun section-section yang ada sesuai keinginan saya. Selain itu, ketika website dibuka dengan tampilan mobile, pengaturan tata letak yang sudah rapi di tampilan desktop jadi berantakan. Misalnya, margin yang membuat section skills memiliki jarak yang cukup dari foto pada tampilan desktop, mengakibatkan adanya jarak yang besar antara section skills dan section lainnya pada tampilan mobile sehingga harus di-override.

Saat mengubah ke tampilan mobile, layout berubah menjadi satu kolom saja. Elemen paling penting (hero-identity dan hero-photo) saya letakkan paling atas agar menjadi hal pertama yang dilihat ketika website dibuka, diikuti oleh hero-info. Sisanya (skills, experience, dan projects) saya letakkan paling bawah karena baru akan dilihat setelah elemen-elemen lain dilihat.

3. Karena website merupakan static website, semua informasi yang ada di dalamnya sudah dituliskan langsung di file html. Hal ini berarti, jika saya ingin mengubah informasi yang ada di website, saya harus mengubah kode html saya dan melakukan push lagi ke pws. Hal ini tentunya tidak efisien. Andai website saya bersifat dynamic, saya hanya perlu mengubah informasi yang ada di database untuk mengubah informasi yang ada di website. Selain itu, saya juga ingin agar tampilan website saya bisa berubah sesuai dengan keinginan pengunjung website. Saya ingin menambahkan toggle untuk mengganti tampilan website ke dark mode pada tugas-tugas berikutnya.

Saya tidak menggunakan AI untuk tugas ini.
Berikut masalah yang muncul dan cara saya mengatasinya:
Saya sempat bingung dengan tata letak (grid) dari proyek ini. Saya ingin membuat foto berada di sudut kanan atas halaman, bukan di tengah. Akan tetapi, saat saya mengubah properti align menjadi top pada file css, box shadow di bawah foto memanjang sampai ke bagian bawah halaman. Setelah membaca kembali dokumen tutorial 01 dengan saksama, saya mulai memahami tata letak dari proyek ini. Saya sadar bahwa section hero-photo menempati dua baris pada kolom yang sama. Hal ini menyebabkan pemanjangan box shadow tadi. Akhirnya, saya mengubah grid-template-areas untuk membuat section hero-photo jadi lebih kecil.

Resources yang saya gunakan untuk tugas ini:
1. coolors.co -> untuk mencari color palette yang sesuai keinginan saya. Saya menggunakan color palette yang sudah ada, bukan yang di-generate oleh fitur AI pada website tersebut. Color palette yang saya gunakan: https://coolors.co/palette/393d3f-fdfdff-c6c5b9-62929e-546a7b
2. Aplikasi Font Book di Mac -> untuk mencari font yang sesuai keinginan saya.
###

### Tutorial 02
Perubahan yang saya buat (selain yang diinstruksikan):
1. Menghapus section experience dari halaman profil dengan menghapus section tersebut dari index.html da style.css.
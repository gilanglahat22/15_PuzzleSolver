# Tugas Kecil 3 IF2211 Strategi Algoritma : Penyelesaian 15 Puzzle dengan Algoritma Branch and Bound

## 15-Puzzle
15-Puzzle adalah salah satu permainan dengan menggunakan papan yang berisikan angka 1 sampai 15 dalam 16 bagian ubin. Terdapat satu ubin kosong yang dapat digerakkan ke atas, bawah, kiri, dan kanan untuk menggeser ubin lainnya. Tujuan yang dicapai dari permainan ini adalah menyusun angka 1 sampai 15 terurut dari atas ke bawah dengan cara menggeser ubin kosong. 

## Algoritma Branch and Bound
Algoritma Branch and Bound merupakan salah satu strategi algoritma yang dipakai untuk menyelesaikan masalah optimasi. Algoritma ini menggunakan pohon ruang status untuk melakukan pencarian solusi terbaik. Perjalanan dalam pencarian status solusi menggunakan usaha yang paling optimal. Salah satu penerapan algoritma ini adalah dalam menyelesaikan persoalan 15-Puzzle.

## Requirement Program
```
  - Python 3
  - Library tkinter
```

## Cara penggunaan Program
Pertama-tama clone repository ini di local repository Anda dengan cara menjalankan perintah berikut

```
  git clone https://github.com/gilanglahat22/Tucil3_13520137.git
```
Setelah itu, anda bisa menjalankan programnya pada directory utama dari repositorynya dengan menjalankan perintah sebagai berikut di terminal Anda.

### Untuk Windows
Jika anda menggunakan terminal, maka anda bisa menjalankan perintah berikut.
```
 python src/Gui.py
```
## Untuk Linux
```
 $Python3 src/Gui.py
```

Atau jika anda menggunakan vscode (pastikan anda juga menginstall exstentionnya terlebih dahulu di vscode). 
    Adapun cara untuk mengerun file python di vscode dapat anda ikuti seperti tutorial pada link berikut ini : https://code.visualstudio.com/docs/python/python-tutorial

## Cara penggunaan Interface
Program yang dibuat menggunakan interface berbasis GUI yang mana inputannya dilakukan langsung di GUI-nya. Sementara itu untuk outputnya, anda bisa mendapatkannya langsung di GUI-nya atau bisa dengan mengexport file .txt yang mana akan menghasilkan step penyelesaian dari problem puzzle yang diberikan. Sementara itu, di dalam GUI tersebut memiliki berbagai button yang memiliki fungsinya masing-masing. Adapun rincian button tersebut adalah sebagai berikut.
1. Select file : berfungsi untuk memilih file inputan .txt dari directory user
2. Solve : berfungsi untuk mengarahkan user kepada solusi dari inputan yang diberikan user
3. Export Solution : berfungsi untuk mengexport/mengesave step-step solusi
4. Details : berfungsi untuk mengarahkan user pada rincian hasil eksekusi program seperti nilai value fungsi kurang pada masing-masing iterasi, jumlah seluruh fungsi kurang, node yang dibangkitkan, dan waktu eksekusi program.
5. Visualize : berfungsi untuk memvisualisasikan step solusi yang dihasilkan dalam bentuk pergeseran ubin kosong pada puzzle
6. Reset : berfungsi untuk mereset bentuk susunan puzzle ke susunan awal (sesuai bentuk puzzle dari inputan user).

## Aturan pada file inputan
File inputan memiliki aturan sebagai berikut.
1. Isi file terdiri dari tepat 4 baris
2. Tiap baris terdiri dari tepat 4 bilangan yang dipisahkan oleh spasi
3. Bilangan yang terdapat di inputan tersebut merupakan permutasi dari 0..15
4. Untuk sel kosong yang terdapat dalam puzzle tersebut direpresentasikan dengan angka 0 pada file inputan
    

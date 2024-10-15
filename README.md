# Skrip Automasi MikroTik

Proyek ini adalah skrip Python yang mengotomatisasi tugas pada router MikroTik menggunakan pustaka Paramiko untuk komunikasi SSH. Skrip ini memungkinkan konfigurasi jarak jauh pada router, seperti menambahkan alamat IP.

## Fitur

- Terhubung ke router MikroTik melalui SSH
- Melakukan konfigurasi jarak jauh
- Fungsionalitas contoh termasuk menambahkan alamat IP

## Prasyarat

- Python 3.x
- Pustaka `paramiko`

Anda dapat menginstal pustaka Paramiko dengan:

```bash
pip install paramiko
```

## Cara Penggunaan

1. **Kloning repositori**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Jalankan skrip**:

   Eksekusi skrip dan ikuti petunjuk yang diberikan:

   ```bash
   python mikrotik.py
   ```

   Skrip akan meminta Anda untuk memasukkan informasi berikut:

   - **Alamat IP Router**: Alamat IP dari router MikroTik Anda.
   - **Username**: Nama pengguna untuk terhubung ke router.
   - **Password**: Kata sandi yang terkait dengan nama pengguna.
   - **Alamat IP yang Akan Ditambahkan**: (jika diminta) Alamat IP yang akan ditambahkan ke router.
   - **Interface**: Interface tempat alamat IP akan ditambahkan.

## Contoh

```plaintext
Masukan IP Router: 192.168.56.1
Masukan Username: admin
Masukan Password: ****
Masukan IP Address: 192.168.56.100/24
Masukan Interface: ether1
```

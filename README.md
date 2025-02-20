![Image](https://github.com/user-attachments/assets/1aad710f-cb9a-44fd-bdc9-2f77f0fa9f76)
# Auto Config Mikrotik Router Os
Proyek ini adalah skrip Python yang mengotomatisasi tugas pada router MikroTik menggunakan library Paramiko untuk berkomunikasi dengan routerOS melalui SSH. Skrip ini memungkinkan konfigurasi dasar jarak jauh pada router, seperti menambahkan alamat IP.

## Fitur

- Terhubung ke router MikroTik melalui SSH
- Melakukan konfigurasi jarak jauh
- Fungsionalitas contoh termasuk menambahkan alamat IP

## Prasyarat

- Python 3.13
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

2. **run skrip**:

   Eksekusi skrip dan ikuti petunjuk yang diberikan:

   ```bash
   python mikrotik.py
   ```

   Skrip akan meminta Anda untuk memasukkan informasi berikut:

   - **Alamat IP Router**: Alamat IP dari router MikroTik Anda.
   - **Username**: Nama pengguna untuk terhubung ke router.
   - **Password**: Kata sandi yang terkait dengan nama pengguna.

## Contoh

```plaintext
Masukan IP Router: 192.168.56.1
Masukan Username: admin
Masukan Password: ****
Masukan IP Address: 192.168.56.100/24
Masukan Interface: ether1
```
testtttttttttttt
test

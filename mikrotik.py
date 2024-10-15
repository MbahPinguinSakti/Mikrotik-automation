#!/usr/bin/python

import paramiko

def add_ip_address():
    # Mendapatkan input dari pengguna
    host = input('Masukan IP Router: ')
    usern = input('Masukan Username: ')
    passwd = input('Masukan Password: ')
    port = 22

    ip = input('Masukan IP Address: ')
    interface = input('Masukan nomor interface (1/2/3): ')

    # Membuat koneksi SSH
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Menghubungkan ke MikroTik
        ssh_client.connect(host, port=port, username=usern, password=passwd)

        # Menjalankan perintah untuk menambahkan IP Address
        command = f'/ip/address/add address={ip} interface=ether{interface}'
        ssh_client.exec_command(command)

        # Menampilkan daftar IP Address
        output = ssh_client.exec_command('/ip/address/print')[1].read().decode()
        print("Daftar IP Address:")
        print(output)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Menutup koneksi SSH
        ssh_client.close()

def dhcpClient():
    # Mendapatkan input dari pengguna
    host = input('Masukan IP Router: ')
    usern = input('Masukan Username: ')
    passwd = input('Masukan Password: ')
    port = 22

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Menghubungkan ke MikroTik
        ssh_client.connect(host, port=port, username=usern, password=passwd)

        # Meminta interface yang akan digunakan
        eth = input('Mau ether berapa? (1/2/3): ')

        # Menambahkan DHCP Client
        command = f'/ip/dhcp-client/add interface=ether{eth}'
        ssh_client.exec_command(command)

        # Menampilkan daftar DHCP Client
        output = ssh_client.exec_command('/ip/dhcp-client/print')[1].read().decode()
        print(output)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Menutup koneksi SSH
        ssh_client.close()

# Menentukan pilihan dari pengguna
choose = int(input("1. Menambahkan IP Address, \n2. Menambahkan DHCP Client\n: "))
if choose == 1:
    add_ip_address()
elif choose == 2:
    dhcpClient()
else:
    print('Invalid input')
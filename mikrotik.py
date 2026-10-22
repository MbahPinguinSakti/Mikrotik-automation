#!/usr/bin/env python3

from getpass import getpass

import paramiko
import pyfiglet


def run_command(ssh_client, command):
    """Jalankan perintah RouterOS, tunggu selesai, lalu kembalikan outputnya."""
    _, stdout, stderr = ssh_client.exec_command(command)
    output = stdout.read().decode() + stderr.read().decode()
    return output.strip()


def ask_interface(prompt):
    """Minta nomor ether (1/2/3) dan kembalikan nama interface, misal 'ether1'."""
    nomor = input(prompt).strip()
    if nomor.startswith('ether'):
        return nomor
    return f'ether{nomor}'


def add_ip_address(ssh_client):
    ip = input('Masukan IP Address (contoh 192.168.56.100/24): ').strip()
    interface = ask_interface('Masukan nomor interface (1/2/3): ')

    # Menjalankan perintah untuk menambahkan IP Address
    hasil = run_command(ssh_client, f'/ip/address/add address={ip} interface={interface}')
    if hasil:
        print(hasil)

    # Menampilkan daftar IP Address
    print("Daftar IP Address:")
    print(run_command(ssh_client, '/ip/address/print'))


def dhcp_client(ssh_client):
    interface = ask_interface('Mau ether berapa? (1/2/3): ')

    # add DHCP Client
    hasil = run_command(ssh_client, f'/ip/dhcp-client/add interface={interface}')
    if hasil:
        print(hasil)

    # show daftar DHCP Client
    print(run_command(ssh_client, '/ip/dhcp-client/print'))


def nat_masquerade(ssh_client):
    interface = ask_interface('out interface (1/2/3)?: ')

    hasil = run_command(
        ssh_client,
        f'/ip/firewall/nat/add chain=srcnat out-interface={interface} action=masquerade',
    )
    if hasil:
        print(hasil)

    print(run_command(ssh_client, '/ip/firewall/nat/print'))


def ip_info(ssh_client):
    print("menampilkan tabel ip address")
    print(run_command(ssh_client, '/ip/address/print'))


MENU = {
    '1': add_ip_address,
    '2': dhcp_client,
    '3': nat_masquerade,
    '4': ip_info,
}


def main():
    print(pyfiglet.figlet_format("ACMRO", font="alligator"))

    # input dari pengguna
    host = input('Masukan IP Router: ').strip()
    usern = input('Masukan Username: ').strip()
    passwd = getpass('Masukan Password: ')
    port = 22

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # connect ke mikrotik
        ssh_client.connect(host, port=port, username=usern, password=passwd)
    except Exception as e:
        print(f"Gagal terhubung ke {host}: {e}")
        return

    try:
        while True:
            choose = input(
                "\n1. Menambahkan IP Address\n"
                "2. Menambahkan DHCP Client\n"
                "3. Nat-masquerade firewall\n"
                "4. Menampilkan ip address router\n"
                "pilih salah satu atau ketik 0 untuk mengakhiri: "
            ).strip()

            if choose == '0':
                break

            action = MENU.get(choose)
            if action is None:
                print('Pilihan tidak valid, coba lagi.')
                continue

            try:
                action(ssh_client)
            except Exception as e:
                print(f"Error: {e}")

    except KeyboardInterrupt:
        print("\nProses dihentikan oleh pengguna.")

    finally:
        # Menutup koneksi hanya saat program selesai
        ssh_client.close()
        print('done')


if __name__ == "__main__":
    main()

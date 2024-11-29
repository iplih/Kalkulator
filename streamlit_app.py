import streamlit as st

st.title("KALKULATOR:rocket:")
# Nama File: kalkulator.py

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Tidak bisa dibagi dengan nol!"

def menu():
    print("\n==== KALKULATOR ====")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")

while True:
    menu()
    pilihan = input("Pilih operasi (1/2/3/4/5): ")

    if pilihan in ('1', '2', '3', '4'):
        num1 = float(input("Masukkan bilangan pertama: "))
        num2 = float(input("Masukkan bilangan kedua: "))

        if pilihan == '1':
            print(f"Hasil: {num1} + {num2} = {tambah(num1, num2)}")
        elif pilihan == '2':
            print(f"Hasil: {num1} - {num2} = {kurang(num1, num2)}")
        elif pilihan == '3':
            print(f"Hasil: {num1} * {num2} = {kali(num1, num2)}")
        elif pilihan == '4':
            print(f"Hasil: {num1} / {num2} = {bagi(num1, num2)}")
    elif pilihan == '5':
        print("Terima kasih telah menggunakan kalkulator ini!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")


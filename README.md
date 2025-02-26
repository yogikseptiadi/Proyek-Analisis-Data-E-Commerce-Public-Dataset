# Proyek Analisis Data: E-Commerce Public Dataset

Proyek ini melakukan analisis data pada dataset e-commerce publik, dengan fokus pada berbagai metrik yang dapat memberikan wawasan bisnis terkait penjualan, lokasi, dan kategori produk. Proyek ini melibatkan pembersihan data, eksplorasi data, dan visualisasi menggunakan berbagai tools dan teknik analisis.

Proyek ini bertujuan untuk:
- Melakukan analisis terhadap dataset e-commerce yang mencakup informasi terkait pesanan, pelanggan, produk, dan lokasi.
- Membuat dashboard visualisasi interaktif untuk memahami tren penjualan, lokasi pesanan, dan kategori produk terlaris.
- Menyediakan wawasan yang berguna untuk perbaikan bisnis e-commerce melalui analisis data yang komprehensif.

## Setup Environment - Shell/Terminal
1. Buat folder baru untuk proyek:
mkdir proyek_analisis_data
cd proyek_analisis_data

2. Instal pipenv dan buat environment:
pipenv install
pipenv shell

3. Instal library yang dibutuhkan:
pip install -r requirements.txt

## Run Streamlit App
streamlit run dashboard.py

## Struktur Folder
```plaintext
Proyek Analisa Data Final
├───dashboard/
│   ├───dashboard.py         # Script utama untuk menjalankan dashboard
│   ├───data_analytic.jpg    # Gambar yang digunakan untuk dashboard
│   ├───geolocation.csv      # Dataset utama yang digunakan untuk dashboard
│   └───main_data.csv        # Dataset utama yang digunakan untuk dashboard
├───data/
│   ├───customers_dataset.csv                   # Dataset utama yang digunakan untuk analisis
│   ├───geolocation_dataset.csv                 # Dataset utama yang digunakan untuk analisis
│   ├───order_items_dataset.csv                 # Dataset utama yang digunakan untuk analisis
│   ├───order_payments_dataset.csv              # Dataset utama yang digunakan untuk analisis
│   ├───orders_dataset.csv                      # Dataset utama yang digunakan untuk analisis
│   ├───order_reviews_dataset.csv               # Dataset utama yang digunakan untuk analisis
│   ├───product_category_name_translation.csv   # Dataset utama yang digunakan untuk analisis
│   ├───products_dataset.csv                    # Dataset utama yang digunakan untuk analisis
│   └───sellers_dataset.csv                     # Dataset utama yang digunakan untuk analisis
├───notebook.ipynb            # Jupyter notebook untuk eksplorasi data dan visualisasi
├───README.md                 # Dokumentasi proyek
└───requirements.txt          # Daftar library yang digunakan dalam proyek


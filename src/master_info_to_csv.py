import csv

# Verilen bilgiler
data = [
    {'local': 1, 'elapsed_time': 24.927491426467896, 'cpu_percent': 24.7, 'virtual_memory_percent': 40.6,
     'accuracy': 0.8362566215420836, 'ROC': 0.917823770809135, 'train_elapsed_time': 16.34953808784485,
     'train_cpu_percent': 28.2, 'train_virtual_memory_percent': 17.5},
    {'local': 2, 'elapsed_time': 13.15972900390625, 'cpu_percent': 33.8, 'virtual_memory_percent': 17.6,
     'accuracy': 0.8435446009389671, 'ROC': 0.9206083050567605, 'train_elapsed_time': 8.971112728118896,
     'train_cpu_percent': 61.0, 'train_virtual_memory_percent': 17.6},
    {'local': 4, 'elapsed_time': 12.976667642593384, 'cpu_percent': 56.0, 'virtual_memory_percent': 18.3,
     'accuracy': 0.8346512451315945, 'ROC': 0.9165465142291688, 'train_elapsed_time': 7.704815149307251,
     'train_cpu_percent': 33.0, 'train_virtual_memory_percent': 18.7},
    {'local': 6, 'elapsed_time': 10.762937307357788, 'cpu_percent': 29.9, 'virtual_memory_percent': 18.5,
     'accuracy': 0.8385225523854622, 'ROC': 0.9213380260517289, 'train_elapsed_time': 6.502172946929932,
     'train_cpu_percent': 43.7, 'train_virtual_memory_percent': 18.8},
    {'local': 8, 'elapsed_time': 12.308561325073242, 'cpu_percent': 49.7, 'virtual_memory_percent': 19.2,
     'accuracy': 0.8446177478435543, 'ROC': 0.9230054591630118, 'train_elapsed_time': 6.333779335021973,
     'train_cpu_percent': 34.0, 'train_virtual_memory_percent': 19.1}
]

# CSV dosyasının adı
csv_file_path = 'code\data\master_info.csv'

# CSV dosyasını yaz
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Sütun başlıklarını yaz
    writer.writeheader()

    # Verileri yaz
    for row in data:
        writer.writerow(row)

print(f"CSV dosyası oluşturuldu: {csv_file_path}")

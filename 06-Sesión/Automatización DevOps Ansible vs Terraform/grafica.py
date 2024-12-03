import matplotlib.pyplot as plt
import pandas as pd

# Ruta del archivo
file_path = "D:/Documents/complementario-3125033/06-Sesión/Automatización DevOps Ansible vs Terraform/ansinbleTerraform.xlsx"

# Leer el archivo completo
data = pd.read_excel(file_path, header=None)  # No asumimos encabezados, cargamos todo
print("Primeras filas del DataFrame:\n", data.head())  # Verifica cómo se cargaron los datos

# Localizar los encabezados reales
headers_row = data[data.iloc[:, 0] == "Semana"].index[0]  # Encuentra la fila donde empieza "Semana"
data.columns = data.iloc[headers_row]  # Usa esa fila como nombres de columna
data = data[headers_row + 1:].reset_index(drop=True)  # Filtra los datos por debajo de los encabezados
data.columns.name = None  # Limpia el nombre del índice de columnas

# Verificar los nombres finales de las columnas
print("Columnas detectadas:", data.columns)
print("Primeras filas procesadas del DataFrame:\n", data.head())

# Extraer columnas relevantes
semanas = data['Semana']
ansible = pd.to_numeric(data['Ansible'], errors='coerce')  # Aseguramos conversión numérica
terraform = pd.to_numeric(data['Terraform'], errors='coerce')

# Graficar los datos
plt.figure(figsize=(10, 6))
plt.plot(semanas, ansible, label='Ansible', color='red', marker='o')
plt.plot(semanas, terraform, label='Terraform', color='green', marker='o')

# Personalización del gráfico
plt.ylim(0, 100)
plt.xticks(rotation=45)
plt.xlabel('Semanas')
plt.ylabel('Índice de Popularidad')
plt.title('Comparativa de Popularidad: Ansible vs Terraform')
plt.legend()
plt.grid()

# Mostrar la gráfica
plt.tight_layout()
plt.show()
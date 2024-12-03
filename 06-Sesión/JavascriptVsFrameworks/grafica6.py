import matplotlib.pyplot as plt
import pandas as pd

# Ruta del archivo
file_path = "D:/Documents/complementario-3125033/06-Sesión/JavascriptVsFrameworks/javaScriptFrameworks.xlsx"

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
semanas = pd.to_datetime(data['Semana'], errors='coerce')  # Convertir la columna 'Semana' a datetime
javaScript = pd.to_numeric(data['JavaScript'], errors='coerce')  # Aseguramos conversión numérica
react = pd.to_numeric(data['React'], errors='coerce')
angular = pd.to_numeric(data['Angular'],errors='coerce')

# Graficar los datos
plt.figure(figsize=(10, 6))
plt.plot(semanas, javaScript, label='JavaScript', color='black', marker='o')
plt.plot(semanas, react, label='React', color='blue', marker='o')
plt.plot(semanas,angular, label='Angular', color='red', marker='o')

# Personalización del gráfico
plt.ylim(0, 100)
plt.xticks(semanas[::len(semanas)//10], [str(year) for year in semanas.dt.year[::len(semanas)//10]])  # Ajustar las etiquetas de años
plt.xlabel('Año')
plt.ylabel('Índice de Popularidad')
plt.title('Comparativa de Popularidad: JavaScript vs Frameworks')
plt.legend()
plt.grid()

# Mover la leyenda al lado izquierdo
plt.legend(loc='upper left')  # Aquí se especifica la ubicación de la leyenda

# Mostrar la gráfica
plt.tight_layout()
plt.show()

from sqlalchemy.orm import sessionmaker

from crear_base import Saludo2
from configuracion import engine
import csv
csv_file = '/home/alex/Escritorio/plataformas_web/clase06-1bim-AlexJavierQ/ejemplo1/data/saludos_mundo.csv'

Session = sessionmaker(bind=engine)
session = Session()

with open(csv_file, newline='', encoding='utf-8') as archivo_csv:
    lector = csv.DictReader(archivo_csv, delimiter='|')  # Usa '|' como separador
    for fila in lector:
        saludo = Saludo2(
            mensaje=fila['saludo'],  # Se adapta al encabezado real del CSV
            tipo=fila['tipo']
            tipo=fila['origen']
        )
        session.add(saludo)

# se confirma las transacciones
session.commit()

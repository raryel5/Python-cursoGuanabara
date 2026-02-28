import csv
import matplotlib.pyplot as plt

campo = []

with open('fm0209.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for linha in reader:
        campo.append(float(linha['Electric_Field_V_m']))

# print(len(campo))

variacao = []

for i in range(len(campo)):
    if i == 0:
        variacao.append(0)
    else:
        variacao.append(campo[i] - campo[i-1])

x = list(range(len(campo)))

# padrão de estilo
plt.style.use('ggplot')

# plt.ion()

plt.title('variações de campo e pulsos')
plt.ylabel('V/m')
plt.xlabel('tempo')
plt.scatter(x, variacao)
plt.legend()
plt.show()

# plt.pause(5)

# plt.ioff()


# Data ISO 8601 (com fuso UTC 'Z')
# iso_date = "2023-10-27T10:00:00Z"

# Converte para objeto datetime
# dt = datetime.fromisoformat(iso_date.replace('Z''+00:00'))

# Converte para timestamp (segundos)
# timestamp = dt.timestamp()

# from datetime import datetime
# dt = datetime.strptime("2026-02-26T00:00:00""%Y-%m-%dT%H:%M:%S")
# timestamp = int(dt.timestamp())
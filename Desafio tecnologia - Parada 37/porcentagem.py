import pandas as pd
import matplotlib.pyplot as plt

planilha = pd.read_excel("A Fazenda.xlsx")

participantes = planilha['Participantes:']
votos = planilha['Votos para ganhar:']

plt.title("Enquete parcial:")

plt.barh(participantes, votos, color='blue', height=0.5)

plt.show()
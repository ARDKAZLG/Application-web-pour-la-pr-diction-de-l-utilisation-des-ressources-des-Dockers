import matplotlib
matplotlib.use('Agg')  # Utilisation de Matplotlib en mode "non interactif"

import matplotlib.pyplot as plt
import pandas as pd

csv_file = '/home/aouzal/DockerApplication/memory_usage.csv'
data = pd.read_csv(csv_file)
timestamp = data['Timestamp']

# Générer le graphique pour l'utilisation du CPU
cpu_percentages = data['CPUsage'].astype(str)
cpu_values = cpu_percentages.str.extract(r'([\d.]+)').astype(float)
fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(timestamp, cpu_percentages)
ax.set_title('CPU Usage of Docker Containers')
ax.set_xlabel('Timestamp')
ax.set_ylabel('CPU Usage (%)')
ax.set_xticks(range(len(timestamp)))
ax.set_xticklabels(timestamp, rotation=60)
ax.set_yticks(range(0, 201, 20))
ax.set_yticklabels(['{}%'.format(i) for i in range(0, 201, 20)])
ax.grid(True)
fig.set_size_inches(fig.get_size_inches()[0], fig.get_size_inches()[1]*1.25)
cpu_image_path = 'static/dist/img/cpu_chart.png'
plt.savefig(cpu_image_path, format='png')
plt.close(fig)

# Générer le graphique pour l'utilisation de la mémoire
mem_percentages = data['Ram_usage']
mem_values = mem_percentages.str.extract(r'([\d.]+)').astype(float)
fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(timestamp, mem_values)
ax.set_title('Memory Usage of Docker Containers')
ax.set_xlabel('Timestamp')
ax.set_ylabel('Memory Usage (MB)')
ax.set_xticks(range(len(timestamp)))
ax.set_xticklabels(timestamp, rotation=60)
ax.set_yticks(range(0, 101, 10))
ax.set_yticklabels(['{}MB'.format(i) for i in range(0, 101, 10)])
ax.grid(True)
fig.set_size_inches(fig.get_size_inches()[0], fig.get_size_inches()[1]*1.25)
mem_image_path = 'static/dist/img/mem_chart.png'
plt.savefig(mem_image_path, format='png')
plt.close(fig)

# Vous pouvez maintenant utiliser les images générées (cpu_image_path et mem_image_path) selon vos besoins.


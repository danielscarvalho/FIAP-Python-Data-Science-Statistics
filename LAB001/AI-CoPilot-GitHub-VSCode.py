# Usando GitHub con Visual Studio Code para colaborar en proyectos de Python com CoPilot

# Usando Python y Seaborn para trazar un gráfico de dispersión y un histograma de una lista de 1000 números aleatorios

# Pairing com AI (CoPilot) para responder a preguntas de Python

# Dicas em: https://code.visualstudio.com/docs/copilot/setup-simplified

# q: Plot a list of 1000 random numbers in a scatter plot and histogram using Python and Seaborn
# a:    
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate 1000 random numbers
data = np.random.randn(1000)

# Create a scatter plot
plt.scatter(np.arange(1000), data)
plt.show()

# Create a histogram
sns.histplot(data, kde=True)
plt.show()

# Plot with Seaborn a linear regression for this data, line in red dots in blue

sns.regplot(x=np.arange(1000), y=data, color='blue', scatter_kws={'color': 'red'})
# sns.regplot(x=np.arange(1000), y=data, color='red')
plt.show()



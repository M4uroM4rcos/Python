# Importa biblioteca
from tqdm import tqdm
import time

# Exibe a barra de progresso
for i in tqdm(range(100)):
    time.sleep(0.05)
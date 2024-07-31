from datetime import datetime
hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open('/workspaces/exercise-terminal-challenge/ej_ter/res/test.txt', "a") as archivo:
	archivo.write(f'Tarea finalizada a las {hora}')

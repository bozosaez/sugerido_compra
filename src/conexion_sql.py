import pyodbc

def conexion(SERVER, DATABASE, PWD):
    try:
        # Asegúrate de usar las variables SERVER, DATABASE y PWD en la cadena de conexión
        cnxn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID=BARRACA;PWD={PWD}')
        return cnxn
    except Exception as e:
        # Devuelve el mensaje de error en lugar del objeto de conexión
        return f"Se ha producido un error: {e}"
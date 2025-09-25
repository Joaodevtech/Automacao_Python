from notion_client import Client
import os

# Carregar token e database ID
NOTION_TOKEN = os.getenv("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")  # ou substitua pelo seu token diretamente
DATABASE_ID = os.getenv("2789f300cc05805184f6000ca18c8107")  # ou substitua pelo seu ID diretamente

notion = Client(auth=NOTION_TOKEN)

# Função para listar propriedades
def listar_propriedades(database_id):
    try:
        database = notion.databases.retrieve(database_id=database_id)
        properties = database.get("properties", {})
        
        print(f"Propriedades do banco de dados ({database_id}):\n")
        for nome, info in properties.items():
            print(f"- {nome}: {info['type']}")
            
    except Exception as e:
        print(f"Erro ao acessar o banco de dados: {e}")

# Executa a função
listar_propriedades(DATABASE_ID)

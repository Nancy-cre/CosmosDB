import azure.functions as func
import azure.cosmos as cosmos
from azure.identity import DefaultAzureCredential

app = func.FunctionApp()

app.route('ShowUser', auth_level = func.AuthLevel.FUNCTION)
def showUser(req : func.HttpRequest) -> func.HttpResponse:
    defCred = DefaultAzureCredential()

    cosmos_url = 'https://cosmos20260202.documents.azure.com:443/'
    cosmosClient = cosmos.CosmosClient(cosmos_url, defCred, '3')

    dbClient = cosmosClient.get_database_client('cosmosDb')

    dbClient.get_container_client('UserM')
    
    userList = dbClient.query_containers("SELECT * FROM c CountryID = 'Japan'")

    html = '<h1>日本のユーザー一覧</h1>'

    for user in userList:
        html += user + '</br>'
        
    return func.HttpResponse(html, mimetype = 'text/html', status_code = 200)
import azure.functions as func
import azure.cosmos as cosmos
from azure.identity import DefaultAzureCredential
import logging

app = func.FunctionApp()

app.route('ShowUser', auth_level = func.AuthLevel.FUNCTION)
def showUser(req : func.HttpRequest) -> func.HttpResponse:
    #defCred = DefaultAzureCredential()

    #cosmos_url = 'https://cosmos20260202.documents.azure.com:443/'
    #cosmosClient = cosmos.CosmosClient(cosmos_url, defCred, '3')

    #dbClient = cosmosClient.get_database_client('cosmosDb')

    #dbClient.get_container_client('UserM')
    
    #userList = dbClient.query_containers("SELECT * FROM c CountryID = 'Japan'")

    #html = '<h1>日本のユーザー一覧</h1>'

    #for user in userList:
        #html += user + '</br>'
        
    return func.HttpResponse('<h1>日本のユーザー一覧</h1>', mimetype = 'text/html', status_code = 200)

@app.route(route="http_trigger", auth_level=func.AuthLevel.FUNCTION)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )


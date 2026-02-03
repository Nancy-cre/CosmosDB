import azure.functions as func
import azure.cosmos as cosmos
from azure.identity import DefaultAzureCredential
import logging

app = func.FunctionApp()

@app.route(route="show_user", auth_level = func.AuthLevel.FUNCTION)
def show_user(req : func.HttpRequest) -> func.HttpResponse:
    defCred = DefaultAzureCredential()

    cosmos_url = 'https://cosmos20260202.documents.azure.com:443/'
    cosmosClient = cosmos.CosmosClient(cosmos_url, defCred, '3')

    dbClient = cosmosClient.get_database_client('cosmosDb')

    container = dbClient.get_container_client('UserM')
    
    userList = container.query_items("SELECT * FROM c", enable_cross_partition_query=True)

    html = '<h1>日本のユーザー一覧</h1>'

    for user in userList:
        if user['CountryID'] == 'Japan':
            html += user['id'] + '----------'
            html += user['CountryID'] + '----------'
            html += user['UserID'] + '----------'
            html += user['_rid'] + '----------'
            html += user['_self'] + '----------'
            html += user['_etag'] + '----------'
            html += user['_attachments'] + '</br>'
            #html += user['_ts'] + ':'
     
    return func.HttpResponse(html, mimetype='text/html', status_code = 200)

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


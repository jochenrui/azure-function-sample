import azure.functions as func

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return {"message": "success"}
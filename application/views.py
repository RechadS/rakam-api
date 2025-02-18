from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.response import Response
# from application.engine.RAGGenApi import askQuestion
from .models import Client
from .serializers import ClientSerializer
from application.engine.agent_QueryClassification.agent_config import AGENT_QUERY_CLASSIFICATION



@api_view(["GET"])
def test_response(request):
    """
    Endpoint that takes a user message as input and returns a response in JSON format.
    """
    base_response = {
        "text": "Hey, test test was successful !",
    }

    return Response(base_response, status=200)

@api_view(["POST"])
def queryClassification(request):
    """
    Endpoint that takes a user message as input and returns a response in JSON format.
    """
    question = request.query_params.get('question', '')
    
    results = AGENT_QUERY_CLASSIFICATION.choose_action(question)

    # Placeholder response structure
    base_response = {
        "text": results,
    }

    return Response(base_response, status=200)

@api_view(["GET"])
def getClients(request):
    """
    Endpoint that takes a user message as input and returns a response in JSON format.
    """
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)

    # Placeholder response structure
    #base_response = {
        # "text": results,
    #    "text": serializer_class,
    #}

    return Response(serializer.data, status=200)

@api_view(["POST"])
def createClient(request):
    serializer = ClientSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data, status=201)

@api_view(["POST"])
def updateClient(request, pk):
    client = Client.objects.get(id=pk)
    serializer = ClientSerializer(instance=client, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data, status=200)

@api_view(["DELETE"])
def deleteClient(request, pk):
    client = Client.objects.get(id=pk)
    client.delete()

    return Response("Client deleted successfully", status=204)



# @api_view(["POST"])
# def dummy_endpoint(request):
#     """
#     Endpoint that takes a user message as input and returns a response in JSON format.
#     """
#     # Placeholder response structure
#     base_response = {
#         "text": "Hey, test test was successful !",
#     }

#     return Response(base_response, status=200)

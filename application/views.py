from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.response import Response
from application.engine.RAGGenApi import askQuestion



@api_view(["GET"])
def test_response(request):
    """
    Endpoint that takes a user message as input and returns a response in JSON format.
    """
    question = request.query_params.get('question', '')
    results = askQuestion(question)
    # Placeholder response structure
    base_response = {
        "text": results,
        # "text": "Hey, test test was successful !",
    }

    return Response(base_response, status=200)


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

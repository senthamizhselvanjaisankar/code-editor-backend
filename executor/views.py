from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

@api_view(["POST"])
def execute_code(request):
    code = request.data.get("code", "")
    stdin = request.data.get("input", "")

    payload = {
        "language": "python",
        "version": "3.10.0",
        "files": [{"name": "main.py", "content": code}],
        "stdin": stdin,
    }

    response = requests.post("https://emkc.org/api/v2/piston/execute", json=payload)
    result = response.json()

    return Response({"output": result.get("run", {}).get("output", "Execution error.")})

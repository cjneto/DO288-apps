from sanic import Sanic
from sanic.response import json

app = Sanic("App Name")

@app.route("/")
async def test(request):
    return json({"hello": "world", "Message from OpenShift":app.config.MSG})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

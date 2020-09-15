from sanic import Sanic
from sanic.response import json

app = Sanic("App Name")
app.config.from_envvar("SETTINGS")

@app.route("/")
async def test(request):
    return json({"hello": "world", "Message from OpenShift":app.config.MSG, "Settings":app.config.DB})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

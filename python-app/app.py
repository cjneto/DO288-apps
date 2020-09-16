from sanic import Sanic
from sanic.response import json
import json,os

with open(os.environ['SANIC_ENV']) as jf:
    cred = json.load(jf)

print(cred)

app = Sanic("App Name")
app.config.update(cred)

@app.route("/")
async def test(request):
    print(app.config)
    return json({"hello": "world", "Message from OpenShift":app.config.MSG}) #, "Settings":app.config})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

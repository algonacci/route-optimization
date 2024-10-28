from flask import Flask
from flask_pydantic import validate
from optimizer import optimize_route
from schema import CoordinateList
from web import Info, WebResponse

app = Flask(__name__)


@app.get("/")
def root():
    image_link = (
        "https://i.pinimg.com/originals/a4/66/92/a466929a0a4f261c67a038c7e0fbd82d.jpg"
    )
    return f'<div style="text-align:center"><img src="{image_link}" alt="Image" style="width: 50%;"></div>'


@app.post("/optimize")
@validate(body=CoordinateList)
def optimize(body: CoordinateList):
    solution = optimize_route(coordinates=body.data).tolist()
    return WebResponse(info=Info(message="Success optimize route"), data=solution)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=6836
    )
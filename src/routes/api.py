from flask import Blueprint
from controllers import shortnener_controller

api = Blueprint("api", __name__)

@api.get("/<code>")
def redirectToOriginalUrl(code):
    return shortnener_controller.redirectToOriginalUrl(code)

@api.post('/shorten')
def shortenUrl():
    return shortnener_controller.createShortUrl()

import random
import string
from models.shortener import Shortnener
from flask import jsonify, request
from extensions.db import db
from schemas.shortener_schema import ShortenerSchema
from marshmallow import ValidationError

def redirectToOriginalUrl(code):
    data = Shortnener.query.filter_by(code = code).first()

    if not data:
        return jsonify({"message": "URL not found"}), 404

    data.amount_clicked = data.amount_clicked + 1

    db.session.commit()

    return jsonify(data.to_dict()), 200

def createShortUrl():
    schema = ShortenerSchema()

    try:
        data = schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(5))

    shortnener = Shortnener(
        code=random_string,
        url=data['url']
    )

    db.session.add(shortnener)
    db.session.commit()

    return jsonify({
        "short_url": request.host + "/" + shortnener.code
    }), 201
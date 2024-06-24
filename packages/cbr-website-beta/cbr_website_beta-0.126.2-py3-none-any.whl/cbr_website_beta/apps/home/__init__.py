from flask import Blueprint

EXPECTED_ROUTES__ROOT = ['/athena','/home', '/home.html','/version', '/chat-with-llms']

blueprint = Blueprint(
    'home_blueprint',
    __name__,
    url_prefix='/web'
)

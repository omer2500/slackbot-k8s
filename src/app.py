from dotenv import load_dotenv
from flask import Flask
from utils.init_routes import init_routes
from middleware.slackAuth import slackAuth
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
# Load env variables to python
load_dotenv()

# Init flask App
app = Flask(__name__)

# Set rate limit
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["3600 per minute", "60 per second"],
)

# Like helmetjs
Talisman(app)

# Auth middleware 
app.wsgi_app = slackAuth(app.wsgi_app)

# init the api routes
init_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
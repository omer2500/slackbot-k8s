from route.pods import pods_blueprint
def init_routes(app):
    app.register_blueprint(pods_blueprint, url_prefix="/")
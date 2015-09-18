
def create_event_routes(app):

    @app.route("/")
    def hello():
        return "Hello World!"

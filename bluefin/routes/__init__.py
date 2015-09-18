from bluefin.routes.event import create_event_routes


def configure_routes(app):
    create_event_routes(app)

"""
Configuration of the app
"""

from bluefin.routes import configure_routes


def configure_app(app, debug=False, testing=False):
    """
    Configure the application.
    """
    app.debug = debug
    app.testing = testing

    # app.config.from_object(defaults)
    # app.config.from_envvar(envvar, silent=True)

    configure_routes(app)

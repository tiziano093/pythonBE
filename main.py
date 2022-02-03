from flask import Flask
from flask import send_file, send_from_directory, safe_join, abort

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        safe_path = safe_join('output.file')
        return send_file(safe_path, as_attachment=True)

    return app
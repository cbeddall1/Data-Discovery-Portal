from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Respect the app config DEBUG value or environment variable
    debug_val = os.environ.get('FLASK_DEBUG', None)
    if debug_val is None:
        debug = app.config.get('DEBUG', False)
    else:
        debug = debug_val.lower() == 'true'

    app.run(host='0.0.0.0', port=port, debug=debug)

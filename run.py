from flaskblog import create_app
from flaskblog import db 
app = create_app()

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=1180)

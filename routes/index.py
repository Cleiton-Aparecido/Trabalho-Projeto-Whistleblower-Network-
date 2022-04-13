from flask.templating import render_template

class AppRoutes:
    def __init__(self, app):
        print(app)

    # @app.route('/')
    # def index():
    #     return render_template('register.html')

    # @app.route('/login')
    # def login():
    #     return render_template('login.html')
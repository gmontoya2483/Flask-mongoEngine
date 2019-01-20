from flask import Flask
from models.models import Users


app = Flask(__name__)
#app.config['MONGODB_SETTINGS'] = {
#    'db': 'gabrielhernan_test',
#    'host': 'mongodb://gabriel:GHM2483@ds159782.mlab.com:59782/gabrielhernan_test'
#}

app.config['MONGODB_DB'] = 'gabrielhernan_test'
app.config['MONGODB_HOST'] = 'ds159782.mlab.com'
app.config['MONGODB_PORT'] = 59782
app.config['MONGODB_USERNAME'] = 'gabriel'
app.config['MONGODB_PASSWORD'] = 'GHM2483'




@app.route('/')
@app.route('/index')
def index():
    #users = Users.objects( name='gabriel', password='ghf1234')
    #users = Users.objects().limit(3).order_by('-name')

    users = Users.objects().limit(3).order_by('-id')

    for user in users:
        print(f'_id: { user.id }, name: { user.name }, password: { user.password }')
    return f'All users!!!'


@app.route('/create/<string:name>/<string:password>')
def create(name, password):
    user = Users(name=name, password=password)
    user.save()
    return f'name = { user.name }, password= { user.password } '


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

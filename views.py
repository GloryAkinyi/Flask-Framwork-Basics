from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index') #127.0.0.1:5000
def index():
    return "<h1>Hello Puppy!</h1>"




@app.route('/information') #127.0.0.1:5000/information
def information():
    return "<h1>Puppies are cute!</h1>"


# Dynamic Routing
@app.route('/puppy/<name>') #127.0.0.1:5000/information
def puppy(name):
    return "<h1>This is a page for {}</h1>".format(name)   



#Rendering Templates

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/admin')
def admin():
    full_name = "Glory"
    return render_template('admin.html', full_name = full_name)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/child')
def child():
    return render_template('child.html')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'No Ninjas Here'

@app.route('/ninjas')
def ninjas():
    return render_template('index.html', ninja_turtles=True)

@app.route('/ninjas/<ninja_color>')
def color(ninja_color):
    return render_template('index.html', ninja_turtles=False, color=ninja_color)


if __name__ == '__main__':
    app.run()

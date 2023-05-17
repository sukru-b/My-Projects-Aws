from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def head():
    return render_template('index.html', number1=1985, number2=1988)


@app.route('/calc')

def number():
    x=5
    y=25
    return render_template('body.html', num1=x, num2=y, mult=x*y, sum=x+y)

if __name__ == '__main__':
    #  app.run(debug=True)
    app.run(host= '0.0.0.0', port=80)
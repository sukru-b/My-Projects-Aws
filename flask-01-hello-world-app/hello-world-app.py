from flask import Flask

app = Flask(__name__)   

@app.route('/')
def head():
    return "Hello World Sukru" 

@app.route('/second')
def second():
    return "This is second page"

@app.route('/third')
def third():
    return "This is third page"

@app.route('/third/<string:id>')
def third_sub(id):
    return f"ID of this page is {id}"

if __name__ == '__main__':
    #  app.run(debug=True)
    app.run(host= '0.0.0.0', port=80)
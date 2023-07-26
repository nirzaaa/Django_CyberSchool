# https://stackoverflow.com/questions/66627441/error-could-not-locate-a-flask-application

from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    search = request.args.get('search') or None

    template = '''
                <p>hello world</p>
                {}
    '''.format(search)

    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, redirect

app = Flask(__name__)
url_map = {}

@app.route('/')
def home():
    return '''
    <form action="/shorten" method="post">
        <input type="text" name="url">
        <button type="submit">Shorten</button>
    </form>
    '''

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form.get('url')
    short_id = str(hash(original_url))[:6]
    url_map[short_id] = original_url
    return f'Shortened URL: <a href="/{short_id}">{short_id}</a>'

@app.route('/<short_id>')
def redirect_to_url(short_id):
    original_url = url_map.get(short_id)
    return redirect(original_url)

if __name__ == '__main__':
    app.run(debug=True)

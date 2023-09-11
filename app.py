import time

from flask import Flask, jsonify, request, Response
from posts.apnews_scraper import external_links

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_world():  # put application's code here
    url = request.args.get('url')
    print(url)
    if not url:
        return jsonify("Please send a url for the category of the web after /")
    data = external_links(url)
    return jsonify({"article_urls": data})

def generate_data():
    for i in range(1, 6):
        time.sleep(3)
        # Simulate some data to send (replace this with your actual data)
        data_chunk = f"Data Chunk {i}\n"

        # Yield the data chunk to the response
        yield data_chunk

@app.route('/api', methods=['GET'])
def stream_data():
    # Create a streaming response using the generator function
    return Response(generate_data(), content_type='text/plain')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

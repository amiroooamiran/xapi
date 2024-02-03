from flask import Flask, request

app = Flask(__name__)

@app.route('/receive-data', methods=['POST'])
def receive_data():
    data = request.get_json()
    search_query = data.get('search_query')
    filters = data.get('filters')

    print(search_query, filters)
    # Now you have received the data from Postman, you can use it in your Selenium script
    return "Data received successfully!"

@app.route('/receive-data', methods=['GET'])
def get_data():
    return "I'm ready to receive data!"

if __name__ == '__main__':
    app.run(debug=True)

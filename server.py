from flask import Flask, request, redirect, render_template

app = Flask(__name__)

count = 0

@app.route('/')
def route_index():
    return render_template('index.html', count=count)


@app.route('/request_counter', methods=['GET', 'POST', 'DELETE', 'PUT'])
def increment_counts():
    global count
    if request.method == 'GET' or request.method == 'POST' or request.method == 'DELETE' or request.method == 'PUT':
        count += 1
        return redirect('/')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )

from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_file():
    return redirect('file:///etc/passwd')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

link = 0

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        link = request.form['code']
        if link == 'cd resume':
            return render_template('cv.html')
        if link == 'ls':
            return render_template('tree.html')
        if link == 'cd projects':
            return render_template('notfound.html')
        if link == 'cd ..' or link == 'cd home' or link=='cd /':
            return render_template('index.html')
        else:
            return render_template('error.html')
    return render_template('index.html')








if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def student():
    return render_template('student_info.html')


@app.route('/detail', methods=['POST'])
def detail():
    if request.method == 'POST':
        res = dict()
        res['Name'] = request.form.get('Name')
        res['StudentNumber'] = request.form.get('StudentNumber')
        res['Gender'] = request.form.get('Gender')
        res['Major'] = request.form.get('Major')
        res['languages'] = ', '.join(request.form.getlist('languages'))
        return render_template("detail.html", result=res)


@app.route('/result', methods=['POST'])
    if request.method == 'POST':
        res = request.form.to_dict()
        return render_template("result.html", result=res)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=80)

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cr7'
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/calculos')
def calculos():
    return render_template("calculos.html")

@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")
@app.route('/geometria')
def geometria():
    return render_template("geometria.html")
@app.route('/funcionario')
def funcionario():
    return render_template("funcionario.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            flash("soma realizada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
        else:
            #passo 1 : emitir a mensagem e a categoria do flash
            flash("preencher os campos", "alert-danger")
    return render_template("operacoes.html")


@app.route('/subtraçao', methods=['GET', 'POST'])
def subtracao():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            sub = n1 - n2
            return render_template("operacoes.html", n1=n1, n2=n2, sub=sub)
        else:
            # passo 1 : emitir a mensagem e a categoria do flash
            flash("preencher os campos", "alert-danger")

    return render_template("operacoes.html")
@app.route('/Multiplicacao', methods=['GET', 'POST'])
def Multiplicacao():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            mult = n1 * n2
            return render_template("operacoes.html", n1=n1, n2=n2, mult=mult)
        else:
            # passo 1 : emitir a mensagem e a categoria do flash
            flash("preencher os campos", "alert-danger")

    return render_template("operacoes.html")

@app.route('/divisao', methods=['GET', 'POST'])
def divisao():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            div = n1 / n2
            return render_template("operacoes.html", n1=n1, n2=n2, div=div)
        else:
            # passo 1 : emitir a mensagem e a categoria do flash
            flash("preencher os campos", "alert-danger")

    return render_template("operacoes.html")

@app.route('/triangulo', methods=['GET', 'POST'])
def triangulo():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            pe = (n1**2, 3**0.5)
            return render_template("geometria.html", n1=n1, pe=pe)

        return render_template("geometria.html")

@app.route('/hexagono', methods=['GET', 'POST'])
def hexagono():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            pe = (n1**2, 3**0.5)
            return render_template("geometria.html", n1=n1, pe=pe)
        return render_template("geometria.html")

@app.route('/circulo', methods=['GET', 'POST'])
def circulo():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            pe = (n1**2, 3**0.5)
            return render_template("geometria.html", n1=n1, pe=pe)
        return render_template("geometria.html")

@app.route('/retangulo', methods=['GET', 'POST'])
def retangulo():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            pe = (n1**2, 3**0.5)
            return render_template("geometria.html", n1=n1, pe=pe)
        return render_template("geometria.html")


#TODO Final do código

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/formulario')
def exibir_formulario():
    return render_template('formulario.html', resultado='Aguardando os dados...')

@app.route('/processo-calcular',methods=['POST'])
def processo_calcular():


    numero1 = float (request.form.get('numero1'))
    numero2 = float (request.form.get('numero2'))
    operacao = request.form.get('operacao')

    if not numero1 or not numero2:
        mensagem_resultado = f"ERRO: Todos os campos são obrigatórios!"

    elif operacao == "soma":
        calculo = numero1 + numero2
        mensagem_resultado = f"{calculo}"
    elif operacao == "subtracao":
        calculo = numero1 - numero2
        mensagem_resultado = f"{calculo}"
    elif operacao == "multiplicacao":
        calculo = numero1 * numero2
        mensagem_resultado = f"{calculo}"
    elif operacao == "divisao":
        calculo = numero1 / numero2
        mensagem_resultado = f"{calculo}"
    else:
        mensagem_resultado = f"ERRO: Todos os campos são obrigatórios!"

    return render_template('formulario.html', resultado=mensagem_resultado)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
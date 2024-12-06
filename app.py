from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Configurações do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'pesquisasatisfacao75@gmail.com'
app.config['MAIL_PASSWORD'] = 'PS123456%'  # Senha de Aplicativo gerada no Google
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    rating = data.get('rating')
    comments = data.get('comments')

    # Enviar o e-mail
    msg = Message('Novo Feedback - Pesquisa de Satisfação',
                  sender='pesquisasatisfacao75@gmail.com',
                  recipients=['pesquisasatisfacao75@gmail.com'])  # E-mail destinatário
    msg.body = f"""
    Nome: {name}
    Email: {email}
    Avaliação: {rating}
    Comentários: {comments}
    """
    mail.send(msg)

    return jsonify({"message": "Feedback enviado com sucesso!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
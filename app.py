from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'secret'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'juanromer673@gmail.com'
app.config['MAIL_PASSWORD'] = 'kclf uale fqsz sgim'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        telefono = request.form['telefono']
        message = request.form['message']

        body_html = f"""
        <html>
          <body>
            <h2 style="color: #007bff;">Nuevo mensaje recibido:</h2>
            <p><strong>Nombre:</strong> {name}</p>
            <p><strong>Correo:</strong> <a href="mailto:{email}">{email}</a></p>
            <p><strong>Teléfono:</strong> {telefono}</p>
            <p><strong>Mensaje:</strong></p>
            <p>{message}</p>
          </body>
        </html>
        """

        msg = Message(
            'Nuevo mensaje desde el formulario de contacto',
            sender=email,
            recipients=['juanromer673@gmail.com'],
            html=body_html
        )

        try:
            mail.send(msg)
            return jsonify({'status': 'success', 'message': 'Mensaje enviado correctamente'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        telefono = request.form.get('telefono')
        message = request.form.get('message')

        msg = Message(
            'Hola Diego, tienes un nuevo mensaje!',
            body=f'Nombre: {name} \nCorreo: <{email}> \nTelefono: {telefono} \n\nEscribio: {message}',
            sender=email,
            recipients=['juanromer673@gmail.com']
        )

        try:
            mail.send(msg)
            return jsonify({'status': 'success', 'message': 'Correo enviado con éxito'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': f'Error al enviar el correo: {str(e)}'})
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

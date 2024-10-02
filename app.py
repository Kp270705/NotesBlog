from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/selectPdf')
def selectPdf():
    return render_template('selectPdf.html')

@app.route('/selectText')
def selectText():
    return render_template('selectText.html')


# ai routes: 
@app.route('/aiText')
def aiText():
    return render_template('ai/ai_selection.html')

@app.route('/aiIntro')
def ai_intro():
    return render_template('ai/ai_introduction.html')

@app.route('/aiAlgo')
def ai_algo():
    return render_template('ai/ai_algo.html')

@app.route('/aiNlp')
def ai_nlp():
    return render_template('ai/ai_nlp.html')

@app.route('/aiRnn_Cnn')
def ai_rnn_cnn():
    return render_template('ai/ai_rnn_cnn.html')


# dbms routes:

@app.route('/dbmsText')
def dbmsText():
    return render_template('dbms/dbms_selection.html')

@app.route('/dbmsIntro')
def dbms_intro():
    return render_template('dbms/dbms_introduction.html')

@app.route('/dbmsIntro2')
def dbms_types():
    return render_template('dbms/dbms_types.html')
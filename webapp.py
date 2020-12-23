from flask import Flask, render_template
app=Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')
    
@app.route('/Aboutpage.html')
def About():
    return render_template('Aboutpage.html')

@app.route('/SellPatent.html')
def Sell():
    return render_template('SellPatent.html')

@app.route('/signin.html')
def sign():
    return render_template('signin.html')

@app.route('/Feedback.html')
def Feddback():
    return render_template('Feedback.html')
    
if __name__ == '__main__':
    app.run(debug=True)

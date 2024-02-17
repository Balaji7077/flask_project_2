from flask import Flask,render_template

FAI= Flask(__name__)

@FAI.route('/send_html')
def send_html():
    return render_template('send_html.html',name='Balaji')

@FAI.route('/function')
def function():
    return render_template('function.html',name='sabat')

if __name__=='__main__' :
    FAI.run(debug=True)
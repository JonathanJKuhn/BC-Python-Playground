from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    pass

@app.route('/play')
@app.route('/play/<int:numOfBoxes>')
@app.route('/play/<int:numOfBoxes>/<string:boxColor>')
def play(numOfBoxes = 3, boxColor = 'blue'):
    playNum = 1
    if boxColor != 'blue':
        playNum = 3
    elif numOfBoxes != 3:
        playNum = 2
    return render_template('playground.html',playNum=playNum,numOfBoxes=numOfBoxes,boxColor=boxColor)

if __name__ =="__main__":
    app.run(debug=True)
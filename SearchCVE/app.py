
from flask import *
#追加------------

from search_cve import main
#------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

#変更&追加-----------------------
@app.route("/calc", methods=['GET','POST'])
def calc():
	if request.method == 'GET':
		return render_template('calc.html')
	elif request.method == 'POST':
		diameter = request.form['diameter']
		result = calculation_circle(diameter)
		if len(result) == 2:
			return render_template('calc.html', area=result[0],circumference=result[1])
		else:
			return render_template('calc.html',error=result)
#-------------------------------------

# search_cve用ルーティング追加
@app.route("/search_cve", methods=['GET', 'POST'])
def search_cve():
	if request.method == "GET":
		return render_template('index.html')
	elif request.method == 'POST':
		cve = request.form['cve']
		result = main(cve)
		#return render_template('index.html', cve=cve)
		return render_template('index.html', cve=result)

if __name__ == '__main__':
    app.run()
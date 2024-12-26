
from flask import *
#追加------------

from search_cve import main
#------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

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
    app.run(port=8000)
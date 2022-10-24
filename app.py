from flask import Flask, request, render_template
import sqlite3
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html')
    else:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        form_user = request.form['input_user']
        form_date = request.form['input_dates']
        form_reason = request.form['input_reason']
        form_evidence = request.form['input_evidence']

        username = form_user
        reason = form_reason
        dates = form_date
        evi = form_evidence

        c.execute("""CREATE TABLE IF NOT EXISTS bans(username text, reason text, dates text, evidence text)""")

        c.execute("INSERT INTO bans (username, reason, dates, evidence) VALUES (?, ?, ?, ?)", (username, reason, dates, evi))

        conn.commit()
        conn.close()

        return render_template('index.html',form_user=form_user)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', Port=5000)
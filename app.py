### Integrate HTML With Flask
### HTTP verb GET And POST

##Jinja2 template engine
'''
{%...%} conditions,for loops
{{    }} expressions to print output
{#....#} this is for comments
'''
from flask import Flask,redirect,url_for,render_template,request

from dash_application import create_dash_application

app = Flask(__name__)

dash_app = create_dash_application(app)

@app.route('/')
def welcome():
    return render_template('index3.html')

# @app.route('/success/<int:score>')
# def success(score):
#     res=""
#     if score>=50:
#         res="PASS"
#     else:
#         res='FAIL'
#     exp={'score':score,'res':res}
#     return render_template('result.html',result=exp)



### Result checker submit html page
# @app.route('/submit',methods=['POST','GET'])
# def submit():
#     total_score=0
#     if request.method=='POST':
#         science=float(request.form['science'])
#         maths=float(request.form['maths'])
#         c=float(request.form['c'])
#         data_science=float(request.form['datascience'])
#         total_score=(science+maths+c+data_science)/4
#     res=""
#     return redirect(url_for('success',score=total_score))


@app.route('/submit2',methods=['POST','GET'])
def submit2():
    if request.method=='POST':
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        download = request.form['download']
        upload = request.form['upload']
        latency = request.form['latency']
        jitter = request.form['jitter']
        isp = request.form['isp']
    results = [latitude, longitude,download,upload,latency,jitter,isp]
   # print results
    print(results)
    return redirect(url_for('/dashboard/'))


@app.route('/dashboard/')
def dashboard():
    return dash_app.index()




if __name__=='__main__':
    app.run(debug=True)
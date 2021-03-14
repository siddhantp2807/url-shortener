from flask import Flask, redirect, render_template, request

from script import URLShortener, find, verifyGenerateAdd

app = Flask(__name__)


@app.route('/s.url', methods = ['GET', 'POST'])
def homePage() :
    if request.method == 'POST' :
        url = request.form['url']
        if URLShortener(url).urlValidator() :
            finalDict = verifyGenerateAdd(url)
            if finalDict :
                return render_template('result.html', data = finalDict)
            
        
        else :
                return render_template('err.html')
        
    else :
        return render_template('index.html')



@app.route('/s.<var>')
def redirection(var) :
    return redirect(find(var)['url'])

@app.errorhandler(404)
def err(e) :
    return f'{e}'
 
if __name__ == '__main__' :
    app.run(debug=True)



from flask import Flask,render_template,request
import gensim.models.word2vec as w2v
import os
app = Flask(__name__)


def hello():
    return 'hello world from flask'

@app.route('/')
def welcomeForm():
    return render_template('form.html',the_title = 'Welcome to generate simillar words on the web')


@app.route('/similarWords',methods=['POST'])
def returnSimilar(word='')->'html':
    vectorization = w2v.Word2Vec.load(os.path.join("E:/IDC_Policies/trained","vectorization.w2v"))
    word = request.form['word']
    try:
        result = vectorization.wv.most_similar(positive = word)
    except KeyError:
        return render_template('situation.html',the_word=word)
    else:
        return render_template('results.html',the_word=word,items=result)


app.run()
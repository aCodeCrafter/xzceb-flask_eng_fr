from machinetranslation import translator
from flask import Flask, render_template, request
import machinetranslation
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = machinetranslation.translator.englishToFrench(textToTranslate)
    return translated_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = machinetranslation.translator.frenchToEnglish(textToTranslate)
    return translated_text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    # with open('templates/index.html') as html_file:
    #     test = html_file.read()
    return render_template('index.html')
    # return test
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

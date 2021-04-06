import sys # This is for adding the /app folder to the system and calls internal functions organized inside folders
sys.path.insert(1, './app') # insert at 1, 0 is the script path (or '' in REPL)


from backend import *
from flask import Flask, jsonify, request

app= Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.config['JSON_SORT_KEYS'] = False 
TESTING = 1 #int( os.getenv('TESTING') )

@app.route('/predict', methods=['POST'])
def predict():
    if not TESTING:
        try:
            message = request.get_json().get('message', '')
            message = str(message)
            print(message)
        except:
            return jsonify( { 'error':['Bad Posting'] } )
        try:
            Pred, PredTh, error = Detection(message)
            dic = {'prediccion': [ PredTh ] , 'score' : Pred.tolist(), 
            'error': error, 'clases': {0:'clase 0', 1:'clase 1'} ,'filas': 0, 'columnas': 0}
            return jsonify( dic )
        except:
            dic = {'prediccion': [ [] ], 'error': 1}
            return jsonify( dic )
    else:
        message = request.get_json().get('message', '')
        message = str(message)
        Pred, PredTh, error = Detection(message)
        dic = {'prediccion': [ PredTh ] , 'score' : Pred.tolist(), 
            'error': error, 'clases': {0:'clase 0', 1:'clase 1'} ,'filas': 0, 'columnas': 0}
        return jsonify( dic )


@app.route('/sayHello', methods=['GET'])
def sayHello():
    try:
        return jsonify( { 'Hello':'I am alive'} )
    except:
        return jsonify( { 'error':'404'} )
    
if __name__ == '__main__':
    app.run(debug=False, host = '0.0.0.0', port = 8080)

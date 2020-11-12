from app.main import app 
from app.base import *
if __name__ == '__main__':
    print("Starting python app")
    app.run(host='0.0.0.0',port=8080,processes=8,threaded=False)

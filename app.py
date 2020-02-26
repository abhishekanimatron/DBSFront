from flask import Flask, render_template, request,  url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
print('How may i help you, sir?') 
def erase():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

 
class chat(db.Model):
    content = db.Column(db.String(200), nullable = False )
    date_created = db.Column(db.DateTime, default = datetime.utcnow, primary_key = True)
    def __ref__(self):
        return '<task %r>' % self.id
    
  

@app.route('/', methods = ['POST', 'GET'])
def reo():
         
    if request.method == 'POST': 
        text_content = request.form['text']
        print('----------------------------------------------')
        print("from user:",text_content)
        #print('----------------------------------------------')
        if text_content.lower() == 'schedule':
            print('----------------------------------------------')
            print('from bot: which train are you looking for?')
            print('----------------------------------------------')
        
        text_content = request.form['text']
        #print("from user:",text_content)
        if text_content.lower() == 'humsafar express':
            print('----------------------------------------------')
            print("""from bot: The humsafar Express's schedule is:
                Arrival Time: 16:00
                Number: 411459
                From: Raipur
                To: Nagpur""")
            print('----------------------------------------------')
        if text_content.lower() == 'hi':
            print('----------------------------------------------')
            print('from Bot: Hello')
            print('----------------------------------------------')
        if text_content.lower() == 'emergency':
            print('----------------------------------------------')
            print('from Bot: Please Dial 108')
            print('----------------------------------------------')
        if  'safar' in text_content.lower() :
            print('----------------------------------------------')
            print("i think you mean Humsafar Express:")
            print("""from bot: The humsafar Express's schedule is:
                Arrival Time: 16:00
                Number: 411459
                From: Raipur
                To: Nagpur""")
            
        
        '''
        q = request.form['name']
        # do for 12 more fields
        db.session.add(q)
        '''
        
        new_text = chat(content = text_content)
        
        db.session.add(new_text)
        db.session.commit()
        return redirect('/')
        '''
        except:
            return "try again //"  '''
    else:
        log = chat.query.order_by(chat.date_created).all()
        
        return render_template("basic.html", tasks = log)







if __name__ == "__main__":
    app.run()#debug = True)
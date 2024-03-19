# Import
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Zmienne umożliwiające obliczenie poboru energii przez urządzenia
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# Pierwsza strona
@app.route('/')
def index():
    return render_template('index.html')
# Druga strona
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# Trzecia strona
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

# Obliczenia
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
# Formularz
@app.route('/form')
def form():
    return render_template('form.html')

# Wyniki formularza
@app.route('/submit', methods=['POST'])
def submit_form():
    # Zadeklaruj zmienne do gromadzenia danych
    name = request.form['name']
    email = request.form['email']
    if request.form['check'] == 'on':
        check = 'tak'
    else:
        check = 'nie'
    address = request.form['address']
    date = request.form['date']
    with open("stolendata.txt", 'a') as data:
        data.write(f"name: {name}\n")
        data.write(f"email: {email}\n")
        data.write(f"is person 18 years old: {check}\n")
        data.write(f"where he or she lives: {address}\n")
        data.write(f"when not go to him: {date}\n")
    # Możesz zapisać swoje dane lub wysłać je e-mailem
    return render_template('form_result.html', 
                           # Umieść tutaj zmienne
                           name=name,
                           email=email,
                           check=check,
                           address=address,
                           date=date
                           )

app.run(debug=True)
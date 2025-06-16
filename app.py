from flask import Flask, render_template, request
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

app = Flask(__name__)

app.static_folder = 'static'
app.template_folder = 'templates'

# Routes and other configurations...
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_location', methods=['POST'])
def detect_location():
    mobile_number = request.form['mobile_number']
    
    try:
        phone_number = phonenumbers.parse(mobile_number, None)
        time_zones = timezone.time_zones_for_number(phone_number)
        mobile_company = carrier.name_for_number(phone_number, "en")
        region = geocoder.description_for_number(phone_number, "en")
        
        location = {
            'time_zones': list(time_zones),
            'mobile_company': mobile_company,
            'region': region
        }
        
        return render_template('result.html', location=location)
    except phonenumbers.phonenumberutil.NumberParseException:
        return render_template('result.html', error='Invalid phone number')

if __name__ == '__main__':
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True

# main.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    transport_options = request.form.getlist('transport_options[]')
    # Sample data objects
    train_data = [{'from': 'A', 'to': 'B', 'departure_time': '9:00 AM', 'arrival_time': '11:00 AM', 'price': 20},
                   {'from': 'B', 'to': 'C', 'departure_time': '12:00 PM', 'arrival_time': '2:00 PM', 'price': 25}]
    bus_data = [{'from': 'A', 'to': 'B', 'departure_time': '10:00 AM', 'arrival_time': '12:00 PM', 'price': 15},
                   {'from': 'B', 'to': 'C', 'departure_time': '1:00 PM', 'arrival_time': '3:00 PM', 'price': 20}]
    flight_data = [{'from': 'A', 'to': 'B', 'departure_time': '11:00 AM', 'arrival_time': '1:00 PM', 'price': 50},
                   {'from': 'B', 'to': 'C', 'departure_time': '2:00 PM', 'arrival_time': '4:00 PM', 'price': 60}]
    donkey_data = [{'from': 'A', 'to': 'B', 'departure_time': '8:00 AM', 'arrival_time': '12:00 PM', 'price': 10},
                   {'from': 'B', 'to': 'C', 'departure_time': '1:00 PM', 'arrival_time': '5:00 PM', 'price': 15}]
    ferry_data = [{'from': 'A', 'to': 'B', 'departure_time': '9:00 AM', 'arrival_time': '10:30 AM', 'price': 12},
                   {'from': 'B', 'to': 'C', 'departure_time': '11:00 AM', 'arrival_time': '12:30 PM', 'price': 14}]
    bike_data = [{'from': 'A', 'to': 'B', 'departure_time': '7:00 AM', 'arrival_time': '9:00 AM', 'price': 5},
                   {'from': 'B', 'to': 'C', 'departure_time': '10:00 AM', 'arrival_time': '12:00 PM', 'price': 7}]
    results = []
    for transport_option in transport_options:
        if transport_option == 'train':
            results.extend(train_data)
        elif transport_option == 'bus':
            results.extend(bus_data)
        elif transport_option == 'flight':
            results.extend(flight_data)
        elif transport_option == 'donkey':
            results.extend(donkey_data)
        elif transport_option == 'ferry':
            results.extend(ferry_data)
        elif transport_option == 'bike':
            results.extend(bike_data)
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)

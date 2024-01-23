from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def recommend_dogs():
    # Retrieve form data
    breed = request.form.get('breed')
    group = request.form.get('group')
    low_energy = 'energy' in request.form.getlist('low[]')
    low_grooming = 'grooming' in request.form.getlist('low[]')
    medium_training = 'training' in request.form.getlist('medium[]')
    medium_shedding = 'shedding' in request.form.getlist('medium[]')
    high_barking = 'barking' in request.form.getlist('high[]')

    # Perform recommendation logic
    recommendations = recommend_dogs(breed, group, low_energy, low_grooming, medium_training, medium_shedding, high_barking)

    # Render results template with recommendations
    return render_template('results.html', breed=breed, group=group, low=low_energy or low_grooming, medium=medium_training or medium_shedding, high=high_barking, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=False)

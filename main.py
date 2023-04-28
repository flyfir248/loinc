from flask import Flask, request, render_template, redirect, jsonify

app = Flask(__name__)

loinc_codes = {
    'sex_at_birth_male': '76689-9',
    'sex_at_birth_female': '76690-7',
    'sex_at_birth_not_specified': '85353-1',
    'age_years': '30525-0',
    'age_months': '36316-9',
    'height_cm': '8302-2',
    'weight_kg': '29463-7'
}


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/ionic_codes', methods=['POST'])
def get_ionic_codes():
    sex = request.form['sex']
    age = request.form['age']
    height = request.form['height']
    weight = request.form['weight']

    loinc_codes = {
        'sex_at_birth_male': '76689-9',
        'sex_at_birth_female': '76690-7',
        'sex_at_birth_not_specified': '85353-1',
        'age_years': '30525-0',
        'age_months': '36316-9',
        'height_cm': '8302-2',
        'weight_kg': '29463-7'
    }

    ionic_codes = []
    if sex == 'Male':
        ionic_codes.append(loinc_codes['sex_at_birth_male'])
    elif sex == 'Female':
        ionic_codes.append(loinc_codes['sex_at_birth_female'])
    else:
        ionic_codes.append(loinc_codes['sex_at_birth_not_specified'])

    if age:
        if 'y' in age.lower():
            ionic_codes.append(loinc_codes['age_years'])
        elif 'm' in age.lower():
            ionic_codes.append(loinc_codes['age_months'])

    if height:
        ionic_codes.append(loinc_codes['height_cm'])

    if weight:
        ionic_codes.append(loinc_codes['weight_kg'])

    return jsonify(ionic_codes)


if __name__ == '__main__':
    app.run(debug=True)
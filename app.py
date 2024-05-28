from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Carregar os modelos
with open('models/random_forest_tuned_important.pkl', 'rb') as f:
    rf_model = pickle.load(f)

with open('models/lightgbm_tuned_important.pkl', 'rb') as f:
    lgb_model = pickle.load(f)

# Função para fazer previsões
def predict(model, features):
    return model.predict([features])[0]

@app.route('/')
def home():
    return render_template('index.html', result=None)

@app.route('/predict', methods=['POST'])
def predict_price():
    model_choice = request.form['model']
    print("Modelo selecionado:", model_choice)  # Para depuração

    if model_choice == 'random_forest':
        try:
            latitude = float(request.form['latitude'])
            longitude = float(request.form['longitude'])
            size_house = float(request.form['size_house'])
            avg_size_neighbor_houses = float(request.form['avg_size_neighbor_houses'])
            year_built = int(request.form['year_built'])
            features = [latitude, size_house, avg_size_neighbor_houses, longitude, year_built]
            print("Features RF:", features)  # Para depuração
            result = predict(rf_model, features)
            print("Resultado RF:", result)  # Para depuração
        except Exception as e:
            print("Erro ao processar RF:", e)
            result = "Erro ao processar a previsão para Random Forest."

    elif model_choice == 'lightgbm':
        try:
            latitude = float(request.form['latitude'])
            longitude = float(request.form['longitude'])
            size_house = float(request.form['size_house'])
            avg_size_neighbor_houses = float(request.form['avg_size_neighbor_houses'])
            avg_size_neighbor_lot = float(request.form['avg_size_neighbor_lot'])
            size_lot = float(request.form['size_lot'])
            year_built = int(request.form['year_built'])
            size_basement = float(request.form['size_basement'])
            num_bath = int(request.form['num_bath'])
            num_bed = int(request.form['num_bed'])
            condition = int(request.form['condition'])
            zip_code = int(request.form['zip'])
            features = [latitude, size_house, avg_size_neighbor_houses, longitude, size_lot, year_built, avg_size_neighbor_lot, zip_code, size_basement, num_bath, num_bed, condition]
            print("Features LGBM:", features)  # Para depuração
            result = predict(lgb_model, features)
            print("Resultado LGBM:", result)  # Para depuração
        except Exception as e:
            print("Erro ao processar LGBM:", e)
            result = "Erro ao processar a previsão para LightGBM."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

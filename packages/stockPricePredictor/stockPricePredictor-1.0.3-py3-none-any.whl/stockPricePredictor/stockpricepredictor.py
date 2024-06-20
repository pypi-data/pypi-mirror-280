import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
import FinanceDataReader as fdr

class StockPricePredictor:
    def __init__(self, stock_code, start_date, end_date, future_steps):
        self.stock_code = stock_code
        self.start_date = start_date
        self.end_date = end_date
        self.future_steps = future_steps
        self.model = None
        self.scaler = MinMaxScaler(feature_range=(0, 1))

    def load_data(self):
        self.data = fdr.DataReader(self.stock_code, self.start_date, self.end_date)
        self.close_prices = self.data['Close'].values.reshape(-1, 1)
        self.close_prices_scaled = self.scaler.fit_transform(self.close_prices)

    def create_sequences(self, seq_length):
        xs, ys = [], []
        for i in range(len(self.close_prices_scaled)-seq_length-1):
            x = self.close_prices_scaled[i:(i+seq_length), 0]
            y = self.close_prices_scaled[i+seq_length, 0]
            xs.append(x)
            ys.append(y)
        return np.array(xs), np.array(ys)

    def train_model(self, seq_length=60):
        X, y = self.create_sequences(seq_length)
        train_size = int(len(X) * 0.8)
        self.X_train, self.X_test = X[:train_size], X[train_size:]
        self.y_train, self.y_test = y[:train_size], y[train_size:]

        self.X_train = np.reshape(self.X_train, (self.X_train.shape[0], self.X_train.shape[1], 1))
        self.X_test = np.reshape(self.X_test, (self.X_test.shape[0], self.X_test.shape[1], 1))

        self.model = Sequential()
        self.model.add(LSTM(units=50, return_sequences=True, input_shape=(self.X_train.shape[1], 1)))
        self.model.add(Dropout(0.2))
        self.model.add(LSTM(units=50, return_sequences=False))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(units=1))

        self.model.compile(optimizer='adam', loss='mean_squared_error')
        self.model.fit(self.X_train, self.y_train, epochs=100, batch_size=32)

    def predict_future_prices(self):
        predicted_stock_price = self.model.predict(self.X_test)
        predicted_stock_price = self.scaler.inverse_transform(predicted_stock_price)
        self.y_test_scaled = self.scaler.inverse_transform(self.y_test.reshape(-1, 1))

        last_sequence = self.X_test[-1]
        future_predictions = self.predict_future_prices_from_sequence(last_sequence, self.future_steps)
        future_predictions = self.scaler.inverse_transform(future_predictions)

        last_date = self.data.index[-1]
        self.future_dates = pd.date_range(last_date, periods=self.future_steps+1, inclusive='right')

        return predicted_stock_price, self.y_test_scaled, future_predictions

    def predict_future_prices_from_sequence(self, last_sequence, n_steps):
        future_predictions = []
        current_sequence = last_sequence.copy()

        for _ in range(n_steps):
            prediction = self.model.predict(current_sequence[np.newaxis, :, :])[0, 0]
            future_predictions.append(prediction)
            current_sequence = np.append(current_sequence[1:], [[prediction]], axis=0)

        return np.array(future_predictions).reshape(-1, 1)

    def visualize_results(self):
        predicted_stock_price, y_test_scaled, future_predictions = self.predict_future_prices()

        plt.figure(figsize=(14, 5))
        plt.plot(self.data.index[-len(y_test_scaled):], y_test_scaled, color='red', label='Actual Stock Price')
        plt.plot(self.data.index[-len(y_test_scaled):], predicted_stock_price, color='blue', label='Predicted Stock Price')
        plt.plot(self.future_dates, future_predictions, color='green', label='Future Predicted Stock Price')
        plt.title(f'{self.stock_code} Stock Price Prediction')
        plt.xlabel('Date')
        plt.ylabel('Stock Price')
        plt.legend()
        plt.show()
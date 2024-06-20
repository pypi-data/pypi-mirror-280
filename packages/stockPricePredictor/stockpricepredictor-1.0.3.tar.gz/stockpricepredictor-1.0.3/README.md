LSTM 모델을 사용하여 주식가격을 예측하는 라이브러리입니다
사용법
예시

import stockpricepredictor as spp
import datetime

today = datetime.date.today().strftime('%Y-%m-%d')
stock_predictor = spp.StockPricePredictor('NVDA', '2020-01-01', today , 2)
stock_predictor.load_data()
stock_predictor.train_model()
stock_predictor.visualize_results()

NVDA자리에는 주식 항목 코드, 2020-01-01과 주식 데이터를 가져올 시점,todat는 오늘 날짜,2는 향후 몇일동안의 주가를 예측할 것인지 설정합니다.
해외주식코드만 가능합니다 ex)엔비디아: NVDA, 애플: AAPL
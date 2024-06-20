import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup (
    name = 'stockPricePredictor',
    version = '1.0.3',
    license = 'MIT',
    description = 'LSTM 모델을 사용한 주식 가격 예측하기',
    author = 'jiwonchoi',
    author_email = 'chooijuwonwon1123456@gmail.com',
    url = '',
    packages = setuptools.find_packages(),
    classifiers = [
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
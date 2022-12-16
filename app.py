from flask import Flask, jsonify, abort, make_response
import json
import psycopg2
import pandas.io.sql as sqlio

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
conn = psycopg2.connect(
    host="localhost",
    database="stock_predicting",
    user="stock",
    password="stock",
    port="5433"
)
cursor = conn.cursor()

def select_companies():
    return sqlio.read_sql_query('select ticker from companies', conn)

def select_company(company_ticker):
    return sqlio.read_sql_query(f'select id, ticker from companies where ticker=\'{company_ticker}\'', conn)


def select_quote(company_id):
    return sqlio.read_sql_query(
        f'select date_, time_, open_ from quotes where company_id = {company_id} order by date_ desc, time_ desc limit 100;', conn)


def select_news(company_id):
    return sqlio.read_sql_query(
        f'select news.id, news.content, news.title from news where company_id={company_id} order by date_time desc limit 5',
        conn
    )



@app.route('/api/company/<string:company_ticker>', methods=['GET'])
def get_company(company_ticker):  # put application's code here
    company = select_company(company_ticker)
    if company.shape[0] == 0:
        abort(404)
    company_id = company.iloc[0]['id']
    news = select_news(company_id)
    qoutes = select_quote(company_id)

    json_news = news.to_json(orient="table")
    parsed_news = json.loads(json_news)
    json.dumps(parsed_news, indent=4)

    json_qoutes = qoutes.to_json(orient="table")
    parsed_qoutes = json.loads(json_qoutes)
    json.dumps(parsed_qoutes, indent=4)

    suggest = "example"

    return jsonify({'news': parsed_news['data'], 'quotes': parsed_qoutes['data'], 'suggest': suggest})


@app.route('/api/companies', methods=['GET'])
def get_companies():
    tickers = select_companies()
    json_tickers = tickers.to_json(orient="table")
    parsed_tickers = json.loads(json_tickers)
    json.dumps(parsed_tickers, indent=4)
    return jsonify({'tickers': parsed_tickers['data']})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run()

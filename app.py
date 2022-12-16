from flask import Flask, jsonify, abort, make_response
import requests
import json
import psycopg2
import pandas as pd
import pandas.io.sql as sqlio

app = Flask(__name__)
conn = psycopg2.connect(
    host="localhost",
    database="iad2",
    user="postgres",
    password="123",
    port="5432"
)
cursor = conn.cursor()


def select_company(company_ticker):
    return sqlio.read_sql_query(f'select id, ticker from company where ticker=\'{company_ticker}\'', conn)


def select_quote(company_id):
    return sqlio.read_sql_query(
        f'select date, time, open from quote where company_id = {company_id} order by date, time limit 100', conn)


def select_news(company_id):
    return sqlio.read_sql_query(
        f'select news.id, news.news_text, news.topic from news left join craudsource c on news.id = c.news_id where c.news_id IS NULL and news.company_id={company_id}',
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

    json_news = news[0:2].to_json(orient="table")
    parsed_news = json.loads(json_news)
    json.dumps(parsed_news, indent=4)

    json_qoutes = qoutes.to_json(orient="table")
    parsed_qoutes = json.loads(json_qoutes)
    json.dumps(parsed_qoutes, indent=4)

    suggest = "example"

    return jsonify({'news': parsed_news, 'qoutes': parsed_qoutes, 'suggest': suggest})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run()

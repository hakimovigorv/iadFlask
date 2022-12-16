insert into company(ticker) VALUES ('YNDX');
insert into company(ticker) VALUES ('SBER');
insert into company(ticker) VALUES ('BIBA');

insert into quote(company_id, date, time, open, high, low, close, vol) values (1, '2017-03-14', '13:00:00', 1000.0, 1001.0, 999.0, 1000.0, 1);
insert into quote(company_id, date, time, open, high, low, close, vol) values (1, '2017-03-14', '13:10:00', 1100.0, 1001.0, 999.0, 1000.0, 1);
insert into quote(company_id, date, time, open, high, low, close, vol) values (1, '2017-03-14', '13:20:00', 1120.0, 1001.0, 999.0, 1000.0, 1);
insert into quote(company_id, date, time, open, high, low, close, vol) values (1, '2017-03-14', '13:30:00', 1123.0, 1001.0, 999.0, 1000.0, 1);
insert into quote(company_id, date, time, open, high, low, close, vol) values (1, '2017-03-14', '13:40:00', 1125.0, 1001.0, 999.0, 1000.0, 1);
insert into quote(company_id, date, time, open, high, low, close, vol) values (1, '2017-03-11', '13:00:00', 1000.0, 1001.0, 999.0, 1000.0, 1);
insert into quote(company_id, date, time, open, high, low, close, vol) values (1, '2017-03-12', '13:10:00', 1100.0, 1001.0, 999.0, 1000.0, 1);
insert into quote(company_id, date, time, open, high, low, close, vol) values (1, '2017-03-13', '13:20:00', 1120.0, 1001.0, 999.0, 1000.0, 1);
insert into quote(company_id, date, time, open, high, low, close, vol) values (1, '2017-03-14', '13:30:00', 1123.0, 1001.0, 999.0, 1000.0, 1);
insert into quote(company_id, date, time, open, high, low, close, vol) values (1, '2017-03-15', '13:40:00', 1125.0, 1001.0, 999.0, 1000.0, 1);

insert into quote(company_id, date, time, open, high, low, close, vol) values (2, '2017-03-14', '13:00:00', 1000.0, 1001.0, 999.0, 1000.0, 1);
insert into quote(company_id, date, time, open, high, low, close, vol) values (2, '2017-03-14', '13:10:00', 1100.0, 1001.0, 999.0, 1000.0, 1);
insert into quote(company_id, date, time, open, high, low, close, vol) values (2, '2017-03-14', '13:20:00', 1120.0, 1001.0, 999.0, 1000.0, 1);
insert into quote(company_id, date, time, open, high, low, close, vol) values (2, '2017-03-14', '13:30:00', 1123.0, 1001.0, 999.0, 1000.0, 1);
insert into quote(company_id, date, time, open, high, low, close, vol) values (2, '2017-03-14', '13:40:00', 1125.0, 1001.0, 999.0, 1000.0, 1);

insert into quote(company_id, date, time, open, high, low, close, vol) values (3, '2017-03-14', '13:00:00', 1000.0, 1001.0, 999.0, 1000.0, 1);
insert into quote(company_id, date, time, open, high, low, close, vol) values (3, '2017-03-14', '13:10:00', 1100.0, 1001.0, 999.0, 1000.0, 1);
insert into quote(company_id, date, time, open, high, low, close, vol) values (3, '2017-03-14', '13:20:00', 1120.0, 1001.0, 999.0, 1000.0, 1);
insert into quote(company_id, date, time, open, high, low, close, vol) values (3, '2017-03-14', '13:30:00', 1123.0, 1001.0, 999.0, 1000.0, 1);
insert into quote(company_id, date, time, open, high, low, close, vol) values (3, '2017-03-14', '13:40:00', 1125.0, 1001.0, 999.0, 1000.0, 1);

insert into news(company_id, news_text, topic) VALUES (1, 'test news text 1 1\\n vsem privet', 'Best topic ever 1 1 ');
insert into news(company_id, news_text, topic) VALUES (1, 'test news text 2 1\\n vsem privet', 'Best topic ever 2 1');
insert into news(company_id, news_text, topic) VALUES (1, 'test news text 3 1\\n vsem privet', 'Best topic ever 3 1');
\
insert into news(company_id, news_text, topic) VALUES (2, 'test news text 1 2\\n vsem privet', 'Best topic ever  1 1');
insert into news(company_id, news_text, topic) VALUES (2, 'test news text 2 2\\n vsem privet', 'Best topic ever  2 1');
insert into news(company_id, news_text, topic) VALUES (2, 'test news text 3 2\\n vsem privet', 'Best topic ever  3 1');
\
insert into news(company_id, news_text, topic) VALUES (3, 'test news text 1 3\\n vsem privet', 'Best topic ever  1 1');
insert into news(company_id, news_text, topic) VALUES (3, 'test news text 2 3\\n vsem privet', 'Best topic ever  2 1');
insert into news(company_id, news_text, topic) VALUES (3, 'test news text 3 3\\n vsem privet', 'Best topic ever  3 1');
\
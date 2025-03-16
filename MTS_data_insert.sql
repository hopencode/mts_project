delete from company_balance;
delete from customer_balance;
delete from sell_list;
delete from buy_list;
delete from order_list;
delete from financial_info;
delete from company;
delete from admin;
delete from account;


insert into account values ('alice1', 'alice123', '12341234', 'customer', 'alice', '010-1234-1234', 10000000, 3000000);
insert into account values ('mark1', 'mark123', '12341235', 'customer', 'mark', '010-1234-1235', 10000, 0);
insert into account values ('chars1', 'chars123', '12341236', 'customer', 'chars', '010-1234-1236', 10000, 0);

insert into account values ('Microsoft1', 'Microsoft123', '12341237', 'company', 'Microsoft', '010-1234-1237', 10000, 0);
insert into account values ('Ford1', 'Ford123', '12341238', 'company', 'Ford', '010-1234-1238', 10000, 0);
insert into account values ('PG1', 'PG123', '12341239', 'company', 'Pg', '010-1234-1239', 10000, 0);


insert into admin values ('admin1', 'admin123', 'admin');


insert into company values ('Microsoft', 500000, 7000, 3500000000, 'IT');
insert into company values ('Amazon', 400000, 6000, 2400000000, 'IT');
insert into company values ('Ford', 100000, 2000, 200000000, 'consumer discretionary');
insert into company values ('Pg', 300000, 1000, 300000000, 'consumer staple');


insert into financial_info values ('Microsoft', 2023, 240000000, 120000000, 118000000, 1.7, 5, 29.4, 10);
insert into financial_info values ('Microsoft', 2022, 220000000, 108000000, 96000000, 1.5, 4.5, 27, 9);
insert into financial_info values ('Ford', 2023, 250000000, 25000000, 24000000, 1.25, 4.17, 8, 2.4);
insert into financial_info values ('Pg', 2023, 120000000, 12000000, 11000000, 1.22, 3, 24.6, 10);

insert into order_list values ('12341237', 'sell', 'Microsoft', 600000, 10, 1);
insert into order_list values ('12341239', 'buy', 'Pg', 350000, 7, 2);
insert into order_list values ('12341239', 'buy', 'Pg', 250000, 3, 3);
insert into order_list values ('12341235', 'sell', 'Ford', 130000, 1, 4);
insert into order_list values ('12341235', 'sell', 'Ford', 130000, 1, 5);

insert into buy_list values (1, '12341237', 'Microsoft', 500000, '2024-12-07', '11:35:00', 7000, 0);
insert into buy_list values (2, '12341238', 'Ford', 100000, '2024-12-07', '11:35:00', 2000, 1);
insert into buy_list values (3, '12341239', 'Pg', 300000, '2024-12-07', '11:35:00', 1000, 10);
insert into buy_list values (4, '12341234', 'Pg', 310000, '2024-12-07', '11:35:00', 5, 0);
insert into buy_list values (5, '12341234', 'Pg', 320000, '2024-12-07', '11:35:00', 5, 0);
insert into buy_list values (6, '12341235', 'Ford', 120000, '2024-12-07', '11:35:00', 2, 0);

insert into sell_list values (1, '12341238', 'Ford', 100000, 120000, '2024-12-07', '11:35:00', 2);
insert into sell_list values (2, '12341239', 'Pg', 300000, 310000, '2024-12-07', '11:35:00', 5);
insert into sell_list values (3, '12341239', 'Pg', 300000, 320000, '2024-12-07', '11:35:00', 5);


insert into customer_balance values ('12341234', 'Pg', 10, 315000);
insert into customer_balance values ('12341235', 'Ford', 0, 120000);

insert into company_balance values ('12341237', 'Microsoft', 6990, 500000);
insert into company_balance values ('12341238', 'Ford', 1998, 100000);
insert into company_balance values ('12341239', 'Pg', 990, 300000);




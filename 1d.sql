create table invoices (
    id                  integer,
    total               decimal,
    invoice_date_time   timestamp not null,
    paid                boolean default false
);

insert into invoices (id, total, invoice_date_time, paid) values (123, 3444.50, '2017-01-01', true);

insert into invoices (id, total, invoice_date_time) values (124, 3445.50, '2017-01-02');

select * from invoices;

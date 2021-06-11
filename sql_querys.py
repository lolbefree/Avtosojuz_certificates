
def history():
    return """select b.wrkordno, b.date, b.usedsum, b.balance from bigcert_header a
inner join bigcert b
on a.id = b.id
where tel= 503539838
order by b.date

"""

def balance():
    return """
select h.id,a.balance from (
select id,max(date) as date,min(balance) as balance from bigcert group by id) a

join bigcert_header h on a.id=h.id
where h.tel=503539838"""


def add_cert_to_base(id, cust_name,tel, certsum, salesman, comment, email):
    return f"""
    insert into amintegrations.dbo.bigcert_header(id, cust_name,tel, certsum, salesman, date, comment, email)
VALUES ({id}, '{cust_name}', {tel},{certsum},'{salesman}' ,GETDATE(), '{comment}', '{email}');
    """


def if_exit_id(x):
    return  f"""
          if exists (
          select id from amintegrations.dbo.bigcert_header where id={x})                                               
          select 'true'
          else select 'none'
        """  # наличие в базе такой ид карточки
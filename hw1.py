import sqlalchemy
from sqlalchemy import func,text
from sqlalchemy.orm import DeclarativeBase,mapped_column,Session
from sqlalchemy import INTEGER,VARCHAR,DATE,select,case,literal,desc
def problem_1(connection,test = False):
    #List, for every boat, the number of times it has been reserved, excluding those boats that have never been reserved (list the id and the name).
    query = "SELECT boats.bid, boats.bname, COUNT(boats.bid) times_reserved FROM boats INNER JOIN reserves ON boats.bid = reserves.bid GROUP BY boats.bid;"
    result = connection.execute(text(query))
    if test:
        return result
    print(f"Query is {query}")
    for row in result:
        print(f"Boat id:{row.bid}, Boat name:{row.bname}, Times Reserved: {row.times_reserved} ")

def problem_2(connection, test = False):
    #List those sailors who have reserved every red boat (list the id and the name).
    query ="SELECT sailors.sid, sailors.sname FROM sailors INNER JOIN reserves on sailors.sid = reserves.sid INNER JOIN boats on reserves.bid = boats.bid WHERE boats.color='red' GROUP BY sailors.sid HAVING COUNT(sailors.sid) = (SELECT sum(case when boats.color='red' then 1 else 0 end) FROM boats); "
    result = connection.execute(text(query))
    if test:
        return result
    print(f"Query is {query}")
    for row in result:
        print(f"Sailor with name {row.sname} and id {row.sid} has rented every red boat")


def problem_3(connection, test = False):
    #sailors who have reserved only red boats
    query = 'SELECT sailors.sid, sailors.sname FROM sailors INNER JOIN reserves on sailors.sid = reserves.sid INNER JOIN boats on reserves.bid = boats.bid  GROUP BY sailors.sid HAVING (SELECT SUM(case when color = \'red\' then 0 else 1 end)) = 0;'
    result = connection.execute(text(query))
    if test:
        return result
    print(f"Query is {query}")
    for row in result:
        print(f"Sailor with name {row.sname} and id {row.sid} has only rented red boats")

def problem_4(connection, test = False):
    #for which boat are there the most reservations
    query = 'SELECT boats.bid, boats.bname, COUNT(boats.bid) times_reserved FROM boats INNER JOIN reserves ON boats.bid = reserves.bid GROUP BY boats.bid ORDER BY COUNT(boats.bid) DESC LIMIT 1;'
    result = connection.execute(text(query))
    if test:
        return result
    print(f"Query is {query}")
    for row in result:
        print(f"The boat with id {row.bid} and name {row.bname} has been reserved the most times, with {row.times_reserved} reservations")

def problem_5(connection,test = False):
    # Select all sailors who never returned a red boat
    query = 'SELECT sailors.sid, sailors.sname FROM sailors INNER JOIN reserves on sailors.sid = reserves.sid INNER JOIN boats on reserves.bid = boats.bid  GROUP BY sailors.sid HAVING (SELECT SUM(case when color = \'red\' then 1 else 0 end)) = 0;'
    result = connection.execute(text(query))
    if test:
        return result
    print(f"Query is {query}")
    for row in result:
        print(f"Sailor with name {row.sname} and id {row.sid} has never rented a red boat")

def problem_6(connection, test = False):
    # Find the average age of sailors with a rating of 10
    query = 'SELECT AVG(age) average FROM sailors WHERE rating = \'10\';'
    result = connection.execute(text(query))
    if test:
        return result
    print(f"Query is {query}")
    for row in result:
        print(f"Average age of sailors with rating of 10 is {row.average}")

def problem_7(connection, test = False):
    # For each rating, find the name and id of the youngest sailor
    query = "SELECT DISTINCT ON (rating) rating, sname,sid FROM sailors ORDER BY rating,age;"
    result = connection.execute(text(query))
    if test:
        return result
    print(f"Query is {query}")
    for row in result:
        print(f"The youngest sailor for rating {row.rating} has the name {row.sname} and id {row.sid}")

def problem_8(connection, test = False):
    # Select, for each boat, the sailor who made the highest number of reservations for that boat
    query = 'SELECT DISTINCT ON (reserves.bid) reserves.bid,sid, COUNT(sid) FROM reserves INNER JOIN boats on boats.bid = reserves.bid GROUP BY reserves.bid, sid ORDER BY reserves.bid, count DESC;'
    result = connection.execute(text(query))
    if test:
        return result
    print(f"Query is {query}")
    for row in result:
        print(f"The sailor who made the most reservations for boat with id {row.bid} has the id {row.sid}")


def problem1_orm(session, test = False):
    stmt = select(Boats.bid,Boats.bname,func.count(Boats.bid)).join(Reserves,Boats.bid == Reserves.bid).group_by(Boats.bid)
    #stmt = select(Boats)
    result = session.execute(stmt).all()
    if test:
        return result
    for entry in result:
        print(entry)

def problem2_orm(session, test = False):
    #"SELECT sailors.sid, sailors.sname FROM sailors INNER JOIN reserves on sailors.sid = reserves.sid INNER JOIN boats on reserves.bid = boats.bid WHERE boats.color='red' GROUP BY sailors.sid HAVING COUNT(sailors.sid) = (SELECT sum(case when boats.color='red' then 1 else 0 end) FROM boats); "
    stmt = select(Sailor.sid,Sailor.sname).join(Reserves,Sailor.sid == Reserves.sid).join(Boats,Boats.bid == Reserves.bid).where(Boats.color == 'red').group_by(Sailor.sid).having(func.count(Sailor.sid) == select(func.sum(case((Boats.color == 'red',1),else_=0))))
    result = session.execute(stmt).all()
    if test:
        return result
    for entry in result:
        print(entry)


def problem3_orm(session, test = False):
    # 'SELECT sailors.sid, sailors.sname FROM sailors INNER JOIN reserves on sailors.sid = reserves.sid INNER JOIN boats on reserves.bid = boats.bid  GROUP BY sailors.sid HAVING (SELECT SUM(case when color = \'red\' then 0 else 1 end)) = 0;'
    stmt = select(Sailor.sid, Sailor.sname).join(Reserves,Sailor.sid == Reserves.sid).join(Boats,Reserves.bid == Boats.bid).group_by(Sailor.sid).having(func.sum(case((Boats.color == 'red',0),else_=1)) == 0)
    result = session.execute(stmt).all()
    if test:
        return result
    for entry in result:
        print(entry)

def problem4_orm(session, test = False):
    #'SELECT boats.bid, boats.bname, COUNT(boats.bid) times_reserved FROM boats INNER JOIN reserves ON boats.bid = reserves.bid GROUP BY boats.bid ORDER BY COUNT(boats.bid) DESC LIMIT 1;'
    stmt = select(Boats.bid, Boats.bname, func.count(Boats.bid).label("times_reserved")).join(Reserves, Reserves.bid == Boats.bid).group_by(Boats.bid).order_by(text('times_reserved DESC'))
    result = session.execute(stmt).first()
    if test:
        return result
    print(result)

def problem5_orm(session, test = False):
    # 'SELECT sailors.sid, sailors.sname FROM sailors INNER JOIN reserves on sailors.sid = reserves.sid INNER JOIN boats on reserves.bid = boats.bid  GROUP BY sailors.sid HAVING (SELECT SUM(case when color = \'red\' then 1 else 0 end)) = 0;'
    stmt = select(Sailor.sid, Sailor.sname).join(Reserves, Sailor.sid == Reserves.sid).join(Boats,Reserves.bid == Boats.bid).group_by(Sailor.sid).having(func.sum(case((Boats.color == 'red',1),else_=0)) == 0)
    result = session.execute(stmt).all()
    if test:
        return result
    for entry in result:
        print(entry)

def problem6_orm(session, test = False):
    # 'SELECT AVG(age) average FROM sailors WHERE rating = \'10\';'
    stmt = select(func.avg(Sailor.age)).where(Sailor.rating == 10)
    result = session.execute(stmt).all()
    if test:
        return result
    for entry in result:
        print(entry)


def problem7_orm(session, test = False):
    # "SELECT DISTINCT ON (rating) rating, sname,sid FROM sailors ORDER BY rating,age;"
    stmt = select(Sailor.rating,Sailor.sname,Sailor.sid).distinct(Sailor.rating).order_by(Sailor.rating,Sailor.age)
    result = session.execute(stmt).all()
    if test:
        return result
    for entry in result:
        print(entry)

def problem8_orm(session, test = False):
    # 'SELECT DISTINCT ON (reserves.bid) reserves.bid,sid, COUNT(sid) FROM reserves INNER JOIN boats on boats.bid = reserves.bid GROUP BY reserves.bid, sid ORDER BY reserves.bid, count DESC;'
    stmt = select(Reserves.bid,Reserves.sid,func.count(Reserves.sid).label('count')).distinct(Reserves.bid).join(Boats,Reserves.bid == Boats.bid).group_by(Reserves.bid,Reserves.sid).order_by(Reserves.bid).order_by(text('count DESC'))
    result = session.execute(stmt).all()
    if test:
        return result
    for entry in result:
        print(entry)



class Base(DeclarativeBase):
    pass

class Sailor(Base):
    __tablename__ = "sailors"

    sid = mapped_column(INTEGER,primary_key=True)
    sname  = mapped_column(VARCHAR(30))
    rating = mapped_column(INTEGER)
    age = mapped_column(INTEGER)
    def __repr__(self) -> str:
        return f"Sailor(id={self.sid!r}, name={self.sname!r}, rating={self.rating!r})"
    

class Reserves(Base):
    __tablename__ = "reserves"

    sid = mapped_column(INTEGER, primary_key=True)
    bid = mapped_column(INTEGER, primary_key=True )
    day = mapped_column(DATE, primary_key=True)
    def __repr__(self) -> str:
        return f"Reservation(sailor_id={self.sid!r}, boat_id={self.bid!r}, day={self.day!r})"
    

class Boats(Base):
    __tablename__ = "boats"

    bid = mapped_column(INTEGER, primary_key=True, nullable=False)
    bname = mapped_column(VARCHAR(20))
    color = mapped_column(VARCHAR(10))
    length = mapped_column(INTEGER)
    def __repr__(self) -> str:
        return f"Boat(boat_id={self.bid!r}, boat_name={self.bname!r}, color={self.color!r}, length = {self.length!r})"
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy import text
    engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5432/sailors_boats', echo=True)
    with engine.connect() as connection:
        for row in problem_7(connection,True):
            print(row)
   # "SELECT boats.bid, boats.bname, COUNT(boats.bid) times_reserved FROM boats INNER JOIN reserves ON boats.bid = reserves.bid GROUP BY boats.bid;"
    session = Session(engine)
    problem7_orm(session)
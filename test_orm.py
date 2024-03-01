import pytest
from hw1 import Sailor,Boats,Reserves
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
def test_question1():
    from hw1 import problem_1,problem1_orm
    engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5432/sailors_boats', echo=True)
    with engine.connect() as connection:
        result = problem_1(connection,True)
    session = Session(engine)
    orm_result = problem1_orm(session,True)
    #assert result == orm_result
    norm_results = []
    orm_results = []
    for row1,row2 in zip(result,orm_result):
        norm_results.append(row1)
        orm_results.append(row2)
    assert norm_results == orm_results

def test_question2():
    from hw1 import problem_2,problem2_orm
    engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5432/sailors_boats', echo=True)
    with engine.connect() as connection:
        result = problem_2(connection,True)
    session = Session(engine)
    orm_result = problem2_orm(session,True)
    #assert result == orm_result
    norm_results = []
    orm_results = []
    for row1,row2 in zip(result,orm_result):
        norm_results.append(row1)
        orm_results.append(row2)
    assert norm_results == orm_results



def test_question3():
    from hw1 import problem_3,problem3_orm
    engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5432/sailors_boats', echo=True)
    with engine.connect() as connection:
        result = problem_3(connection,True)
    session = Session(engine)
    orm_result = problem3_orm(session,True)
    #assert result == orm_result
    norm_results = []
    orm_results = []
    for row1,row2 in zip(result,orm_result):
        norm_results.append(row1)
        orm_results.append(row2)
    assert norm_results == orm_results

def test_question4():
    from hw1 import problem_4,problem4_orm
    engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5432/sailors_boats', echo=True)
    with engine.connect() as connection:
        result = problem_4(connection,True)
    session = Session(engine)
    orm_result = problem4_orm(session,True)
    #assert result == orm_result
    norm_results = []
    for row1 in result:
        norm_results.append(row1)
    assert norm_results[0] == orm_result

def test_question5():
    from hw1 import problem_5,problem5_orm
    engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5432/sailors_boats', echo=True)
    with engine.connect() as connection:
        result = problem_5(connection,True)
    session = Session(engine)
    orm_result = problem5_orm(session,True)
    #assert result == orm_result
    norm_results = []
    orm_results = []
    for row1,row2 in zip(result,orm_result):
        norm_results.append(row1)
        orm_results.append(row2)
    assert norm_results == orm_results

def test_question6():
    from hw1 import problem_6,problem6_orm
    engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5432/sailors_boats', echo=True)
    with engine.connect() as connection:
        result = problem_6(connection,True)
    session = Session(engine)
    orm_result = problem6_orm(session,True)
    #assert result == orm_result
    norm_results = []
    orm_results = []
    for row1,row2 in zip(result,orm_result):
        norm_results.append(row1)
        orm_results.append(row2)
    assert norm_results == orm_results

def test_question7():
    from hw1 import problem_7,problem7_orm
    engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5432/sailors_boats', echo=True)
    with engine.connect() as connection:
        result = problem_7(connection,True)
    session = Session(engine)
    orm_result = problem7_orm(session,True)
    #assert result == orm_result
    norm_results = []
    orm_results = []
    for row1,row2 in zip(result,orm_result):
        norm_results.append(row1)
        orm_results.append(row2)
    assert norm_results == orm_results

def test_question8():
    from hw1 import problem_8,problem8_orm
    engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5432/sailors_boats', echo=True)
    with engine.connect() as connection:
        result = problem_8(connection,True)
    session = Session(engine)
    orm_result = problem8_orm(session,True)
    #assert result == orm_result
    norm_results = []
    orm_results = []
    for row1,row2 in zip(result,orm_result):
        norm_results.append(row1)
        orm_results.append(row2)
    assert norm_results == orm_results
from flask import Flask
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time
import json

app = Flask(__name__)

engine = create_engine('sqlite:///./db.sqlite', echo=False)
session = sessionmaker(bind=engine)()
Base = declarative_base(bind=engine)


class DataSet(Base):
    __tablename__ = 'dataset'
    id = Column(Integer, primary_key=true, autoincrement=True)
    timestamp = Column(Float, nullable=false)
    payload_data = Column(Integer, nullable=false)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

Base.metadata.create_all()


@app.route('/')
def hello_api():
    return 'Hello, welcome to the api! For documentation see <a href=github.com/harry-r/piduino-sensor>Github</a>'


@app.route('/write/<int:data>')
def write_data(data):
    dataset = DataSet()
    dataset.timestamp = time.time()
    dataset.payload_data = data
    session.add(dataset)
    session.commit()
    return 'ok'


@app.route('/read/<int:id>')
def read_data(id):
    for dataset in session.query(DataSet).filter(DataSet.id == id):
        print(dataset.as_dict())
        return json.dumps(dataset.as_dict(), ensure_ascii=False)


session.close()

if __name__ == '__main__':
    app.run()

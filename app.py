from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
engine = create_engine('sqlite:///ab_testing.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Experiment(Base):
    __tablename__ = 'experiment'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    variant_a = Column(Integer, default=0)
    variant_b = Column(Integer, default=0)


@app.route('/')
def home():
    session = Session()
    experiments = session.query(Experiment).all()
    session.close()

    return render_template('index.html', experiments=experiments)

# click event sends information back
@app.route('/track_click', methods=['POST'])
def track_click():
    element_id = request.json.get('element_id')
    # Process and store the click information as needed
    # You can save it to a database, log file, or perform any other desired action
    # ...
    return 'OK'

@app.route('/increment/<experiment_id>/<variant>')
def increment(experiment_id, variant):
    session = Session()
    experiment = session.query(Experiment).get(experiment_id)
    if variant == 'A':
        experiment.variant_a += 1
    elif variant == 'B':
        experiment.variant_b += 1
    session.commit()
    session.close()

    return redirect('/')


if __name__ == '__main__':
    # Create the database tables
    Base.metadata.create_all(engine)
    app.run(debug=True)

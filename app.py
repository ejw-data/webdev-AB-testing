from flask import Flask, render_template, request, redirect, make_response, json, jsonify
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

    output=[]
    for result in experiments:
        output.append({'item_clicked':result.name})


    if 'ejw' in request.cookies:
        print("\nHOME ROUTE:  Cookie found...\n")
        return render_template('index.html', experiments=output)
    else:
        response = make_response(render_template('index.html', experiments=output))
        response.headers['X-Parachutes'] = 'parachutes are cool'
        response.set_cookie('ejw',  value='464535346',
                                    max_age = 3600,
                                    # expires = "date-time format",
                                    # path = "",
                                    # domain = "",
                                    # httponly = "",
                                    secure=True
                                    )

        return response

# click event sends information back - see tracker.js
@app.route('/track_click', methods=['POST'])
def track_click():
    element_id = request.json.get('element_id')

    # ...
    record = Experiment(name=element_id)

    # add record
    session = Session()
    session.add(record)
    session.commit()
    session.close()

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

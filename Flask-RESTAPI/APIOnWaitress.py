# pip install waitress

from flask import Flask
from flask_restful import Resource,Api
from waitress import serve

app=Flask(__name__)
api=Api(app)

class Film(Resource):
    def get(self):
        film_data={
        "title": "The Matrix",
        "release_year": 1999,
        "directed_by": "The Wachowskis",
        "written_by": "The Wachowskis",
        "produced_by": "Joel Silver",
        "starring": [
            "Keanu Reeves",
            "Laurence Fishburne",
            "Carrie-Anne Moss",
            "Hugo Weaving",
            "Joe Pantoliano"
        ],
        "cinematography": "Bill Pope",
        "edited_by": "Zach Staenberg",
        "music_by": "Don Davis",
        "production_companies": [
            "Village Roadshow Pictures",
            "Groucho II Film Partnership",
            "Silver Pictures"
        ],
        "distributed_by": [
            "Warner Bros. (worldwide)",
            "Roadshow Entertainment (Australia)"
        ],
        "release_dates": {
            "premiere": "March 24, 1999",
            "US": "March 31, 1999",
            "Australia": "April 8, 1999"
        },
        "running_time_minutes": 136,
        "countries": ["United States", "Australia"],
        "language": "English",
        "budget_usd": 63000000,
        "box_office_usd": 467800000,
        "ratings": {
            "IMDb": 8.7,
            "RottenTomatoes": 83,
            "Metacritic": 73
        },
        "plot_summary": "In a dystopian future, humanity is unknowingly trapped inside the Matrix, a simulated reality created by intelligent machines. A hacker named Neo is recruited by rebels who believe he is 'the One' destined to defeat the machines."
        }  
        return film_data

api.add_resource(Film,"/film")
#app.run(debug=True)

if __name__=='__main__':
    serve(app,host='127.0.0.1',port=5001,threads=4)

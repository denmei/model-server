# ML-Server
A simple application to deploy my Machine Learning models and make them accessible via a REST-API.
Implemented with the Django-Framework.
The application is hosted on Heroku. Find the documentation for the REST-API here.

## Available Apps/Models
Each app contains one specific model:

### Artist Recommender
Model that can be used to retrieve recommendations for similar artists given one specific artist. 

#### GET: /music_recommender/api/artist_list 
Provides a list of all available artists. Can be used e.g. for autocompletion where user has to type in an artist.
##### Parameters:
* `contentType`: 'application/json',
* `headers`:
    * `Accept`: 'application/json'
    * `Content-Type`: 'application/json'

##### Output: 
[{`id`: ___, `name`: ___}, ...] 

#### POST: /music_recommender/api/artist_recommendation
Returns a list of the n most similar artists together with their distances from the artist in the input parameters.
##### Parameters:
* `contentType`: 'application/json',
* `headers`:
    * `Accept`: 'application/json'
    * `Content-Type`: 'application/json'
* `data`:
    * `artist`: string with artist name
    * `number`: Integer defining the required number of recommendations
##### Output:  
* `recommendations`: [{`name`: __, `distance`: __}, ...]
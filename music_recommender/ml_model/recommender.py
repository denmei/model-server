import os
import pickle
from ml_server.settings import BASE_DIR
import pandas as pd
from django.core.cache import cache


def get_artist_recommendations(artist_name, number=5):
    """
    Returns recommendations for a specific artists.
    :param artist_name: Input artist.
    :param number: Number of recommendations to be made. Max = 20.
    :return: List of recommendations.
    """
    number = min(20, number)

    nn_model, data = get_model_data()

    try:
        dist, indices = nn_model.kneighbors(data.ix[artist_name].values.reshape(1, -1), n_neighbors=number+1)
        results = []
        for i in range(1, len(dist.flatten())):
            artist_dict = dict()
            artist_dict['name'] = data.index[indices[0][i]]
            artist_dict['distance'] = dist.flatten()[i]
            results += [artist_dict]
    except KeyError:
        results = []
    return results


def get_model_data():
    model_cache_key = 'recommender_cache'
    nn_model = cache.get(model_cache_key)  # get model from cache

    data_cache_key = 'recommender_data_cache'
    data = cache.get(data_cache_key)

    if nn_model is None:
        # your model isn't in the cache
        # so `set` it
        model_path = os.path.join(BASE_DIR, "music_recommender/ml_model/nn_recommender.sav")
        nn_model = pickle.load(open(model_path, 'rb'))
        cache.set(model_cache_key, nn_model, None)  # save in the cache

    if data is None:
        data_path = os.path.join(BASE_DIR, "music_recommender/ml_model/wide_artist.csv")
        data = pd.read_csv(data_path).pivot(index='artist_name', columns='user_id',
                                            values='artist_total_plays').fillna(0)
        cache.set(data_cache_key, data, None)  # save in the cache

    return nn_model, data

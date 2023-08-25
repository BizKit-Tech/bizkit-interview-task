from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    searched_users = []

    if args:

        if 'id' in args:
            
            # if args has a parameter 'id'
            user_id = args['id']
            # iterate through USERS and get those that matches the 'id'
            user = next((user for user in USERS if user['id'] == user_id), None)
            searched_users.append(user)

        if 'name' in args:

            # use lower function since name parameters is case insensitive
            name_param = args['name'].lower()
            # add the searched users that matched the name parameters to the list
            searched_users.extend(user for user in USERS if name_param in user['name'].lower())

        if 'age' in args:

            # convert age to int since age is in string
            age = int(args['age'])
            # add the searched users that matched the user range to the list
            searched_users.extend(user for user in USERS if user['age'] >= age -1 and user['age'] <= age + 1)

        if 'occupation' in args:

            # user lower function since occupation parameter is case insensitive
            occupation_param = args['occupation'].lower()
            # add the searched users that matched the occupation parameter to the list
            searched_users.extend(user for user in USERS if occupation_param in user['occupation'].lower())

        return searched_users

def sort_search(args):

    searched_users = []

    # sort the result of the search based on key priority
    if args:
        searched_users.expand(sorted(USERS, key = lambda x: (x['id'], x['name'], x['age'], x['occupation'])))

    return searched_users
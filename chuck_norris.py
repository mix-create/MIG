import chucknorris.quips as q


def get_quip_for_name(name: str):
    return q.random(name)


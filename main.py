from graphviz import Digraph


class Node:

    def __init__(self, value=0, score=0, parent=None):
        self.value = value
        self.score = score
        self.parent = parent
        self.children = []

    def add_child(self, score):
        tmp_node = Node(score, self.score + score, self)
        self.children.append(tmp_node)

    def add_children(self):
        self.add_child(4)
        self.add_child(5)
        self.add_child(6)


def create_level(node: Node):

    if node.score < 21:
        node.add_children()

        for child in node.children:
            create_level(child)


def create_digraph(node: Node, dot: Digraph,):

    global node_id

    parent_label = str(node_id)
    dot.node(parent_label, str(node.score) + ' ' + str(node.value))
    node_id += 1

    for child in node.children:

        child_label = str(node_id)
        create_digraph(child, dot)
        dot.edge(parent_label, child_label)

        node_id += 1


def estimate_result(node: Node, current_max):

    if node.score > 21 and current_max is True:
        return -1
    elif node.score > 21 and current_max is False:
        return 1
    elif node.score == 21:
        return 0

    result_sum = 0

    for child in node.children:
        result_sum += estimate_result(child, not current_max)

    return result_sum


def min_max(node: Node, current_max=True):

    results = [estimate_result(child, current_max) for child in node.children]

    print(results)

    best_result = max(results) if current_max else min(results)
    best_coin = node.children[results.index(best_result)]

    best_coin_value = best_coin.value
    best_coin_score = best_coin.score

    player = 'Protagonist' if current_max else 'Enemy'

    print('{player_type} chooses {coin_value}'.format(player_type=player, coin_value=best_coin_value))
    print('Current stack:', best_coin_score)

    if best_coin_score == 21:
        print('Draw !')
    elif best_coin_score > 21:
        print(player, 'has lost!')
    else:
        min_max(best_coin, not current_max)


# task 1 - create game graph

root = Node()
create_level(root)

node_id = 0

graph = Digraph('gameRun')
create_digraph(root, graph)
graph.render('graph.gv', view=False)

# task 2 - implement min-max algorithm

min_max(root)

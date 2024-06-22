from os import PathLike
from pathlib import Path
from typing import List, Tuple, Callable, Iterator, Any, Dict

from IPython.core.display import HTML


class Printable:
    def show(self) -> HTML:
        raise NotImplementedError

    @staticmethod
    def _css() -> str:
        return '''
            <style type="text/css">
                .row {
                    display: flex;
                    flex-direction: row;
                }

                .node {
                    flex-grow: 1;
                    border: 2px solid black;
                }

                .node:not(:first-child) {
                    margin-left: 0.33rem;
                }

                .node:not(:last-child) {
                    margin-right: 0.33rem;
                }

                .node .title {
                    font-weight: bold;
                    border-bottom: 2px solid black;
                    padding: 0.33rem 0.67rem;
                }

                .node .content {
                    padding: 0.33rem 0.67rem;
                }
            </style>
        '''

    @staticmethod
    def _node(num: int, content: str):
        return f'''
            <div class="node">
                <div class="title">
                    Node{num}
                </div>
                <div class="content">
                    {content}
                </div>
            </div>
        '''


class MapReduce(Printable):
    def __init__(self, data: Dict[str, str], num_nodes: int = 4):
        # store properties
        self.num_nodes: int = num_nodes
        self.data: List[List[Tuple[str, str]]] = [[] for _ in range(num_nodes)]

        # read data
        node = 0

        for filename, text in data.items():
            self.data[node].append((filename, text))
            node = (node + 1) % num_nodes

    def show(self) -> HTML:
        html = f'{self._css()} <div class="row">'

        for node_num, node_data in enumerate(self.data, start=1):
            node_content = ''

            for title, text in node_data:
                node_content += f'''
                    <b>{title}</b>
                    <br>

                    <span>{text[:250].strip()} <i>[...]</i></span>
                    <br><br>
                '''

            html += self._node(node_num, node_content[:-25])

        html += '</div>'
        return HTML(html)

    def map(self, fun: Callable[[str, str], Iterator[Tuple[str, Any]]]) -> 'MapResult':
        return MapResult(self, fun)


class MapResult(Printable):
    def __init__(self, parent: MapReduce, fun: Callable[[str], Iterator[Tuple[str, Any]]]):
        self.root: MapReduce = parent
        self.fun: Callable[[str], Iterator[Tuple[str, Any]]] = fun

    def get(self, node: int) -> Iterator[Tuple[str, Any]]:
        for title, text in self.root.data[node]:
            for emit in self.fun(title, text):
                yield emit

    def show(self, max_items: int = 10) -> HTML:
        html = f'{self._css()} <div class="row">'

        for node_num, node_data in enumerate(self.root.data, start=1):
            node_content = ''

            for title, text in node_data:
                node_content += f'''
                    <b>{title}</b>
                    <br>
                '''

                i = 0
                for value in self.fun(title, text):
                    if i >= max_items:
                        node_content += '<i>[...]</i><br>'
                        break

                    node_content += f'<span>{value}</span><br>'
                    i += 1

                node_content += f'<br>'

            html += self._node(node_num, node_content[:-4])

        html += '</div>'
        return HTML(html)

    def shuffle(self) -> 'ShuffleResult':
        return ShuffleResult(self)


class ShuffleResult(Printable):
    def __init__(self, parent: MapResult):
        self.root: MapReduce = parent.root
        self.parent: MapResult = parent

    def get(self) -> Iterator[Tuple[int, Tuple[str, Any]]]:
        key_to_node: Dict[str, int] = {}
        last_used_node: int = 0

        for node_num in range(self.root.num_nodes):
            for key, value in self.parent.get(node_num):
                if key not in key_to_node:
                    key_to_node[key] = (last_used_node // 4096)
                    last_used_node = (last_used_node + 1) % (self.root.num_nodes * 4096)

                node = key_to_node[key]
                yield node, (key, value)

    def collect(self) -> Dict[int, List[Tuple[str, Any]]]:
        result: Dict[int, List[Tuple[str, Any]]] = {i: [] for i in range(self.root.num_nodes)}
        for node_num, value in self.get():
            result[node_num].append(value)

        for value in result.values():
            value.sort()

        return result

    def show(self, max_items: int = 20):
        html = f'{self._css()} <div class="row">'
        result = self.collect()

        for node_num in result:
            node_content = ''

            i = 0
            for value in result[node_num]:
                if i >= max_items:
                    node_content += '<i>[...]</i><br>'
                    break

                node_content += f'<span>{value}</span><br>'
                i += 1

            html += self._node(node_num + 1, node_content)

        html += '</div>'
        return HTML(html)

    def reduce(self, fun: Callable[[str, Iterator[Any]], Iterator[Tuple[str, Any]]]):
        return ReduceResult(self, fun)


class ReduceResult(Printable):
    def __init__(self, parent: ShuffleResult, fun: Callable[[str, Iterator[Any]], Iterator[Tuple[str, Any]]]):
        self.root: MapReduce = parent.root
        self.parent: ShuffleResult = parent
        self.fun: Callable[[str, Iterator[Any]], Iterator[Tuple[str, Any]]] = fun

    def get(self) -> Iterator[Tuple[int, Tuple[str, Any]]]:
        result = self.parent.collect()

        for node_num, node_result in result.items():
            first_iteration = True
            last_key = None
            values = []

            for key, value in node_result:
                if first_iteration:
                    last_key = key
                    first_iteration = False

                if key != last_key:
                    for yield_key, yield_value in self.fun(last_key, iter(values)):
                        yield node_num, (yield_key, yield_value)

                    last_key = key
                    values = []

                values.append(value)

            yield node_num, self.fun(last_key, iter(values))

    def collect(self) -> Dict[int, Tuple[str, Any]]:
        result = {i: [] for i in range(self.root.num_nodes)}
        for node_num, value in self.get():
            result[node_num].append(value)

        return result

    def show(self, max_items: int = 20):
        html = f'{self._css()} <div class="row">'
        result = self.collect()

        for node_num in result:
            node_content = ''

            i = 0
            for value in result[node_num]:
                if i >= max_items:
                    node_content += '<i>[...]</i><br>'
                    break

                node_content += f'<span>{value}</span><br>'
                i += 1

            html += self._node(node_num + 1, node_content)

        html += '</div>'
        return HTML(html)

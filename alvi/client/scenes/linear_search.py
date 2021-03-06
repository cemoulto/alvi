import random

import alvi.client.containers
import alvi.client.utils
from . import base


class LinearSearch(base.Scene):
    def generate_nodes(self, list, data_generator):
        if data_generator.quantity() == 0:
            return
        value = next(data_generator.values)
        list.create_head(value)
        node = list.head
        for value in data_generator.values:
            node = node.create_child(value)
        list.sync()

    def search(self, list, wanted_value):
        seeker = list.create_marker("seeker", list.head)
        list.sync()

        node = list.head
        found_index = 0
        while node:
            found_index += 1
            seeker.move(node)
            list.sync()
            if wanted_value == node.value:
                list.stats.found_index = found_index
                break
            node = node.next
        else:
            list.stats.not_found = ""
        list.sync()

    def run(self, **kwargs):
        list = kwargs['container']
        data_generator = kwargs['data_generator']
        #TODO add marker for wanted value
        wanted_value = random.randint(0, data_generator.quantity())
        list.stats.wanted_value = wanted_value

        self.generate_nodes(list, data_generator)
        self.search(list, wanted_value)

    @staticmethod
    def container_class():
        return alvi.client.containers.List


if __name__ == "__main__":
    LinearSearch.start()
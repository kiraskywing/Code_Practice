from random import randint

class LoadBalancer:
    def __init__(self):
        self.pos = {}
        self.ids = []

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        if server_id in self.pos:
            return
        self.ids.append(server_id)
        self.pos[server_id] = len(self.ids) - 1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        if server_id not in self.pos:
            return
        index = self.pos[server_id]
        self.ids[index], self.ids[-1] = self.ids[-1], self.ids[index]
        self.pos[self.ids[index]] = index
        del self.pos[server_id]
        self.ids.pop()

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        return self.ids[randint(0, len(self.ids) - 1)]

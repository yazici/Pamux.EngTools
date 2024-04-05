import logging
logger = logging.getLogger(__name__)

class NodePos:
    DeltaX = 400
    DeltaY = 300
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def goto_inputs(self):
        self.x = 0
        self.y = 0

    def goto_process(self):
        self.x = 3 * NodePos.DeltaX
        self.y = 0

    def goto_outputs(self):
        self.x = 10 * NodePos.DeltaX
        self.y = 0

    def dump(self, s):
        # logger.warning(f"{s}: {self.x} {self.y}")
        pass

CurrentNodePos = NodePos(0, 0)

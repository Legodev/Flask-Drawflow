from components.base.drawflownodebase import DrawflowNodeBase


class GoogleDriveSaveNode(DrawflowNodeBase):
    name = "Google Drive save"
    inputs = 1
    outputs = 0
    icon = 'fab fa-google-drive'
    node = 'google'
    nodehtml = """<div><div class="title-box"><i class="fab fa-google-drive"></i> Google Drive save </div></div>"""

    def getAsTuple(self):
        return (self.name, self.inputs, self.outputs, self.icon, self.node, self.nodehtml)

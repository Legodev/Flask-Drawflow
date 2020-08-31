from components.base.drawflownodebase import DrawflowNodeBase


class FileLogNode(DrawflowNodeBase):
    def __init__(self):
        self.name('log')
        self.title("File Log")
        self.input("filecontent", str)
        self.icon('fas fa-file-signature')
        self.nodehtml("""<div><div class="title-box"><i class="fas fa-file-signature"></i> Save log file </div></div>""")

from components.base.drawflownodebase import DrawflowNodeBase


class GoogleDriveSaveNode(DrawflowNodeBase):
    def __init__(self):
        super().__init__()

        self.name('google')
        self.title("Google Drive save")
        self.input("filecontent", str)
        self.icon('fab fa-google-drive')
        self.html("""<div><div class="title-box"><i class="fab fa-google-drive"></i> Google Drive save </div></div>""")

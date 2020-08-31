from components.base.drawflownodebase import DrawflowNodeBase


class EmailSendNode(DrawflowNodeBase):
    def __init__(self):
        self.name('email')
        self.title('Email send')
        self.input('msg', str)
        self.icon('fas fa-at')
        self.nodehtml("""<div><div class="title-box"><i class="fas fa-at"></i> Send Email </div></div>""")

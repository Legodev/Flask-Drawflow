from components.base.drawflownodebase import DrawflowNodeBase


class FacebookNode(DrawflowNodeBase):
    def __init__(self):
        self.name('facebook')
        self.title('Facebook')
        self.output('msg', str)
        self.icon('fab fa-facebook')
        self.nodehtml('<div><div class="title-box"><i class="fab fa-facebook"></i> Facebook Message</div></div>')

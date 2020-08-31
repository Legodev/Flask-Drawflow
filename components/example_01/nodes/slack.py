from components.base.drawflownodebase import DrawflowNodeBase


class SlackNode(DrawflowNodeBase):
    def __init__(self):
        self.name('slack')
        self.title('Slack recive message')
        self.input('msg', str)
        self.icon('fab fa-slack')
        self.nodehtml('<div><div class="title-box"><i class="fab fa-slack"></i> Slack chat message</div></div>')

from components.base.drawflownodebase import DrawflowNodeBase


class PersonalizedNode(DrawflowNodeBase):
    def __init__(self):
        self.name('personalized')
        self.title('Personalized')
        self.input('Input1', int)
        self.output('Output1', str)
        self.icon('fas fa-fill')
        self.nodehtml("""<div>Personalized</div>""")

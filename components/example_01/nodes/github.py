from components.base.drawflownodebase import DrawflowNodeBase


class GithubNode(DrawflowNodeBase):
    def __init__(self):
        super().__init__()

        self.name('github')
        self.title("Github Star")
        self.output('msg', str)
        self.icon('fab fa-github')
        self.html("""
              <div>
                <div class="title-box"><i class="fab fa-github "></i> Github Stars</div>
                <div class="box">
                  <p>Enter repository url</p>
                <input type="text" df-name>
                </div>
              </div>
              """)

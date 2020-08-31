from components.base.drawflownodebase import DrawflowNodeBase


class TelegramNode(DrawflowNodeBase):
    def __init__(self):
        super().__init__()

        self.name('telegram')
        self.title('Telegram send message')
        self.input('msg', str)
        self.icon('fab fa-telegram')
        self.html("""
              <div>
                <div class="title-box"><i class="fab fa-telegram-plane"></i> Telegram bot</div>
                <div class="box">
                  <p>Send to telegram</p>
                  <p>select channel</p>
                  <select df-channel>
                    <option value="channel_1">Channel 1</option>
                    <option value="channel_2">Channel 2</option>
                    <option value="channel_3">Channel 3</option>
                    <option value="channel_4">Channel 4</option>
                  </select>
                </div>
              </div>
              """)

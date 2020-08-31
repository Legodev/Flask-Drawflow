from components.base.drawflownodebase import DrawflowNodeBase


class TelegramNode(DrawflowNodeBase):
    name = "Telegram send message"
    inputs = 1
    outputs = 0
    icon = 'fab fa-telegram'
    node = 'telegram'
    nodehtml = """
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
          """

    def getAsTuple(self):
        return (self.name, self.inputs, self.outputs, self.icon, self.node, self.nodehtml)

class Session:
    def __init__(self, conv_id=None):
        self.conv_id = conv_id

    def get_conv_id(self):
        return self.conv_id

    def set_conv_id(self, conv_id):
        self.conv_id = conv_id

    def close(self):
        self.conv_id = None
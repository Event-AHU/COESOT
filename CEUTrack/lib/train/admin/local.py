class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/home/kraus/PycharmProjects/CEUTrack'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '/home/kraus/PycharmProjects/CEUTrack/tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = '/home/kraus/PycharmProjects/CEUTrack/pretrained_networks'
        self.coesot_dir = '/home/kraus/PycharmProjects/CEUTrack/data/coesot'
        self.coesot_val_dir = '/home/kraus/PycharmProjects/CEUTrack/data/coesot'
        self.fe240_dir = '/home/kraus/PycharmProjects/CEUTrack/data/fe240'
        self.fe240_val_dir = '/home/kraus/PycharmProjects/CEUTrack/data/fe240'
        self.visevent_dir = '/home/kraus/PycharmProjects/CEUTrack/data/visevent'
        self.visevent_val_dir = '/home/kraus/PycharmProjects/CEUTrack/data/visevent'

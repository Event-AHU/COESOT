class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/home/ioe/tcm/CEUTrack'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '/home/ioe/tcm/CEUTrack/tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = '/home/ioe/tcm/CEUTrack/pretrained_networks'
        self.coesot_dir = '/home/ioe/tcm/CEUTrack/data/COESOT/train'
        self.coesot_val_dir = '/home/ioe/tcm/CEUTrack/data/COESOT/test'
        self.fe108_dir = '/home/ioe/tcm/CEUTrack/data/FE108/train'
        self.fe108_val_dir = '/home/ioe/tcm/CEUTrack/data/FE108/test'
        self.visevent_dir = '/home/ioe/tcm/CEUTrack/data/VisEvent/train'
        self.visevent_val_dir = '/home/ioe/tcm/CEUTrack/data/VisEvent/test'

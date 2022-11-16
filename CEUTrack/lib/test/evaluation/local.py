from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.coesot_path = '/home/kraus/PycharmProjects/CEUTrack/data/COESOT'
    settings.fe240_path = '/home/kraus/PycharmProjects/CEUTrack/data/FE240'
    settings.network_path = '/home/kraus/PycharmProjects/CEUTrack/output/test/networks'    # Where tracking networks are stored.
    settings.prj_dir = '/home/kraus/PycharmProjects/CEUTrack'
    settings.result_plot_path = '/home/kraus/PycharmProjects/CEUTrack/output/test/result_plots'
    settings.results_path = '/home/kraus/PycharmProjects/CEUTrack/output/test/tracking_results'    # Where to store tracking results
    settings.save_dir = '/home/kraus/PycharmProjects/CEUTrack/output'
    settings.segmentation_path = '/home/kraus/PycharmProjects/CEUTrack/output/test/segmentation_results'
    settings.visevent_path = '/home/kraus/PycharmProjects/CEUTrack/data/VisEvent'

    return settings


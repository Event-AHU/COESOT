from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.coesot_path = '/home/ioe/tcm/CEUTrack/data/COESOT'
    settings.fe108_path = '/home/ioe/tcm/CEUTrack/data/FE108'
    settings.network_path = '/home/ioe/tcm/CEUTrack/output/test/networks'    # Where tracking networks are stored.
    settings.prj_dir = '/home/ioe/tcm/CEUTrack'
    settings.result_plot_path = '/home/ioe/tcm/CEUTrack/output/test/result_plots'
    settings.results_path = '/home/ioe/tcm/CEUTrack/output/test/tracking_results'    # Where to store tracking results
    settings.save_dir = '/home/ioe/tcm/CEUTrack/output'
    settings.segmentation_path = '/home/ioe/tcm/CEUTrack/output/test/segmentation_results'
    settings.visevent_path = '/home/ioe/tcm/CEUTrack/data/VisEvent'

    return settings


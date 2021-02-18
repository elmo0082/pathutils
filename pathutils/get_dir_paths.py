import getpass
import socket
import os

# CUDA_VISIBLE_DEVICES=4 python experiments/cremi/infer.py -- --inherit R1SD --update0 infer_config.yml --config.inference.index_output 1 --config.inference.threshold 0.5

def get_home_dir():
    username = getpass.getuser()
    hostname = socket.gethostname()

    if username == 'sdamrich_tmp':
        return '/home_sdc/sdamrich_tmp/'
    elif username == 'jgrieser_tmp':
	    return '/home_sdb/jgrieser_tmp/'
    else:
        raise ValueError("Home path not available for this machine and user")


def get_trendytukan_drive_dir():
    username = getpass.getuser()
    hostname = socket.gethostname()
    if hostname == 'trendytukan' and username == 'abailoni':
        return '/mnt/localdata0/abailoni/'
    elif hostname == 'trendytukan' and username == 'abailoni_local':
        return '/home/abailoni_local/trendyTukan_localdata0/'
    elif (hostname == 'ialgpu01' or hostname == 'birdperson' or hostname == 'sirherny') and (username == 'abailoni'):
        return '/home/abailoni/trendyTukan_drive/'
    elif username == 'abailoni_local' and hostname == 'fatchicken':
        return '/home/abailoni_local/trendyTukan_drive/'
    elif hostname == 'quadxeon5' and username == 'abailoni':
        return '/srv/scratch/abailoni/'
    elif hostname == 'sfb1129gpu02' and username == 'abailoni_tmp':
        return '/home_sdb/abailoni_tmp/trendyTukan_drive/'
    elif username == 'abailoni':
        return '/net/hcihome/storage/abailoni/trendyTukan_drive/'
    else:
        raise ValueError("Trendytukan local drive not available for this machine and user")


def get_list_source_dirs():
    username = getpass.getuser()
    if username in ['abailoni', 'abailoni_tmp', 'abailoni_local']:
        source_dirs = [
            # "python_libraries/nifty/python",
            "repositories/pathutils",
            "python_libraries/nifty/tmp/tmp.VVvldgIb9A/cmake-build-debug/python",
            "python_libraries/nifty/tmp/tmp.1DGbcigwoN/cmake-build-debug/python", # Affogato
            "python_libraries/cremi_python",
            "pyCharm_projects/inferno",
            # "pyCharm_projects/constrained_mst",
            # "pyCharm_projects/neuro-skunkworks",
            "pyCharm_projects/segmfriends",
            "pyCharm_projects/speedrun",
            "pyCharm_projects/neurofire",
            "pyCharm_projects/embeddingutils",
            "pyCharm_projects/firelight",
            "pyCharm_projects/ConfNets",
            "pyCharm_projects/GASP",
            "pyCharm_projects/latent_instance_masks",
        ]
        for i, dir in enumerate(source_dirs):
            source_dirs[i] = os.path.join(get_home_dir(), dir)
    else:
        raise ValueError("Source directories not available for this user")
    return source_dirs

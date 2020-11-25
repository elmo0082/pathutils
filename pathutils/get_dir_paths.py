import getpass
import socket
import os


def get_home_dir():
    username = getpass.getuser()
    hostname = socket.gethostname()
    if username == 'abailoni':
        if hostname == 'trendytukan':
            return '/net/hcihome/storage/abailoni/'
        elif hostname == 'ialgpu01' or hostname == 'birdperson' or hostname == 'sirherny':
            return '/home/abailoni/local_home/'
            # return '/home/abailoni/hci_home/'
        # elif hostname == 'sfb1129gpu01':
        #     return '/net/hcihome/storage/abailoni/ial_local_home/'
        elif hostname == 'quadxeon5':
            return '/srv/scratch/abailoni/'
        elif hostname == 'hgsgpu01':
            return '/srv/scratch/abailoni/'
        elif hostname == 'hgsgpu02':
            return '/srv/localscratch/abailoni/'
        # elif hostname == 'sfb1129gpu01':
        #     return '/net/hcihome/storage/abailoni/local_copy_home/'
        else:
            return '/net/hcihome/storage/abailoni/local_home/'
    elif hostname == 'trendytukan' and username == 'abailoni_local':
        # return '/home/abailoni_local/hci_home/'
        return '/home/abailoni_local/ialgpu1_local_home/'
    elif username == 'abailoni_local' and hostname == 'fatchicken':
        return '/home/abailoni_local/local_copy_home/'
    elif hostname == 'sfb1129gpu02' and username == 'abailoni_tmp':
        return '/home_sdb/abailoni_tmp/local_copy_home/'
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

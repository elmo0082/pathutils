# pathutils
Bunch of few path utils (get home directory for the current machine/user; automatically add your source directories to the python path)


### Creating a .pth config file 
- First, make sure to update the `pathutils/get_dir_paths.py` file with your paths and source dirs
- Run the `create_pth_fil.py` script using your current python environment
- Copy the config.pth file inside the `site-package` folder of your environment (that could look something like `~/anaconda3/envs/ENV_NAME/lib/python3.7/site-packages/`) and you are good to go. All your packages will be available 

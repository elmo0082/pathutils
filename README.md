# pathutils
Bunch of few path utils:
 - Get home and data directories for the current machine/user; 
 - Automatically add your source directories to the python path

### Usage for inferencing with Rasenna 

To be able to use the inferencing component, add 
```python
elif username == <usename>:
	   return </path/to/your/home>
```
to the file ```get_home_dir.py``` in the function named ```get_home_dir()```.

### Creating a .pth config file 
- First, make sure to update the `pathutils/get_dir_paths.py` file with your paths and source dirs
- Run the `create_pth_file.py` script on the machine you want to use
- Copy the config.pth file inside the `site-package` folder of your environment (that could look something like `~/anaconda3/envs/ENV_NAME/lib/python3.7/site-packages/`) and you are good to go. All your packages (including this one) will be available 

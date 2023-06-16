import os

#
# This is a user-modifiable Python file designed to be a set of simple input file and
# directory settings that you can choose and change.
#

# the location of the file containing AssetCollection id for the dtk sif (singularity image)
sif_id = os.path.join(os.pardir, 'dtk_sif.id')
# The script is going to use this to store the downloaded schema file.
# Create 'download' directory or change to your preferred (existing) location.
schema_file = "download/schema.json"
# The script is going to use this to store the downloaded Eradication binary.
# Create 'download' directory or change to your preferred (existing) location.
# eradication_path="download/Eradication"
eradication_path = "download/Eradication"
# Create 'Assets' directory or change to a path you prefer. idmtools will upload files found here.
assets_input_dir = "Assets"
plugins_folder = "download/reporter_plugins"

# path to pre- and post- processing scripts
ep4_path = "EP4"

job_directory = os.path.join(os.path.expanduser('~'), "example_emodpy_malaria/microsporidia")
os.makedirs(job_directory, exist_ok=True)
SIF_PATH = os.path.join(os.path.expanduser('~'), 'dtk_run_rocky_py39.sif')
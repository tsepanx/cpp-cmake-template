# cat post_gen_project.py
import os
import shutil

print(os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

add_rpm = '{{cookiecutter.add_rpm}}' == 'y'

if not add_rpm:
    # remove top-level file inside the generated folder
    remove('rpm')

# if not create_file_one:
#    # remove absolute path to file nested inside the generated folder
#    remove(os.path.join(os.getcwd(), '{{cookiecutter.package_name}}', 'file_one.py'))

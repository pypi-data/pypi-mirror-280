import shutil
import importlib_resources
from pathlib import Path

def import_quarto_template(qmd_filename:str = 'template.qmd', destination_dir:str=None):
  """
  Imports the brand themed qmd template into the working directory

  Args:
      qmd_filename (str, optional): The name of the qmd file to be imported alongside the template. Defaults to template.qmd
      destination_dir (str, optional): The directory to copy the template to. Defaults to the current working directory.

  Returns:
      None
  """
  package_name = f"{__package__}".split('.')[0]

  exclude_filenames = ['template.qmd']

  if qmd_filename[-4:] != '.qmd':
    qmd_filename = qmd_filename + '.qmd'
  
  # Use importlib_resources to get the absolute path of the resource directory
  resource_dir = importlib_resources.files(package_name).joinpath('template_files')

  # Determine the destination directory
  if destination_dir is None:
    destination_dir = Path.cwd()
  else:
    destination_dir = Path(destination_dir)

  #copy the template qmd file to the main directory
  if destination_dir.joinpath(qmd_filename).exists():
    print(f'A filename {qmd_filename} already exists and the blank qmd template will not be automatically copied.')
  else:
    shutil.copy2(resource_dir.joinpath('template.qmd'), destination_dir.joinpath(qmd_filename))
  
  #create directory to copy the template files to
  quarto_dir = destination_dir.joinpath('_extenstions/brandtemplate')

  if quarto_dir.exists() == False:
    quarto_dir.mkdir(parents=True)

  # Walk through the directory structure and copy files
  for src_file_path in resource_dir.glob('**/*'):
    if src_file_path.is_file() and src_file_path.name not in exclude_filenames:
      relative_path = src_file_path.relative_to(resource_dir)
      dest_file_path = quarto_dir.joinpath(relative_path)
      dest_file_path.parent.mkdir(parents=True, exist_ok=True)
      
      # Copy the file to the destination
      shutil.copy2(src_file_path, dest_file_path)


from .import_template import import_quarto_template

import argparse

def _cli_import_template():
  '''
  Function for running import_template via command line. 
  Use import_template instead if running from python.
  '''
  parser = argparse.ArgumentParser(description='Import the branded quarto template to your project.')

  parser.add_argument('-n', '--name', type=str, default='template.qmd', help='The name of the qmd file to create. Defaults to "template.qmd" if not specified.')
  parser.add_argument('-d', '--directory', type=str, default=None, help='The directory to import the template into. Defaults to the current directory if not specified.')

  args = parser.parse_args()

  import_quarto_template(qmd_filename=args.name, destination_dir=args.directory)


if __name__ == '__main__':
  _cli_import_template()
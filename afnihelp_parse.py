"""
Functions for generating boutiques descriptors from AFNI help
"""
from pathlib import Path
import re
from json import json

FINDARGS = re.compile("ARGS=\((.*) ?\)")


def get_complete_args(fname):
    """
    Attempts to find arguments for a given AFNI command

    Parameters
    ----------
    fname : str
        Path to "COMMAND.complete.bash" file generated by running
        `apsearch -update_all_afni_help`

    Returns
    -------
    args : list of str
        Putative arguments for command defined by `fname`
    """
    fpath = Path(fname).expanduser()
    if not fpath.exists():
        raise FileNotFoundError('{} does not seem to exist?'.format(fname))
    args = FINDARGS.findall(fpath.read_text())
    if len(args) < 1:
        raise ValueError('Unable to find arguments for {}'.format(fname))
    args = args[0].strip().replace('\'', '').split(' ')
    return args


def get_args_dict(help_dir,outfile='output.json'):
	tools = Path(help_dir).glob('*.complete.bash')
	args_dict = {}
	for tool in tools:
		in_args = get_complete_args(tool)
		tool_name = tool.as_posix().replace('.complete.bash','')
		args_dict[tool_name] = in_args
	with open(outfile) as dest: json.dump(args_dict,dest)


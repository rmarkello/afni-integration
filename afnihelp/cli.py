"""
Functions for generating parsed AFNI help JSONs from CLI
"""
import argparse
from pathlib import Path
from afnihelp.parsing import gen_boutify_jsons, gen_boutique_descriptors


def _get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('help_dir', type=Path, metavar='help_directory',
                        help='Path to AFNI help directory, as generated by '
                             '`apsearch -update_all_afni_help`.')
    parser.add_argument('-o', '--out', type=Path, metavar='PATH',
                        dest='outdir', required=True,
                        help='Path to where generated JSON files should be '
                             'saved.')
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        help='Whether to print status updates.')

    return parser


def boutify(argv=None):
    options = _get_parser().parse_args(args=argv)
    gen_boutify_jsons(**vars(options))


def descriptify(argv=None):
    options = _get_parser().parse_args(args=argv)
    gen_boutique_descriptors(**vars(options))
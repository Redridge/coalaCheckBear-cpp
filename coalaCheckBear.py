import os

from coalib.bearlib.abstractions.ExternalBearWrap import external_bear_wrap


@external_bear_wrap(executable='coalaCheck_cpp',
                    settings={})
class coalaCheckBear:
    """
    Checks for coala written with uppercase 'C'
    """
    LANGUAGES = {'All'}
    REQUIREMENTS = {'coalaCheck_cpp'}
    AUTHORS = {'Redridge'}
    AUTHORS_EMAILS = {'alexandros.dimos.95@gmail.com'}
    LICENSE = 'GPLv3'

    @staticmethod
    def create_arguments():
        return ()

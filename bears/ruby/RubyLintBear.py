import re

from coalib.bearlib.abstractions.Lint import Lint
from coalib.bears.LocalBear import LocalBear
from coalib.results.RESULT_SEVERITY import RESULT_SEVERITY


class RubyLintBear(LocalBear, Lint):
    executable = 'ruby'
    arguments = '-S ruby-lint {filename}'
    prerequisite_command = ['ruby-lint']
    prerequisite_fail_msg = "Please install ruby-lint for this bear to work"
    output_regex = re.compile(r'(?P<file_name>.*rb):\s*'
                              r'(?P<severity>error|warning):\s*'
                              r'line\s*(?P<line>\d+),\s*column\s*'
                              r'(?P<column>\d+):\s*'
                              r'(?P<message>.*)')
    severity_map = {
        "warning": RESULT_SEVERITY.NORMAL,
        "error": RESULT_SEVERITY.MAJOR}

    def run(self, filename, file):
        '''
        Checks the code with `ruby-lint` on each file separately.
        '''
        return self.lint(filename)

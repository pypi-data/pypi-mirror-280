# This code is part of vulqano.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.


import os
import os.path
import unittest
from io import StringIO
import pylint.lint
from pylint.reporters.text import ParseableTextReporter


class TestPylint(unittest.TestCase):
    """
    Run pylint to check syntax in source files.

    **Details**

    We disable globally:

    * C0325: superfluous parenthesis
    * C0209: consider using fstring
    * C3001: Lambda expression assigned to a variable
    * W1514: unspecified encoding
    * R1711: useless returns (for allowing empty iterators with
      return-yield)
    * Skip Unused argument errors when args
    * Skip Unused argument errors when kargs
    """

    def setUp(self):
        """
        Provide the test setup.
        """
        self.pylint_args = {
            "good-names": "ii,jj,kk,nn,mm,fh,dx,dy,dz,dt,op",
            "disable": "C0325,C0209,W1514,R1711,C3001",
        }

    def run_pylint(self, filename, local_settings={}):
        """
        Run linter test with our unit test settings for one specific
        filename.
        """
        args = []

        ignore_in_line = []
        if "ignore_in_line" in local_settings:
            ignore_in_line = local_settings["ignore_in_line"]
            del local_settings["ignore_in_line"]

        for elem in self.pylint_args.keys():
            args += ["--" + elem + "=" + self.pylint_args[elem]]

            if elem in local_settings:
                args[-1] = args[-1] + "," + local_settings[elem]
                del local_settings[elem]

        for elem in local_settings.keys():
            args += ["--" + elem + "=" + local_settings[elem]]

        args += [filename]

        obj = StringIO()
        reporter = pylint.reporters.text.ParseableTextReporter(obj)
        pylint.lint.Run(args, reporter=reporter, exit=False)

        error_list = []
        for elem in obj.getvalue().split("\n"):
            tmp = elem.replace("\n", "")

            if len(tmp) == 0:
                continue
            if tmp.startswith("***"):
                continue
            if tmp.startswith("---"):
                continue
            if tmp.startswith("Your code"):
                continue
            if "Unused argument 'args'" in tmp:
                continue
            if "Unused argument 'kwargs'" in tmp:
                continue

            do_continue = False
            for pattern in ignore_in_line:
                if pattern in tmp:
                    do_continue = True

            if do_continue:
                continue

            error_list.append(tmp)

        return error_list

    def test_folders_recursively(self):
        """
        Recursively run python linter test on all .py files of
        specified folders.
        """
        parent_folders = ["vulqano"]
        skip_files = []
        error_list = []

        for elem in parent_folders:
            for root, dirnames, filenames in os.walk(elem):
                for filename in filenames:
                    if not filename.endswith(".py"):
                        continue

                    if filename in skip_files:
                        continue

                    target_file = os.path.join(root, filename)

                    target_attr = "get_settings_" + filename.replace(".py", "")
                    if hasattr(self, target_attr):
                        target_setting = self.__getattribute__(target_attr)()
                    else:
                        target_setting = {}

                    error_list_ii = self.run_pylint(
                        target_file, local_settings=target_setting
                    )

                    error_list += error_list_ii

        self.assertEqual(len(error_list), 0, "\n".join(error_list))

    # --------------------------------------------------------------------------
    #                          Settings for vulqano
    # --------------------------------------------------------------------------

    def get_settings_utils(self):
        """
        Linter for module ``utils.py``.

        **Details**

        We locally ignore:

        * R0911: Ttoo many return statements.
        """
        local_settings = {
            "disable": "R0911",
        }
        return local_settings

    def get_settings_compiler(self):
        """
        Linter for module ``compiler.py``.

        **Details**

        We locally ignore:

        * R0913: Too many arguments.
        """
        local_settings = {
            "disable": "R0913",
        }
        return local_settings

    def get_settings_quantumdynamics(self):
        """
        Linter for module ``quantumdynamics.py``.

        **Details**

        We locally ignore:

        * R0912: Too many branches.
        * R0913: Too many arguments.
        * R0914: Too many locals.
        * R0915: Too many statements.
        """
        local_settings = {
            "disable": "R0912,R0913,R0914,R0915",
        }
        return local_settings

    def get_settings_quantummodel(self):
        """
        Linter for module ``quantummodel.py``.

        **Details**

        We locally ignore:
        """
        pattern_1 = "Unused argument 'parameters'"
        local_settings = {
            "ignore_in_line": [pattern_1],
        }
        return local_settings

    def get_settings_collapsedquantummodel(self):
        """
        Linter for module ``collapsedquantummodel.py``.

        **Details**

        We locally ignore:
        * R0913: Too many arguments.
        * C0301: Line too long.
        """
        pattern_1 = "Unused argument 'parameters'"
        local_settings = {
            "disable": "R0913,C0301",
            "ignore_in_line": [pattern_1],
        }
        return local_settings

    def get_settings_mcmc(self):
        """
        Linter for module ``mcmc.py``.

        **Details**

        We locally ignore:

        * R0913: Too many arguments.
        """
        local_settings = {
            "disable": "R0913",
        }
        return local_settings

    def get_settings_markoviandynamics(self):
        """
        Linter for module ``markoviandynamics.py``.

        **Details**

        We locally ignore:

        * R0912: Too many branches.
        * R0913: Too many arguments.
        * R0914: Too many locals.
        * R0915: Too many statements.

        """
        pattern_1 = "Unused argument 'step'"
        local_settings = {
            "disable": "R0912,R0913,R0914,R0915",
            "ignore_in_line": [pattern_1],
        }
        return local_settings

    def get_settings_localquantumops(self):
        """
        Linter for module ``localquantumops.py``.

        **Details**

        We locally ignore:

        * R0903: Too few public methods.
        * W0231: Super init not called.
        """
        local_settings = {
            "disable": "R0903,W0231",
        }
        return local_settings

    def get_settings_standardcontinuousrules(self):
        """
        Linter for module ``standardcontinuousrules.py``.

        **Details**

        We locally ignore:

        * C0302: Too many lines.
        * E0102: Function redefined.
        * R0915: Too many statements.
        * W0640: Cell variable defined in loop.
        * W0108: Unnecessary lambda.
        """
        local_settings = {
            "disable": "C0302,E0102,R0915,W0108,W0640",
        }
        return local_settings

    def get_settings_abstractcontinuousrules(self):
        """
        Linter for module ``abstractcontinuousrules.py``.

        **Details**

        We locally ignore:

        * R0902: Too many instance attributes.
        * R0913: Too many arguments.
        """
        local_settings = {
            "disable": "R0902,R0913",
        }
        return local_settings

    def get_settings_mcrules(self):
        """
        Linter for module ``mcrules.py``.

        **Details**

        We locally ignore:

        * R0903: Too few public methods.
        """
        local_settings = {
            "disable": "R0903",
        }
        return local_settings

    def get_settings_abstractcircuitstate(self):
        """
        Linter for module ``abstractcircuitstate.py``.

        **Details**

        We locally ignore:

        * R0902: Too many instance attributes.
        * R0912: Too many branches.
        * R0914: Too many locals.
        * R0915: Too many statements.

        """
        local_settings = {
            "disable": "R0902,R0912,R0914,R0915",
        }
        return local_settings

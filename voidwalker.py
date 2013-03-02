# (void)walker GDB plugin
# Copyright (C) 2012 David Holm <dholmster@gmail.com>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import inspect
import os.path
import sys

from flowui.terminal import AnsiTerminal
from flowui.themes import Solarized

voidwalker_path = os.path.abspath(inspect.getfile(inspect.currentframe()))
sys.path.append(os.path.dirname(voidwalker_path))


# Load GDB backend
from backends.gdb import *

# Register all commands, parameters, cpus and themes
from application import *
from application.patching import *
from backends.gdb.tools import *

from framework.interface import CommandBuilder
from framework.interface import Configuration
from framework.interface import ParameterBuilder
from framework.platform import CpuFactory
from framework.target import InferiorManager
from framework.target import TargetFactory

from backends.gdb import ConvenienceManager
from backends.gdb import GdbCommandFactory
from backends.gdb import GdbParameterFactory
from backends.gdb import GdbTerminal

version = '0.0.0'

config = Configuration()
ParameterBuilder(GdbParameterFactory(), config)

ansi_terminal = AnsiTerminal(GdbTerminal(), Solarized())
CommandBuilder(GdbCommandFactory(), config, ansi_terminal)

TargetFactory().init(CpuFactory())
InferiorManager().init()
ConvenienceManager().init()

ansi_terminal.write(('%(face-underlined)s(void)walker%(face-normal)s '
                     'v%(version)s installed\n'),
                    {'version': version})

# (void)walker unit tests
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

from unittest import TestCase

from ui.solarized import Solarized
from ui.terminal import SysTerminal
from ui.theme import ThemeManager
from ui.zenburn import Zenburn


class TestTheme(object):
    def tearDown(self):
        reset = self.theme().property('normal')
        self.terminal().write('%s\n' % reset)

    def theme(self):
        raise NotImplementedError()

    def terminal(self):
        raise NotImplementedError()

    def test_faces(self):
        reset = self.theme().property('normal')
        self.terminal().write('\n')
        for name, face in self.theme().faces().iteritems():
            self.terminal().write(self.theme().write('\t%s[%s]%s\n' %
                                                     (face, name, reset)))


class TestSolarized(TestTheme, TestCase):
    _theme = ThemeManager().theme(Solarized.name())
    _terminal = SysTerminal(_theme)

    def theme(self):
        return self._terminal.theme()

    def terminal(self):
        return self._terminal


class TestZenburn(TestTheme, TestCase):
    _theme = ThemeManager().theme(Zenburn.name())
    _terminal = SysTerminal(_theme)

    def theme(self):
        return self._terminal.theme()

    def terminal(self):
        return self._terminal
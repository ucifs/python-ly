# This file is part of python-ly, https://pypi.python.org/pypi/python-ly
#
# Copyright (c) 2008 - 2014 by Wilbert Berendsen
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# See http://www.gnu.org/licenses/ for more information.

"""
MusicXML functionality.
"""

from __future__ import unicode_literals

def writer():
    """Convert LilyPond text to MusicXML

    Example:

    import ly.musicxml

    e = ly.musicxml.writer()
    e.parse_text(lilypond_text) # or: e.parse_tokens(tokens)
    xml = e.musicxml()

    xml.write(filename)         # or: xml.tostring()

    # xml.tree is the ElementTree xml tree.

    """
    #from . import source2musxml
    #return source2musxml.parse_source()

    """
    new parser using ly.music
    Under development!

    """

    from . import lymus2musxml
    return lymus2musxml.ParseSource()



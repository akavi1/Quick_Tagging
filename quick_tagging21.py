# Quick Tagging is an anki2.1 addon for quickly adding tags while reviewing
# Copyright 2012 Cayenne Boyer
# Copyright 2018 Arthur Milchior
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from aqt import mw
from aqt.utils import getTag, tooltip
from aqt.reviewer import Reviewer
from .config import *

def debug(t):
    #print(t)
    pass
# add space separated tags to a note

def addTags(note, tagString):
    #debug(f"Call addTags({note},{tagString})")
    # add tags to card
    tagList = mw.col.tags.split(tagString)
    for tag in tagList:
        note.addTag(tag)
    note.flush()

# prompt for tags and add the results to a note
def promptAndAddTags():
    # prompt for new tags
    #debug(f"Call promptAndAddTags()")
    mw.checkpoint(_("Add Tags"))
    note = mw.reviewer.card.note()
    prompt = _("Enter tags to add:")
    (tagString, r) = getTag(mw, mw.col, prompt)
    # don't do anything if we didn't get anything
    if not r:
        return
    # otherwise, add the given tags:
    addTags(note, tagString)
    tooltip('Added tag(s) "%s"' % tagString)

def quick_tag_method(map):
  #debug(f"Call quick_tag_method({map})")
  def r():
    #debug(f"Call function defined thanks to ({map})")
    card = mw.reviewer.card
    note = card.note()
    if 'bury' in map and map['bury']:#old config. May eventually be removed.
        map['action']='bury note'
        del map['bury']
        updateConfig()
    action = map.get('action',"")
    checkSuffix = {
        "bury card":" and Bury Card",
        "bury note":" and Bury Note",
        "suspend card":" and Suspend Card",
    }.get(action,"")
    mw.checkpoint("Add Tags"+checkSuffix)
    addTags(note, map['tags'])
    if action == "bury card":
        mw.col.sched.buryCards([card.id])
    elif action == "bury note":
        mw.col.sched.buryNote(note.id)
    elif action == "suspend card":
        mw.col.sched.suspendCards([card.id])
    if action:
        mw.reset()
    tooltipSuffix = {
        "bury card":" and buried card",
        "bury note":" and buried note",
        "suspend card":" and suspended card",
    }.get(action,"")
    tooltip(f'Added tag(s) "%s"{tooltipSuffix}'
                % map['tags'])
  return r

def new_shortcutKeys():
    tag_shortcut = getConfig().get("tag shortcut","t")
    quick_tags = getConfig().get("quick tags",dict()) # end quick_tags
    sk=[(tag_shortcut, promptAndAddTags)]
    for key,map in quick_tags.items():
        #debug(f"{key}:{map}")
        sk.append((key,quick_tag_method(map)))
    #debug(f"new_shortcutKeys(), returning {sk}")
    return sk

old_shortcutKeys = Reviewer._shortcutKeys
def _shortcutKeys(self):
    shortcutKeys = old_shortcutKeys(self)+new_shortcutKeys()
    #debug(f"new_shortcutKeys(), returning {shortcutKeys}")
    return shortcutKeys
Reviewer._shortcutKeys=_shortcutKeys

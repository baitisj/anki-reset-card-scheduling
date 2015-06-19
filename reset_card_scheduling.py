# -*- coding: utf-8 -*-
# Copyright: Jeffrey Baitis <jeff@baitis.net>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

import os
from anki.hooks import addHook
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QAction

# import the main window object (mw) from ankiqt
from aqt import mw
from aqt.utils import showInfo
from aqt import browser

# Col is a collection of cards, cids are the ids of the cards to reset.
def resetSelectedCardScheduling(self):
	""" Resets statistics for selected cards, and removes them from learning queues. """
	cids = self.selectedCards()
	if not cids:
		return
	# Allow undo
	self.mw.checkpoint(_("Reset scheduling and learning on selected cards"))
	self.mw.progress.start(immediate=True)
	# Not sure if beginReset is required
	self.model.beginReset()

	# Resets selected cards in current collection
	self.col.sched.resetCards(cids)
	# Removes card from dynamic deck?
	# self.col.sched.remFromDyn(cids)
	# Removes card from learning queues
	self.col.sched.removeLrn(cids)
	self.model.endReset()
	self.mw.progress.finish()
	# Update the main UI window to reflect changes in card status
	self.mw.reset()

def addMenuItem(self):
	""" Adds hook to the Edit menu in the note browser """
	action = QAction("Reset scheduling and learning on selected cards", self)
	self.resetSelectedCardScheduling = resetSelectedCardScheduling
	self.connect(action, SIGNAL("triggered()"), lambda s=self: resetSelectedCardScheduling(self))
	self.form.menuEdit.addAction(action)

# Add-in hook; called by the AQT Browser object when it is ready for the add-on to modify the menus
addHook('browser.setupMenus', addMenuItem)

# TODO: Eventually, this add-on should be able to be invoked from the deck browser
# addHook('deckbrowser.setupOptions', addOptionsItem)

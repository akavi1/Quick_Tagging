* tag shortcut: key which, when pressed during review, will open the tag adder.
* quick tags: a dictionnary which associate to a key(shortcut) a set of actions to do. One such action consists of a dictionnary. This dictionnary may have the following keys:
  * `tags`: the tag or tags which will be added to the note. (add " marked " to this string to ensure the card become marked)
  * `action`: what to do to the card/note. The possible values may be:
    *  `bury note`: whether pressing this button will bury the card.
    * `bury card`: whether pressing this button will bury the note.
    * `suspend`: whether pressing this button will suspend the note.

For example `'l': {'tags': 'hard marked', 'action': 'bury card'}` state that, when you press "l", the card is baried add the tags 'hard' and 'marked' are added to it. However, the card is not suspended.

If you're already in the review mode, you won't be able to use the new configurations until you leave this mode and goes back to it.
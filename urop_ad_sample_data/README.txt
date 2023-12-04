We've provided two csv files with the raw interaction data for two switch-users that trialed Nomon. Each user copied multiple target phrases using the Nomon keyboard. Each row represents a single click sent into the Nomon Keyboard. The columns in the dataset are described below:

Phrase Num — Index of the click’s phrase that the user was typing.

Selection Num — Index of the click’s selection towards typing the current phrase.

Click Num — Index of the current switch press needed to make the current selection.

Phrase Text -- The target phrase presented to the user.

Typed Text — The text currently typed by the user on a given phrase. Note this may difer from the phrase text if the user made an error.

Click Time Relative (s) — The time that the user clicked their switch minus the time at which the clock they ultimately selected was at Noon, modulo the Clock Period. The time is recorded in seconds and takes values within [−Clock Period/2, Clock Period/2].

Click Time Absolute (s) — The global timestamp measured in seconds since epoch (Unix time) that the user clicked their switch.

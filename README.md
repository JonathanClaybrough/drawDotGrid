# drawDotGrid
A simple python script to generate a grid of dot grids (useful to print to play The Nature Game)

The Nature Game
This is a Rule deduction game. One player will play the rule of "Nature", they will choose a particular
rule which marks some geometric figures as valid, and others as invalid. The other players submit different
figures trying to understand the pattern, and can submit a rule once they think they found it.

The game is played using squares of 5 by 5 grid of dots, drawing any set of horizontal or vertial lines connecting
those dots. There are thus 2^40 possible states of the grid of dots. Nature chooses a rule, like "there should be 
as many vertical or horizontal lines" or "there should be a continous line connecting opposite sides of the board". 
It is more elegant that it can be calculated quickly, expressed simply, yet has both many positive and negative
examples. To start the game, Nature provides one example of a board which verifies the rule, and one which doesn't.
Nature keeps track of two areas, the "verifies" and "doesn't verify" areas.

The players all get stacks of empty grids and pens to draw examples, submit them to Nature, who puts them in the correct pile.
Players can suggest a rule when they want, but cannot suggest for 30 seconds when they get it wrong. When they get it wrong, 
Nature must provide an example of a grid which disproves the player's suggestion. First to find correct rule wins.

Competitive multiplayer variants : 
Every player (except nature) gets 3 tokens, which are their "hidden experiment" tokens. 
When they submit a grid, they submit it face down with their token on it. Nature evaluates the grid, marks it (with a cross
or check) as correct or incorrect, then gives it face down to the corresponding player. A player can thus have 3 hidden
experiments they don't show to others. If they want to submit more grids, they must free up a token by revealing a grid
and putting it in the correct area. 
When a player attempts to guess a rule to Nature, they must give up a token. If they have no more tokens, they can still
attempt to guess a rule but with the 30 second penalty time between suggestions. 

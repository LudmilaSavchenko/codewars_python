"""
Likes Vs Dislikes

Story

YouTube had a like and a dislike button, which allowed users to express their opinions about particular content. It was set up in such a way that you cannot like and dislike a video at the same time. There are two other interesting rules to be noted about the interface: Pressing a button, which is already active, will undo your press. If you press the like button after pressing the dislike button, the like button overwrites the previous "Dislike" state. The same is true for the other way round.

Task

Create a function that takes in a list of button inputs and returns the final state.

Examples

like_or_dislike([Dislike]) ➞ Dislike
like_or_dislike([Like, Like]) ➞ Nothing
like_or_dislike([Dislike, Like]) ➞ Like
like_or_dislike([Like, Dislike, Dislike]) ➞ Nothing
Notes

If no button is currently active, return Nothing.
If the list is empty, return Nothing.
"""

"""
#var 1
def like_or_dislike(lst):
    result = "Nothing"
    for i in lst:
        if result == "Nothing":
            result = i
        elif result == "Like":
            result = "Nothing" if i == "Like" else "Dislike"
        elif result == "Dislike":
            result = "Nothing" if i == "Dislike" else "Like"
    return result

"""

def like_or_dislike(lst):
    state = 'Nothing'
    for i in lst:
        state = 'Nothing' if i == state else i
    return state


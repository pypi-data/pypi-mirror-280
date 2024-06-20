"""

"""

def ds_to_os(durs, init_beat=0):
    """Returns a list of (accumulated onset, corresponding duration).
    The initial onset is the desired starting onset."""
    durs = list(durs) # convert to pop
    onsets = []
    while durs:
        onsets.append(init_beat)
        init_beat += durs.pop(0)
    return onsets


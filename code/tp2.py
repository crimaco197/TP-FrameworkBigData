#! /usr/bin/python
with open("forum_node.tsv", "r") as _in:
    with open("clean_forum.tsv", "w") as _out:
        for l in _in.readlines(): 
            if len(l.strip()) == 0: 
                _out.write(l.strip())
            else:
                # Check if at the end of the line we have \r\n
                if len(l) > 1 and l[-2] == "\r":
                    # End of the line
                    _out.write(l.strip() + "\n")
                else:
                    # Line not ended
                    _out.write(l.strip())
 
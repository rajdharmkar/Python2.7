try:
    def foo():
        z=['zo','si']
        for s in z:
        s=='zo'
    raise IndentationError

except IndentationError as e:
       print e.args


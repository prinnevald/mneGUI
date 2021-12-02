class RedirectText(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, text_ctrl):
        """Constructor"""
        self.text = text_ctrl
 
    #----------------------------------------------------------------------
    def write(self, string):
        """"""
        self.text.insert("\r", string)
import os,sys

class CpaException(Exception):

    """
    CpaException is customized exception designed to capture refined details about exception
    such as python script file line number along with error message
    With custom exception one can easily spot source of error and provide quick fix.
    
    """
    def __init__(self, error_message :Exception, error_detail:sys):
        """
        : param error_message: error message in string format
        """
        super().__init__(error_message)
        self.error_message = CpaException.error_message_detail(error_message,error_detail=error_detail)

    @staticmethod
    def error_message_detail(error:Exception,error_detail:sys):
        """
        error : Exception object raise from module
        error_detail: in sys module contain detail information about system execution information
        
        """

        _,_,exc_tb = error_detail.exc_info()

        # extracting file name from exception traceback
        file_name = exc_tb.tb_frame.f_code.co_filename

        # preparing error message

        error_message = f"Error Occurred python script name [{file_name}]"\
                        f"Line Number [{exc_tb.tb_lineno}] error message [{error}]."

        return error_message
    
    def __repr__(self):

        """
        formating object of CpaException
        """
        return CpaException.__name__.__str__()

    def __str__(self):
        """
        Formating how a object should be visible if used in print statement
        """
        return self.error_message


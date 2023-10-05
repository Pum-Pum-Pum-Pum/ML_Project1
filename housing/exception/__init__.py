import os
import sys

class HousingException(Exception):

    def __init__(self, error_message:Exception, error_detail:sys):
        super().__init__(error_message)
        self.error_message = HousingException.get_detailed_Error_message(error_message=error_message, error_detail=error_detail)
        
    @staticmethod
    def get_detailed_Error_message(error_message:Exception, error_detail:sys)->str:
        _,_,exec_tb     = error_detail.exc_info() #_ _ is used as exc_info returns 3 values, first two is not required.
        line_number     = exec_tb.tb_frame.f_lineno # pre-defined line number
        file_name       = exec_tb.tb_frame.f_code.co_filename
        error_message   = f"Error occured in file: [{file_name}] at line number : [{line_number}] error message: [{error_message}]"
        return error_message
    
    # __str__ is called as dunder method, when we print the object of any class, what info will be displayed that is defined in __str__
    def __str__(self):
        return self.error_message
    
    def __repr__(self) -> str:
        return HousingException.__name__.str()
        
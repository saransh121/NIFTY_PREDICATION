import sys



def error_message_details(error,error_details:sys):
    #error_details:sys , here : sys , says that the error_details variable will a type of sys
    # : is also known as hint
    _,_,exc_tab = error_details.exc_info()
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        exc_tab.tb_frame.f_code.co_filename , exc_tab.tb_lineno , error
    )
    return error_message

class customeException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__()
        self.error_message = error_message_details(error_message,error_details)
    def __str__(self):
        return self.error_message
    
# if __name__ == '__main__':
    
#     try:
#         a = 1/0
#     except Exception as e:
#         customeException_ = customeException(e.__str__(),error_details=sys)
#         logging.info('divided error'+customeException_.__str__())
#         # raise customeException_

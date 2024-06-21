from typing import Callable, Any, Iterable


def _input_with_validation(input_txt: str, validation_func: Callable[[str], Any], error_text: str = None):
    
    val = None
        
    while val is None:
        try:
            val = validation_func(input(input_txt))
            break
        except ValueError:
            val = None
            
        print(error_text or "This is not a valid input")
        
    return val
    
    
def input_int(input_text: str):
    return _input_with_validation(input_text, int)
    
    
def input_float(input_text: str):
    return _input_with_validation(input_text, float)
    

def input_option(input_text: str, options_list: Iterable[Any]):
    options_dict = {str(option): option for option in options_list}
    assert len(options_dict) == len(options_list)
    def validation_func(input_text):
        if input_text not in options_dict:
            raise ValueError("Invalid option")
        return options_dict[input_text]
        
    if len(options_list) <= 10:
        error_text = f"Invalid option, valid options are [{', '.join(options_dict.keys())}]"
    else:
        error_text = None
        
    return _input_with_validation(input_text, validation_func, error_text)
import module_razional as model
import view
import logger

def button_click():
    value_a = view.get_value()
    math_char = view.get_math_char()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.do_it(math_char)
    logger.log_operations(f'{value_a} {math_char} {value_b} = {result}')
    view.view_data(result)
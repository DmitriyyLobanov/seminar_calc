import module_razional as model
import view

def button_click():
    value_a = view.get_value()

    math_char = view.get_math_char()

    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.razi_mult()
    view.view_data(result)
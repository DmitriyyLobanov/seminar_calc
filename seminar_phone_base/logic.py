import ui_console as ui
import logger
import assigment_id as id

def use_phone_base():
    mode = ui.get_mode()
    if mode == "1":
        entry_user = ui.get_user_info()
        entry_user = id.assign_id(entry_user)
        logger.log_json(entry_user)
        logger.log_xml(entry_user)
    elif mode == "2":
        ui.find_user()



from src.helpers.buttons_dict import btn_dict
from src.service.calculator import Calc


if __name__ == "__main__":
    with Calc() as calc:
        calc.process_btn(btn_img=btn_dict['1'])
        calc.process_btn(btn_img=btn_dict['2'])
        calc.process_btn(btn_img=btn_dict['+'])
        calc.process_btn(btn_img=btn_dict['7'])
        calc.process_btn(btn_img=btn_dict['='])
        calc.get_result()



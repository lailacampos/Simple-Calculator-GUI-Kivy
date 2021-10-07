# Useful links:
# https://www.youtube.com/watch?v=Lu-HP4eOYM4&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=15&ab_channel=Codemy.com

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

# Set app size
Window.size = (500, 700)


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"

    def press_button(self, button_value):
        input_value = self.ids.calc_input.text

        if "Error" in input_value:
            self.ids.calc_input.text = ''

        if input_value == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button_value}"
        else:
            self.ids.calc_input.text += f"{button_value}"

    def math_sign(self, operator):
        input_value = self.ids.calc_input.text

        if operator in input_value:
            pass
        else:
            self.ids.calc_input.text = f'{input_value}{operator}'

    def add_dot(self):
        input_value = self.ids.calc_input.text
        num_list = input_value.split("+")

        # num_list[-1] = Last item in the list
        if "+" in input_value and "." not in num_list[-1]:
            input_value = f'{input_value}.'
            self.ids.calc_input.text = input_value

        elif "." in input_value:
            pass
        else:
            input_value = f'{input_value}.'
            self.ids.calc_input.text = input_value

    # Remove last character in text input
    def remove(self):
        input_value = self.ids.calc_input.text
        input_value = input_value[:-1]
        self.ids.calc_input.text = input_value

    def change_negative_positive(self):
        input_value = self.ids.calc_input.text

        if "-" in input_value:
            self.ids.calc_input.text = f'{input_value.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{input_value}'

    def equals(self):
        input_value = self.ids.calc_input.text

        try:
            answer = eval(input_value)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"

        # Addition
        # Check if plus sign in input
        # if "+" in input_value:
        #     num_list = input_value.split("+")
        #
        #     answer = 0.0
        #
        #     for number in num_list:
        #         # if number.isnumeric():
        #         answer = answer + float(number)

        # elif "-" in input_value:
        #     num_list = input_value.split("-")
        #
        #     answer = 0
        #
        #     for index, number in enumerate(num_list):
        #         if number.isnumeric():
        #             answer -= int(number)
        #
        # elif "*" in input_value:
        #     num_list = input_value.split("*")
        #
        #     answer = 0
        #
        #     for number in num_list:
        #         if number.isnumeric():
        #             answer *= int(number)
        #
        # elif "/" in input_value:
        #     num_list = input_value.split("/")
        #
        #     answer = 0
        #
        #     for number in num_list:
        #         if number.isnumeric():
        #             answer /= int(number)


class MyCalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    MyCalculatorApp().run()

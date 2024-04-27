import time
from talon import Context, actions, settings, clip
import re


ctx = Context()
ctx.matches = r"""
mode: user.dart
mode: user.auto_lang
and code.language: dart
"""
ctx.tags = ["user.code_operators", "user.code_generic"]

defaultType = "final"
ctx.lists["user.variable_types"] = {
    "mutable": "var",
    "immutable": defaultType,
    "constant": 'const',
}

ctx.lists["user.data_structure_types"] = {
    "list": "List",
    "set": "Set",
    "future": 'Future',
    "map":'Map',
}


data_structure_type_to_empty = {
    "List":'[]',
    "Set":"{}",
    "Map":'{}',
}

ctx.lists["user.code_functions"] = {
    "print": "print",
}



@ctx.action_class("user")
class UserActions:
    def format_and_insert_type(type: str):
        if type in ['int', 'bool', 'void', 'double', 'number', 'dynamic']:
            if(type == 'number'):
                actions.insert('num')
            else:
                actions.insert(type)
        else:
            actions.user.insert_formatted(type, "PUBLIC_CAMEL_CASE")
    
    def constructor_call_named_field(field: str):
        actions.user.insert_formatted(field, "PRIVATE_CAMEL_CASE")
        actions.insert(": ")

    def define_widget(widget_name:str, widget_type: str):
        actions.insert("import 'package:flutter/material.dart';\n")
        if 'Hook' in widget_type:
            actions.insert("import 'package:flutter_hooks/flutter_hooks.dart';\n")
        if 'Consumer' in widget_type:
            actions.insert("import 'package:hooks_riverpod/hooks_riverpod.dart';\n")

        actions.insert('class ')
        actions.user.insert_formatted(widget_name, "PUBLIC_CAMEL_CASE")
        actions.insert(f' extends {widget_type}'+' {')
        actions.key('enter')

    def type_variable(type: str, variable_name: str):
        UserActions.format_and_insert_type(type)
        actions.insert(" ")
        actions.user.insert_formatted(variable_name, "PRIVATE_CAMEL_CASE")

    def initialize_type_variable(type: str, variable_name: str):
        actions.insert("final ")
        UserActions.format_and_insert_type(type)
        actions.insert(" ")
        actions.user.insert_formatted(variable_name, "PRIVATE_CAMEL_CASE")

    def wrap_with_data_structure(dataStructureType: str):
        actions.insert("<")
        actions.key("left:2")
        actions.insert(dataStructureType)

    def code_operator_structure_dereference():
        actions.insert(' => ')
    
    def code_operator_in():
        actions.insert(' in ')

    def format_named_arguments():
        #  final escapingInnerPuzzle = createWaitingRoomInnerPuzzle(delayTime: delayTime, delayPuzzlehash: delayPuzzlehash)
        selected_text = actions.edit.selected_text()    

    
    def localize_text():
        text_raw = clip.get()
        text_no_quotes = text_raw.replace("'", "").strip()
        text=re.sub(r'[^A-Za-z0-9 ]+', '', text_no_quotes)

        actions.insert(',')
        actions.key('enter')
        formatted = ''

        words = text.split(' ')
        print(words)
        first = True
        total_words = 0
        for word in words:
            if first:
                first = False
                formatted += word.lower()
            else:
                formatted += word.capitalize()
            total_words += 1

            if (total_words > 5):
                break

        clip.set_text(f'AppLocalizations.of(context)!.{formatted}')

        actions.insert(f'"{formatted}": "{text_no_quotes}"')

    def define_data_structure(dataStructureType: str, innerType: str):
        actions.insert(dataStructureType)
        actions.insert('<')
        UserActions.format_and_insert_type(innerType)       
        actions.insert('>')

    def initialize_empty_data_structure(dataStructureType: str, innerType: str):
        actions.insert('<')
        UserActions.format_and_insert_type(innerType)       
        actions.insert('>')
        actions.insert(f'{data_structure_type_to_empty[dataStructureType]};')


    def code_initialize_variable(variableType: str, variableName: str):
        if (variableType == "no_spoken_type"):
            actions.insert(defaultType)
        else:
            actions.insert(variableType)
        
        actions.insert(" ")
        actions.user.insert_formatted(variableName, "PRIVATE_CAMEL_CASE")

    def code_construct_object(objectType: str, className: str):
        if (objectType != "no_spoken_type"):
            actions.insert(objectType)
            actions.insert(" ")
        
        actions.user.insert_formatted(className, "PUBLIC_CAMEL_CASE")
        actions.insert("()")
        actions.key('left')

    def code_call_function(text: str):
        actions.user.insert_formatted(text, "PRIVATE_CAMEL_CASE")
        actions.insert('()')
        actions.key('left')

    def code_give_type(type1: str):
        actions.insert(": ")
        print("entered correct function")
        if (type1 == "uuid"):
            actions.user.insert_formatted(type1, "SNAKE_CASE_CAP")
        elif (type1 =="integer"):
            actions.user.insert_formatted("int", "PUBLIC_CAMEL_CASE")
        else:
            actions.user.insert_formatted(type1, "PUBLIC_CAMEL_CASE")
    
    def self_dot(text: str):
        actions.insert('.')
        actions.user.insert_formatted(text, "PUBLIC_CAMEL_CASE")
    
    def code_operator_indirection():
        actions.skip()

    def code_operator_address_of():
        actions.skip()

    def code_operator_lambda():
        actions.auto_insert(" => ")

    def code_operator_subscript():
        actions.insert("[]")
        actions.key("left")

    def code_operator_assignment():
        actions.auto_insert(" = ")

    def code_operator_subtraction():
        actions.auto_insert(" - ")

    def code_operator_subtraction_assignment():
        actions.auto_insert(" -= ")

    def code_operator_addition():
        actions.auto_insert(" + ")

    def code_operator_addition_assignment():
        actions.auto_insert(" += ")

    def code_operator_multiplication():
        actions.auto_insert(" * ")

    def code_operator_multiplication_assignment():
        actions.auto_insert(" *= ")

    def code_operator_exponent():
        actions.auto_insert(" ^ ")

    def code_operator_division():
        actions.auto_insert(" / ")

    def code_operator_division_assignment():
        actions.auto_insert(" /= ")

    def code_operator_modulo():
        actions.auto_insert(" % ")

    def code_operator_modulo_assignment():
        actions.auto_insert(" %= ")

    def code_operator_equal():
        actions.auto_insert(" == ")

    def code_operator_not_equal():
        actions.auto_insert(" != ")

    def code_operator_greater_than():
        actions.auto_insert(" > ")

    def code_operator_greater_than_or_equal_to():
        actions.auto_insert(" >= ")

    def code_operator_less_than():
        actions.auto_insert(" < ")

    def code_operator_less_than_or_equal_to():
        actions.auto_insert(" <= ")

    def code_operator_and():
        actions.auto_insert(" && ")

    def code_operator_or():
        actions.auto_insert(" || ")

    def code_operator_bitwise_and():
        actions.auto_insert(" & ")

    def code_operator_bitwise_or():
        actions.auto_insert(" | ")

    def code_operator_bitwise_exclusive_or():
        actions.auto_insert(" ^ ")

    def code_operator_bitwise_left_shift():
        actions.auto_insert(" << ")

    def code_operator_bitwise_left_shift_assignment():
        actions.auto_insert(" <<= ")

    def code_operator_bitwise_right_shift():
        actions.auto_insert(" >> ")

    def code_operator_bitwise_right_shift_assignment():
        actions.auto_insert(" >>= ")

    def code_self():
        actions.auto_insert("this")

    def code_null():
        actions.auto_insert("null")

    def code_is_null():
        actions.auto_insert(" == null")

    def code_is_not_null():
        actions.auto_insert(" != null")

    def code_state_if():
        actions.insert("if ()")
        actions.key("left")

    def code_state_if_block():
        actions.insert("if () {}")
        actions.key("left")
        actions.key("enter")
        actions.key("up")
        actions.key("right:2")

    def code_state_else_if_block():
        actions.insert("else if () {}")
        actions.key("left")
        actions.key("enter")
        actions.key("up")
        actions.key("right:7")


    def code_state_else_if():
        actions.insert("else if ()")
        actions.key("left")

    def code_state_else():
        actions.insert("else")

    def code_state_else_block():
        actions.insert("else {}")
        actions.key("left")
        actions.key("enter")

    def code_state_switch():
        actions.insert("switch () ")
        actions.key("left")
        actions.edit.left()

    def code_state_case():
        actions.insert("case \nbreak;")
        actions.edit.up()

    def code_state_for():
        actions.insert("for () ")
        actions.key("left")
        actions.key("left")

    def code_state_while():
        actions.insert("while () ")
        actions.edit.left()
        actions.edit.left()

    def code_type_class():
        actions.auto_insert("class ")

    def code_default_function(text: str):
        actions.user.code_public_function(text)

    def code_private_function(text: str):
        actions.insert("private")

    def code_protected_function(text: str):
        actions.user.code_private_function()

    def code_public_function(text: str):
        actions.user.insert_formatted(text, "PRIVATE_CAMEL_CASE")
        actions.insert("() ")
        actions.insert("{")
        # actions.edit.left()
        actions.key("enter")
        actions.edit.up()
        actions.edit.line_end()
        actions.key("left:3")

    def code_function_no_body(text: str):
        actions.insert("fun ")
        actions.user.insert_formatted(text, "PRIVATE_CAMEL_CASE")
        actions.insert("() = ")
        actions.key("left:4")

    def code_typed_function(functionName: str, returnType: str):
        actions.user.insert_formatted(returnType, "PUBLIC_CAMEL_CASE")
        actions.insert(' ')
        actions.user.insert_formatted(functionName, "PRIVATE_CAMEL_CASE")
        actions.insert("() ")
        actions.insert("{")
        # actions.edit.left()
        actions.key("enter")
        actions.edit.up()
        actions.edit.line_end()
        actions.key("left:3")

    def code_typed_arrow_function(functionName: str, returnType: str):
        actions.user.insert_formatted(returnType, "PUBLIC_CAMEL_CASE")
        actions.insert(' ')
        actions.user.insert_formatted(functionName, "PRIVATE_CAMEL_CASE")
        actions.insert("() =>")

    def code_state_return():
        actions.insert("return ")

    def code_insert_function(text: str, selection: str):
        actions.insert(text)
        actions.insert('()')
        actions.key("left")
    
    def code_lambda_function():
        result = "() {}"

        actions.insert(result)
        actions.key("left")
        actions.key("enter")




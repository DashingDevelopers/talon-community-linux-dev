import logging
import os
from datetime import datetime

from talon import Module, actions, registry

global lines_written
lines_written = 0



# repeat the above but in html format
def user_list_to_html_table(file, list_name):
    global lines_written

    command_list = registry.lists[list_name][0].items()
    write_page_break_if_needed(file, len(command_list))
    commandGroup = list_name.replace('user.', '').upper()
    #If the last character of Command Group does not equal s. Then add the character S.
    if commandGroup[-1] != "S":
        commandGroup = commandGroup + "S"
    file.write(f"<h1>{commandGroup}</h1>\n\n")
    # convert this to a two column table
    file.write("<table>\n")
    file.write("<tr><th>Input</th><th>Result</th></tr>\n")
    for key, value in command_list:
        file.write(f"<tr class=context><td>{key}</td><td>{value}</td></tr>\n")
    file.write("</table>\n\n")

    file.write("\n\n")


def write_alphabet(file):
    user_list_to_html_table(file, 'user.letter')


def write_numbers(file):
    user_list_to_html_table(file, 'user.number_key')


def write_modifiers(file):
    user_list_to_html_table(file, 'user.modifier_key')


def write_special(file):
    user_list_to_html_table(file, 'user.special_key')


def write_symbol(file):
    user_list_to_html_table(file, 'user.symbol_key')


def write_arrow(file):
    user_list_to_html_table(file, 'user.arrow_key')


def write_punctuation(file):
    user_list_to_html_table(file, 'user.punctuation')


def write_function(file):
    user_list_to_html_table(file, 'user.function_key')


def write_formatters(file):
    user_list_to_html_table(file, 'user.formatters')



def write_context_commands(key, file, commands):
    global lines_written
    # write out each command and it's implementation

    write_page_break_if_needed(file, len(commands))
    pretty_print_context_name(file, key)

    file.write("<table class='contexts'>\n")
    file.write("<tr><th>Input</th><th>Result</th></tr>\n")

    #sort the commands by the rule
    commands = dict(sorted(commands.items()))
    #sorted by item
    # commands = {k: v for k, v in sorted(commands.items(), key=lambda item: item[1].target.code)}

    previousRule= ""
    rowCount = 0

    for key in commands:
        rowCount += 1
        try:
            rule = commands[key].rule.rule
            implementation = commands[key].target.code.replace("\n", "\n<br/>")
        except Exception:
            continue

        ruleHtmlEscaped = escapeHtml(rule)

        #        #.replace('/n', '<br>')

        #emove any text following a hash # symbol if the length > 20 chqars
        if len(implementation) > 20:
          implementation = implementation.split('#')[0]
        result = escapeHtml(implementation)

        #if the rowCount is greater than 5 and the first 2 characters of the rule are the same as the first 2 characters of the previous rule
        #then add a blank row
        # if ((rowCount > 5 and rule[:2] != previousRule[:2]) or (rowCount > 7 and rule[:rowCount] != previousRule[:rowCount])):
        if ((rowCount > 5 and rule[:rowCount] != previousRule[:rowCount])):

            file.write("<tr class=blank><td>&nbsp;</td><td></td></tr>\n")
            rowCount = 0
        previousRule = rule
        file.write(
            f"<tr class=context><td>{ruleHtmlEscaped}</td><td>{result}</td></tr>\n")


        lines_written += 1

    file.write("</table>\n\n")

def escapeHtml(htmltobe):
    return htmltobe.replace("<", "&lt;").replace(">", "&gt;")


def pretty_print_context_name(file, name):
    ## The logic here is intended to only print from talon files that have actual voice commands.
    splits = name.split(".")
    index = -1

    os = ""

    if "mac" in name:
        os = "mac"
    if "win" in name:
        os = "win"
    if "linux" in name:
        os = "linux"

    if "talon" in splits[index]:
        index = -2
        short_name = splits[index].replace("_", " ")
    else:
        short_name = splits[index].replace("_", " ")

    if "mac" == short_name or "win" == short_name or "linux" == short_name:
        index = index - 1
        short_name = splits[index].replace("_", " ")

    global lines_written
    file.write("<h2>" + short_name.upper() + "</h2>")


def write_page_break_if_needed(file, size_of_next_list):
    global lines_written
    if lines_written+size_of_next_list > 40:
        file.write('<p style="page-break-after: always;"><hr/></p>')
        lines_written = 0


mod = Module()


def write_html_header(file):
    file.write("""<!DOCTYPE html>
        <html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
        <head>
          <meta charset="utf-8" />
          <meta name="generator" content="pandoc" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
          <title>cheatsheet</title>
          <style>
            code{white-space: pre-wrap;}
            span.smallcaps{font-variant: small-caps;}
            span.underline{text-decoration: underline;}
            div.column{display: inline-block; vertical-align: top; width: 50%;}
            div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;}
            ul.task-list{list-style: none;}
          </style>
          <link rel="stylesheet" href="cheatsheet.css" />
        </head>
        <body>""")


@mod.action_class
class user_actions:
    def cheatsheet():
        """Print out a sheet of talon commands"""
        # open file
        logging.info(
            f"generating cheat sheet in {os.path.dirname(os.path.realpath(__file__))}"
        )
        this_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(this_dir, 'cheat_sheet.html')
        file = open(file_path, "w")
        write_html_header(file)
        file.write(f"<h1 align=center>Talon Cheat Sheet</h1>\n\n")
        file.write(f"<p align=center>Generated on: {datetime.now()}</p>\n\n")
        # write_arrow(file)
        # write_function(file)
        # write_modifiers(file)
        # write_numbers(file)
        # write_special(file)

        write_alphabet(file)
        write_formatters(file)
        write_punctuation(file)
        write_symbol(file)

        # print out all the commands in all of the contexts

        list_of_contexts = dict(registry.contexts.items())
        sorted_keys = sorted(list_of_contexts)

        for key in sorted_keys:
            value = list_of_contexts[key]
            commands = value.commands  # Get all the commands from a context
            if len(commands) > 0:

                write_context_commands(key, file, commands)

        file.write(f"<h1 align=center>End of Talon Cheat Sheet</h1>\n\n")
        file.write("</body></html>")
        file.close()

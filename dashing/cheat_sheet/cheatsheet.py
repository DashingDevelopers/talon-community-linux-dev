import os

from talon import Module, actions, registry

global linecount
linecount = 0


def list_to_markdown_table(file, list_name):
    list_to_html_table(file, list_name)



# repeat the above but in html format
def list_to_html_table(file, list_name):
    file.write(f"<h1>yo {list_name} </h1>\n\n")
    command_list = registry.lists[list_name][0].items()

    file.write("<h2>command word  {list_name}</h2> \n\n")

    # convert this to a two column table
    file.write("<table>\n")
    file.write("<tr><th>command</th><th>word</th></tr>\n")
    for key, value in command_list:
        file.write(f"<tr><td>{key}</td><td>{value}</td></tr>\n")
    file.write("</table>\n\n")

    file.write("\n\n")


def write_alphabet(file):
    list_to_markdown_table(file, 'user.letter')


def write_numbers(file):
    list_to_markdown_table(file, 'user.number_key')


def write_modifiers(file):
    list_to_markdown_table(file, 'user.modifier_key')


def write_special(file):
    list_to_markdown_table(file, 'user.special_key')


def write_symbol(file):
    list_to_markdown_table(file, 'user.symbol_key')


def write_arrow(file):
    list_to_markdown_table(file, 'user.arrow_key')


def write_punctuation(file):
    list_to_markdown_table(file, 'user.punctuation')


def write_function(file):
    list_to_markdown_table(file, 'user.function_key')


def write_formatters(file):
    global linecount
    writepagebreak(file)
    file.write(f"<h2>formatters</h2> \n\n")
    command_list = registry.lists['user.formatters'][0].items()


    # convert this to a two column table
    file.write("<table>\n")
    file.write("<tr><th>command</th><th>word</th></tr>\n")
    for key, value in command_list:
        file.write(f"<tr><td>{key}</td><td>{value}</td></tr>\n")
    file.write("</table>\n\n")

    linecount += 1


def write_context_commands(file, commands):
    global linecount
    # write out each command and it's implementation

    writepagebreak(file)

    for key in commands:
        try:
            rule = commands[key].rule.rule
            implementation = commands[key].target.code.replace("\n", "\n\t\t")
        except Exception:
            continue
        # file.write("\n-**" + rule + "**  `" + implementation + "`\n")
        # file.write( "> **"+ rule + "** `" + implementation + "` \n>\n")
        ruleHtmlEscaped = escapeHtml(rule)
        file.write("<p>rule: " +ruleHtmlEscaped + " , imp:" + escapeHtml(implementation).replace("/n",'<br>') + "</p>")
        linecount += 1


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
        index = index-1
        short_name = splits[index].replace("_", " ")

    global linecount
    writepagebreak(file)
    # file.write("<h2>" + "# " + os + " " + short_name + "</h2>")
    file.write("<h2>"  + short_name + "</h2>")


def writepagebreak(file):
    global linecount
    if linecount > 20:
        file.write('<p style="page-break-after: always;">&nbsp;</p>')
        # file.write('<p style="page-break-before: always;">&nbsp;</p>')
        linecount = 0


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

        this_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(this_dir, 'cheat_sheet.html')
        file = open(file_path, "w")
        write_html_header(file)
        file.write(f"<h1> Talon Cheat Sheet </h1>\n\n")

        write_alphabet(file)
        # write_numbers(file)
        # write_modifiers(file)
        # write_special(file)
        write_symbol(file)
        # write_arrow(file)
        write_punctuation(file)
        # Is never on things write_function(file)

        write_formatters(file)

        # print out all the commands in all of the contexts

        list_of_contexts = registry.contexts.items()
        for key, value in list_of_contexts:
            #
            commands = value.commands  # Get all the commands from a context
            if len(commands) > 0:
                pretty_print_context_name(file, key)
                write_context_commands(file, commands)
        file.close()

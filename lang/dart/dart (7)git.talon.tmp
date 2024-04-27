mode: user.dart
mode: user.auto_lang
and code.language: dart
-

op question: ' ? '

op double question: ' ?? '
op colon: ' : '

op as: ' as '

read ref: 
    insert('ref.read()')
    key('left')

watch ref: 
    insert('ref.watch()')
    key('left')


state color theme: 'Theme.of(context).colorScheme'

state text theme: 'Theme.of(context).textTheme'

new consumer widget <user.text>:
    user.define_widget(text, 'ConsumerWidget')

new hook consumer widget <user.text>:
    user.define_widget(text, 'HookConsumerWidget')

new widget <user.text>:
    user.define_widget(text, 'StatelessWidget')


construct field: 'required this.'

variable <user.text> of type <user.text>$:user.type_variable(text_2, text_1)
class variable <user.text> of type <user.text>$:user.initialize_type_variable(text_2, text_1)

type <user.text> $: user.format_and_insert_type(text)

^funky <user.text>$: user.code_public_function(text)
^typed funky <user.text> returning <user.text>$: user.code_typed_function(text_1, text_2)
# ^member funky <user.text>$: user.code_public_function(text)

make local: user.localize_text()

json object: 'Map<String, dynamic>'

app localizations: 'AppLocalizations.of(context)!'

make from jason: '.fromJson(Map<String, dynamic> json)'

make to json: 
    insert('Map<String, dynamic> toJson() => <String, dynamic>{')
    key('enter')

# [{user.data_structure_types}] of <user.text> : user.define_data_structure(data_structure_types, text)

(wrap | rap) [{user.data_structure_types}]: user.wrap_with_data_structure(data_structure_types)

state null return: 'return null;'

new provider: 'Provider((ref) {},);'
new family provider: 'Provider.family((ref, arg) {},);'

state try catch: 
    insert('try {}')
    key('left')
    key('enter')
    key('down')
    insert('on Exception catch(e) {}')
    key('left')
    key('enter')
    key('enter')
    key('up')

logging error: 
    insert('LoggingContext().error()')
    key('left')

logging info: 
    insert('LoggingContext().info()')
    key('left')

make to do: '// TODO(nvjoshi2): '

^lambda funky: user.code_lambda_function()
async lambda funky: 
    insert("() async {}")
    key("left")
    key("enter")

state indexed for: 
    insert('for(var i = 0; i< X; i++){}')
    key("left")
    key("enter")

state const: 'const '

state use state: 
    insert('useState()')
    key("left")

state for block: 
    insert('for () {}')
    key("left")
    key("enter")
    key('up')
    key("right:3")


state use memoized: 
    insert('useMemoized()')
    key("left")

state async when: ".when(data: (data) {},error: (error, stackTrace) => const DefaultError(message: '',),loading: DefaultLoading.new,)"

import flutter hooks: "import 'package:flutter_hooks/flutter_hooks.dart';"

interpolate string: 
    insert('${}')
    key("left")

state sleep: 'await Future<void>.delayed(const Duration(seconds: ))'
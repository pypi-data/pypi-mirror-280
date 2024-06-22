from frontend.middle import *
from utils.nodes import *
from utils.logging import *
from codex import ok, warning, error, dblog

from frontend.lexy import lexer
from frontend.percy import parser
from frontend.main import check_flows, check_builds, check_shapes



file = ''
with open('./demo.fl', 'r') as fb:
    file = fb.read()
    print(file)

lexer.input(file)
ast = parser.parse(file, lexer = lexer, tracking = True)

for each in ast:
    print(type(each), FlowDef, type(each) == FlowDef, isinstance(each, FlowDef))

ast = Program(
    name = None,
    flows = list(filter(lambda x: type(x) == FlowDef, ast)),
    builds = list(filter(lambda x: type(x) == Build, ast))
)
print(ast)
ast = iron(ast)
print(checked('AST ironed...'))


check_flows(ast)
ok(checked('Flows semantically checked...'))


check_builds(ast)
ok(checked('Builds semantically checked...'))


print(ast)

build = None
if build is None: build = ast.builds[-1]
else:
    for each in ast.builds:
        if each.name == build:
            build = each
warning(f'Building from `{build.name}`...')
context = contextfrombuild(build, ast)
print(checked('Context successfully built...'))


check_shapes(build, context)

print(context)
print(context.ichains)

from cli import *

show_chain(file, context.ichains['w'], context)

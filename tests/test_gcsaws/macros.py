from gcsaws.nodes import AcceptChildScriptTemplate, NodeScriptTemplate, AcceptChildStepFunction, NodeStepFunction
from gcscore.mod import BaseContext


def macro_manage_linux_server(parent: AcceptChildScriptTemplate,
                              context: BaseContext,
                              action: str,
                              environment: str,
                              server_name: str
                              ) -> NodeScriptTemplate:
    node = parent.run_script_template(f'{action}_{server_name}') \
        .on_targets(context.targets.select_by_name(server_name)) \
        .shell() \
        .command(f'{environment}/{server_name}/{action}.sh')
    if context.variables.get('compact_scripts'):
        node.compact()
    return node


def macro_send_mail(parent: AcceptChildStepFunction,
                    context: BaseContext,
                    name: str,
                    message_template: str,
                    extra_context: dict = None) -> NodeStepFunction:
    node = parent.run_step_function(name)
    node.function_name('sf-message-ses')
    node.payload({
        'template': message_template,
        'context': context.variables['messaging']['context'],
        'extra_context': extra_context,
        'to': context.variables['messaging']['to'],
        'from': context.variables['messaging']['from']
    })
    return node

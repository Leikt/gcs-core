from gcsaws import *
from gcscore.mod import BaseContext

from macros import macro_send_mail, macro_manage_linux_server


def main(context: BaseContext) -> Procedure:
    proc = Procedure('stop_sbx').description('Stop the SBX servers in the right order.')

    if context.variables.get('pause_before_start'):
        proc.pause('pause_before_start').identifier('stop_sbx,pause_before_start')\
            .description('Pause the automation so the operator can do some verification before really starting it.')

    macro_send_mail(proc, context, 'send_start_mail', 'stop/beginning.html', {'targets': context.targets.all})\
        .description('Notifies everyone that an operation is going on.')

    stop_systems = proc.run_in_parallel('stop_systems').description('All SBX system can be stopped in parallel')
    for server_name in ['vm01', 'vm02']:
        macro_manage_linux_server(stop_systems, context, 'stop', 'sbx', server_name)\
            .description(f'Run the stop script on {server_name}')

    if context.variables.get('pause_before_end'):
        proc.pause('pause_before_end').identifier('stop_sbx,pause_before_end')\
            .description('Pause the automation so the operator can do some verification before sending the end email.')

    macro_send_mail(proc, context, 'send_end_mail', 'stop/end.html', {'targets': context.targets.all})\
        .description('Notifies everyone that the operation is finished.')

    return proc

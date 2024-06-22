"""Start websocket connection."""

import ssl
import threading

import daemon as py_daemon
import rich_click as click
import websocket

from oxpecker import WORK_DIR, WS_URL, auth
from oxpecker.utils import retry_if_network_error
from oxpecker.ws_demo import on_close, on_error, on_message, on_open, start_heartbeat
from oxpecker.tunnel import tunnel


def ws_conn():
    websocket.enableTrace(True)

    ws = websocket.WebSocketApp(
        WS_URL,
        header=auth,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    # FIXME: sikp verify only explicitly.
    start_heartbeat(ws)
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


@click.command(help="Connect to the websocket server for bidirectional communication.")
@click.pass_context
@click.option(
    "--detach/--no-detach",
    is_flag=True,
    help="[Experimental] Connect and put the process in background.",
    default=False,
)
# XXX: copied and pasted from tunnle.py.
@click.option("--local-host", default="localhost", show_default=True)
@click.option("--local-port", default=22, show_default=True)
@click.option(
    "--remote-proto", default="tcp", help="Remote protocol.", show_default=True
)
@click.option("--remote-host", default="", help="Remote host.", show_default=True)
@click.option("--remote-port", help="Remote port.", show_default=True)
@retry_if_network_error()
def serve(ctx, detach, local_host, local_port, remote_proto, remote_host, remote_port):
    """Connect to the websocket server."""
    if detach:
        with py_daemon.DaemonContext(
            pidfile=(WORK_DIR / "serve.pid").open("w"),
            stdout=(WORK_DIR / "serve.out.log").open("w+"),
            stderr=(WORK_DIR / "serve.err.log").open("w+"),
        ) as dc:
            t = threading.Thread(
                target=ctx.invoke,
                args=(tunnel,),
                kwargs={
                    "local_host": local_host,
                    "local_port": local_port,
                    "remote_proto": remote_proto,
                    "remote_host": remote_host,
                    "remote_port": remote_port,
                },
            )
            ws_conn()
            click.echo(f"{dc.pidfile} = ")
    else:
        t = threading.Thread(
            target=ctx.invoke,
            args=(tunnel,),
            kwargs={
                "local_host": local_host,
                "local_port": local_port,
                "remote_proto": remote_proto,
                "remote_host": remote_host,
                "remote_port": remote_port,
            },
        )
        t.start()
        ws_conn()


if __name__ == "__main__":
    serve()  # pylint: disable=no-value-for-parameter

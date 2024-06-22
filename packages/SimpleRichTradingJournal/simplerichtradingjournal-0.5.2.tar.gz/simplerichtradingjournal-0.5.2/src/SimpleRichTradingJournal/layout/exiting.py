import dash_bootstrap_components as dbc
from dash import html

import __env__
from config import imgs

MODAL = dbc.Modal(
    [
        exit_modal_head := dbc.ModalHeader(
            dbc.ModalTitle("Terminate Server"),
            id="exit_modal_head_",
            close_button=True,
        ),
        exit_modal_body := dbc.ModalBody(
            id="exit_modal_body_",
        ),
        dbc.ModalFooter(
            exit_modal_button := dbc.Button(
                "Ok",
                id="exit_modal_button_",
            )
        )
    ],
    id="exit_modal_",
    scrollable=True,
)

exit_button = html.Button(
    imgs.cross,
    id="exit_button_",
    style={
        "display": "inline-block",
        "margin": "7px",
        "fontSize": "13px",
        "paddingLeft": "10px",
        "paddingRight": "10px",
        "borderRadius": "15px",
        "backgroundColor": __env__.color_theme.cell_negvalue,
        "border": "1px solid " + __env__.color_theme.table_sep,
        "opacity": 0.7,
    },
)

COMPONENTS = html.Div([
    MODAL
])

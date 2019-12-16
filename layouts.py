# layouts

import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

topic = html.H6('''
    All the code, including Machine Learning algorithms, which is used at the site is real and \
    can be easily implemented into your application or Soft-as-a-Service.
    ''', style = {'background-image': 'linear-gradient(to right, lightgrey , lightgrey)'})

card_content_1 = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H6("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]

card_content_2 = dbc.CardBody(
    [
        html.Blockquote(
            [
                dcc.Markdown(
                    """
                    Companies need to use data to run and grow their everyday business. 
                    The fundamental goal of data science is to help companies make quicker 
                    and better decisions, which can take them to the top of their market, 
                    or at least – especially in the toughest red oceans – be a matter 
                    of long-term survival."""
                ),
                html.Footer(
                    html.Small("deepsence.ai", className="text-muted")
                ),
            ],
            className="blockquote",
        )
    ]
)

card_content_dataScience = [
    dbc.CardImg(src="/assets/images/back2.jpeg", top=True),
    dbc.CardBody(
        [
            html.H6("Data Science to help your business", className="card-title"),
            html.P(
                "Human should create but computer must work - this is the basic principle for our business. \
                Suppose you have a little business and need to predict your sales. Click the button below and \
                try to feel your sales during the time then predict your profit using different models",
                className="card-text",
            ),
            dbc.Button("Make prediction", color="success", href="/apps/business"),
        ]
    ),
]


card_content_OCR = [
    dbc.CardImg(src="/assets/images/ocr.jpeg", top=True),
    dbc.CardBody(
        [
            html.H6("Optical character recognition", className="card-title"),
            html.P(
                "Optical character recognition or optical character reader (OCR) \
                is the electronic or mechanical conversion of images of typed, \
                handwritten or printed text into machine-encoded text, whether \
                from a scanned document, a photo of a document, a scene-photo \
                (for example the text on signs and billboards in a landscape photo) \
                or from subtitle text superimposed on an image (for example from a television broadcast)",
                className="card-text",
            ),
            html.Footer(
                    html.Small("https://en.wikipedia.org/wiki/Optical_character_recognition", className="text-muted")),
            dbc.Button("Try", color="primary", href="/apps/ocr", disabled=True),
        ]
    ),
]


card_content_time = [
    dbc.CardImg(src="/assets/images/time.jpeg", top=True),
    dbc.CardBody(
        [
            html.H6("Time-series prediction and clustering", className="card-title"),
            html.P(
                "Out system also available to predict time-series, for example, energy or gas \
                consumption to plan your business. Additionally, we are able to identify the \
                groups of consumer to set the best tariff plans for them",
                className="card-text",
            ),
            dbc.Button("Time-series", color="primary", href='/', disabled=True),
        ]
    ),
]


card_content_vision = [
    dbc.CardImg(src="/assets/images/vision.jpeg", top=True),
    dbc.CardBody(
        [
            html.H6("Computer Vision and Human Recognition", className="card-title"),
            html.P(
                "We have developed a simple system to recognize humans at the CCTV. It will let \
                you save your time and make your CCTV system more effective. Try to upload your image \
                and see if we will be able to recognize them. This is low-load system available to work \
                even for microcomputers like Raspberry PI",
                className="card-text",
            ),
            dbc.Button("Try it", color="success", href='/apps/cv'),
        ]
    ),
]


card_content_monitor = [
    dbc.CardImg(src="/assets/images/monitor2.jpeg", top=True),
    dbc.CardBody(
        [
            html.H6("On-line process monitoring", className="card-title"),
            html.P(
                "Our system lets you to monitor tons of the parameters creating user-friendly \
                dashboard. It can include various parameters including numbers, images, levels etc.",
                className="card-text",
            ),
            dbc.Button("Example", color="success", href='/apps/monitor'),
        ]
    ),
]


card_content_online = [
    dbc.CardImg(src="/assets/images/online.jpeg", top=True),
    dbc.CardBody(
        [
            html.H6("Natural Language Processing", className="card-title"),
            html.P(
                "It is very similar to on-line process monitoring but more focused at news or tweet \
                monitoring to recognize trends and providing sentiment analysis. It looks useful for \
                risk assessment, insurance related business and on-line trading",
                className="card-text",
            ),
            dbc.Button("Try", color="success", href='/apps/sentiment'),
        ]
    ),
]


card_content_scrap = [
    dbc.CardImg(src="/assets/images/scrap.jpeg", top=True),
    dbc.CardBody(
        [
            html.H6("Web scrapping and processing", className="card-title"),
            html.P(
                "There are lot of data available in the Internet however very few of them are available \
                in machine-readable format. Our project will help you to scrap all the data around the \
                world to help your business to understand current trends and tendencies and to increase \
                your profit",
                className="card-text",
            ),
            dbc.Button("Example", color="primary", disabled=True),
        ]
    ),
]


card_content_reports = [
    dbc.CardImg(src="/assets/images/report.png", top=True),
    dbc.CardBody(
        [
            html.H6("Report creation", className="card-title"),
            html.P(
                "It is quite similar to on-line monitoring and processing but more focused at the \
                data processing to create printable reports. If you have lots of data which does not \
                change very often it could be your choice to save hundreds of hours for your staff. You \
                can simply feed the system of all your data and have a look at the final report. \
                Of course, it will be used with the very modern Artificial Intelligence technology.",
                className="card-text",
            ),
            dbc.Button("Report example", color="success", href='/dash-financial-report/overview'),
        ]
    ),
]


cards = dbc.CardColumns(
    [
        #dbc.Card(card_content_1, color="primary", inverse=True),
        dbc.Card(card_content_2, body=True),
        #dbc.Card(card_content_1, color="secondary", inverse=True),
        dbc.Card(card_content_dataScience, color="info", inverse=True),
        dbc.Card(card_content_vision, color="info", inverse=True),
        dbc.Card(card_content_monitor, color="info", inverse=True),
        dbc.Card(card_content_online, color="info", inverse=True),
        dbc.Card(card_content_scrap, color="info", inverse=True),
        dbc.Card(card_content_reports, color="info", inverse=True),
        dbc.Card(card_content_time, color="info", inverse=True),
        dbc.Card(card_content_OCR, color="info", inverse=True),
        #dbc.Card(card_content_1, color="success", inverse=True),
        #dbc.Card(card_content_1, color="warning", inverse=True),
        #dbc.Card(card_content_1, color="danger", inverse=True),
        #dbc.Card(card_content_3, color="light"),
        #dbc.Card(card_content_1, color="dark", inverse=True),
    ]
)


search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button("Search", color="primary", className="ml-2"),
            width="auto",
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.NavbarSimple(
    #children=[
    #    dbc.NavItem(dbc.NavLink("Main page", href="/")),
    #    dbc.DropdownMenu(
    #        children=[
    #            dbc.DropdownMenuItem("More pages", header=True),
    #            dbc.DropdownMenuItem("Page 2", href="#"),
    #            dbc.DropdownMenuItem("Page 3", href="#"),
    #        ],
    #        nav=True,
    #        in_navbar=True,
    #        label="More",
    #    ),
    #],
    brand="Data Science Delivery Company",
    brand_href="/",
    color="primary",
    dark=True,
)
import pandas as pd
import requests
from bs4 import BeautifulSoup
stream_urls_dict = {}
stream_urls_dict['Jason Cooley'] = 'https://livestormchasing.com/chasers/jason.cooley'
stream_urls_dict['Steve Wooten'] = 'https://livestormchasing.com/chasers/steve.wooten'
stream_urls_dict['Brett Adair'] = 'https://livestormchasing.com/chasers/brett.adair'
stream_urls_dict['Michael Craddock'] = 'https://livestormchasing.com/chasers/michael.craddock'
stream_urls_dict['Ryan McCarthy'] = 'https://livestormchasing.com/chasers/ryan.mccarthy'
stream_urls_dict['Brad Arnold'] = 'https://livestormchasing.com/chasers/brad.arnold'
stream_urls_dict['James McMullin'] = 'https://livestormchasing.com/chasers/james.mcmullin'
stream_urls_dict['Eric Tole'] = 'https://livestormchasing.com/chasers/eric.tole'
stream_urls_dict['Joshua Myers'] = 'https://livestormchasing.com/chasers/joshua.myers'
stream_urls_dict['Kory Poggenpohl'] = 'https://livestormchasing.com/chasers/kory.poggenpohl'
stream_urls_dict['Ryan Cartee'] = 'https://livestormchasing.com/chasers/ryan.cartee'
stream_urls_dict['Jason Cooley'] = 'https://livestormchasing.com/chasers/jason.cooley'
stream_urls_dict['Brett Adair'] = 'https://livestormchasing.com/chasers/brett.adair'
stream_urls_dict['Steve Wooten'] = 'https://livestormchasing.com/chasers/steve.wooten'
stream_urls_dict['Colby Ward'] = 'https://livestormchasing.com/chasers/colby.ward'
stream_urls_dict['Michael Craddock'] = 'https://livestormchasing.com/chasers/michael.craddock'
stream_urls_dict['Ryan McCarthy'] = 'https://livestormchasing.com/chasers/ryan.mccarthy'
stream_urls_dict['David Gaede'] = 'https://livestormchasing.com/chasers/david.gaede'
stream_urls_dict['Brad Arnold'] = 'https://livestormchasing.com/chasers/brad.arnold'
stream_urls_dict['James McMullin'] = 'https://livestormchasing.com/chasers/james.mcmullin'


def get_streams(streams_urls_dict):
    streams = []
    videos = []
    for stream_name, stream_url in streams_urls_dict.items():
        try:
            response = requests.get(stream_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            stream = {}
            stream['stream_name'] = stream_name
            # find stream content at #stream > div > div.container > video css selector
            stream['stream_url'] = soup.select('#stream > div > div.container > video')[0]['src']
            # save stream as a viewable video to the html dashboard and save the video to a local directory
            print(stream['stream_url'])

        except Exception as e:
            print(e)
            continue


def create_panel(streams):
    panel = pn.Column()
    for stream in streams:
        stream_panel = pn.Column(
            pn.pane.HTML(
                f"""
                <h3>{stream['stream_name']}</h3>
                <p>{stream['stream_description']}</p>
                <p>{stream['stream_location']}</p>
                <p>{stream['stream_viewers']}</p>
                <p>{stream['stream_tags']}</p>
                <p>{stream['stream_start_time']}</p>
                <p>{stream['stream_end_time']}</p>
                <p>{stream['stream_duration']}</p>
                <p>{stream['stream_category']}</p>
                <p>{stream['stream_language']}</p>
                <p>{stream['stream_country']}</p>
                <p>{stream['stream_state']}</p>
                <p>{stream['stream_city']}</p>
                <p>{stream['stream_latitude']}</p>
                <p>{stream['stream_longitude']}</p>
                """
            ),
            pn.pane.HTML(
                f"""
                <iframe src="{stream['stream_url']}" width="560" height="315" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
                """
            )
        )
        panel.append(stream_panel)
    return panel
import panel as pn
streams_result = get_streams(stream_urls_dict)
panel_result = create_panel(streams_result)
panel_result.servable()
pn.pane.HTML(
    f"""
    <iframe src="{streams_result[0]['stream_url']}" width="560" height="315" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
    """
)

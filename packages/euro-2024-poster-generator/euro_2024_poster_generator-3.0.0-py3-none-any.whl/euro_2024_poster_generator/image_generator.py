import datetime
import requests
from io import BytesIO
from slugify import slugify
from PIL import Image, ImageDraw, ImageFont

def get_image(url):
    response = requests.get(url)
    response.raise_for_status()
    return Image.open(BytesIO(response.content))

def prepare(home_team, away_team, home_logo_url, away_logo_url):
    # Load the background image
    background_path = "./assets/img/euro-2024-bg.jpg"
    image = Image.open(background_path).convert("RGBA")

    # Initialize drawing context
    draw = ImageDraw.Draw(image)

    # Load fonts
    font_path = "./assets/fonts/montserrat-semibold.ttf"
    teams_name_font = ImageFont.truetype(font_path, 90)

    # Function to draw text with specified position
    def draw_text(draw, text, font, x, y):
        draw.text((x, y), text, fill='white', font=font)

    # Home team name
    home_team_x = 290
    home_team_y = 488
    draw_text(draw, home_team, teams_name_font, home_team_x, home_team_y)

    # Away team name
    away_team_x = 1410
    away_team_y = 488
    draw_text(draw, away_team, teams_name_font, away_team_x, away_team_y)

    # Download and resize team logos
    home_logo = get_image(home_logo_url).convert("RGBA")
    away_logo = get_image(away_logo_url).convert("RGBA")
    logo_size = (350, 350)
    home_logo = home_logo.resize(logo_size, Image.LANCZOS)
    away_logo = away_logo.resize(logo_size, Image.LANCZOS)

    # Calculate logo positions
    home_logo_x = 252
    home_logo_y = 122
    away_logo_x = 1339
    away_logo_y = 122

    # Paste logos onto the image
    image.paste(home_logo, (home_logo_x, home_logo_y), home_logo)
    image.paste(away_logo, (away_logo_x, away_logo_y), away_logo)

    # Save the image
    current_date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    image_path = f"./generated/{slugify(home_team)}-vs-{slugify(away_team)}-{current_date}.png"
    image.save(image_path)
    return image_path

def generate(match_id):
    try:
        res = requests.get(f"https://prosoccer.tv/api/fixtures?t=info&id={match_id}")
        res.raise_for_status()
        
        data = res.json()
        match = data.get('data')
        
        if match is None:
            return 'No match data found.'

        home_team = match['teams']['home']['name']
        away_team = match['teams']['away']['name']
        home_logo_url = match['teams']['home']['img']
        away_logo_url = match['teams']['away']['img']

        return prepare(home_team, away_team, home_logo_url, away_logo_url)
    except Exception as e:
        return f'An unexpected error occurred: {e}'
    
# match_id = input('Match ID: ')
# generate(match_id)
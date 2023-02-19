# Import the required libraries
from PIL import Image, ImageDraw, ImageFont
import pandas as pd


def generate_certificates(participans_list: list, certificate_template_path: str, font_path: str):

    for participant in participants_list:

        # Adjust the position according to your sample
        text_y_position = 975
        text_x_position = 1650
        # text_x_position = (image_width - text_width) / 2 # center

        # Open the certificate template
        certificate_template = Image.open(certificate_template_path, mode='r')

        # Get the certificate template width
        image_width = certificate_template.width

        # Get the certificate template height
        image_height = certificate_template.height

        # Create a drawing canvas overlay on top of the certificate template
        draw = ImageDraw.Draw(certificate_template)

        # Get the font object from the font file (TTF)
        font = ImageFont.truetype(
            font_path,
            size=100  # Adjust the font size according to your sample
        )

        # Fetche the text width for calculations
        text_width, _ = draw.textsize(participant, font=font)

        # Add the name on the certificate
        draw.text(
            (
                # this calculation is done
                # to centre the image
                text_x_position,
                text_y_position
            ),
            participant,
            font=font,
            fill='black')

        # Save the certificate in png format
        certificate_template.save(
            "generated_certificates\{}.png".format(participant))

# Function to create a list of participants from a CSV file


def create_participant_list(csv_file_path: str):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Get the list of participants
    participants_list = df['Names'].tolist()

    return participants_list


# Driver Code
if __name__ == "__main__":

    # path to csv file
    csv_file_path = "participant_list.csv"

    # some example of names
    participants_list = create_participant_list(csv_file_path)

    # path to font
    font_path = "OpenSans-Regular.ttf"

    # path to sample certificate
    certificate_template_path = "certificate_template.png"

    generate_certificates(
        participants_list, certificate_template_path, font_path)

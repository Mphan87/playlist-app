"""Forms for playlist app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired



class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Playlist Name", validators=[InputRequired()],)
    description = StringField("description")
  

class SongForm(FlaskForm):
    """Form for adding songs."""

    artist = StringField("artist", validators=[InputRequired()],)
    title = StringField("title", validators=[InputRequired()],)
    


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""
    song = SelectField('Song To Add')
    







from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    return redirect("/playlists")

@app.route("/playlists")
def show_all_playlists():
    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)

@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    playlist = Playlist.query.get_or_404(playlist_id)
    wow = PlaylistSong.query.filter(PlaylistSong.playlist_id == playlist_id).all()  
    return render_template("playlist.html", playlist = playlist, wow = wow)

@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    form = PlaylistForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        new_playlist = Playlist(name = name, description = description)
        db.session.add(new_playlist)
        db.session.commit()
        return redirect("/playlists")
    else:
        return render_template("new_playlist.html", form = form)
    
@app.route("/songs")
def show_all_songs():
    songs = Song.query.all()
    return render_template("songs.html", songs=songs)

@app.route("/songs/<int:song_id>")
def show_song(song_id):
    song = Song.query.get_or_404(song_id)
    wow = PlaylistSong.query.filter(PlaylistSong.song_id == song_id).all()
    return render_template("song.html", song = song, wow = wow)

@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    form = SongForm()

    if form.validate_on_submit():
        title = form.title.data
        artist = form.artist.data
        new_song = Song(title = title, artist = artist)
        db.session.add(new_song)
        db.session.commit()
        return redirect("/songs")
    else:
        return render_template("new_song.html", form = form)
    

@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):

  playlist = Playlist.query.get_or_404(playlist_id)
  form = NewSongForPlaylistForm()

  curr_on_playlist = [s.id for s in playlist.playlistsongs]
  form.song.choices = (db.session.query(Song.id, Song.title).filter(Song.id.notin_(curr_on_playlist)).all())

  if form.validate_on_submit():
      selection = form.song.data[1]
      playlist_song = PlaylistSong(song_id=selection,playlist_id=playlist_id)
      print(form.song.data)
      db.session.add(playlist_song)
      db.session.commit()
      return redirect(f"/playlists/{playlist_id}")

  return render_template("add_song_to_playlist.html",playlist=playlist, form=form)


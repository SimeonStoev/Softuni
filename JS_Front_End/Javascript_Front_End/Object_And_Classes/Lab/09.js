function songs(songsList) {
    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
    }

    let typeList = songsList[songsList.length - 1];
    let songsData = songsList.slice(1, songsList.length - 1);
    let songs = [];

    for (let song of songsData) {
        let [type, name, time] = song.split("_");
        songs.push(new Song(type, name, time));
    }

    for (let song of songs) {
        if (song.typeList === typeList || typeList === "all") {
            console.log(song.name);
        }
    }
}

songs([2,
    'like_Replay_3:15',
    'ban_Photoshop_3:48',
    'all']
);
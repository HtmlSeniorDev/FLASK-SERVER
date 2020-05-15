
from api.Repository.GridFsDao import GridFsDao


class ServiceAudio:
    grid_save = GridFsDao()

    def add_audio(self, user_id, audio_files):
        return self.grid_save.save_audio(audio_files, user_id)

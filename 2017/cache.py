import video

class cache:
  def __init__(self, capa):
    self.capacity = capa
    self.list = []
    self.size = 0

  def addVideo(self, video):
    self.list.append(video)
    self.size += video.size